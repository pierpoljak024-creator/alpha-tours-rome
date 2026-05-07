#!/usr/bin/env node
/**
 * review-watchdog.mjs — Automated review checker
 *
 * Runs review-manager.mjs fetch + draft periodically.
 * Designed to be run by cron / Modal scheduler every 6 hours.
 *
 * Usage:
 *   node tools/review-watchdog.mjs              # Normal run (fetch + draft)
 *   node tools/review-watchdog.mjs --quiet       # Silent run (no output if no new reviews)
 *   node tools/review-watchdog.mjs --once        # Single check, exit
 *   node tools/review-watchdog.mjs --loop        # Continuous loop every 6 hours
 */

import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REVIEW_MANAGER = path.join(__dirname, 'review-manager.mjs');
const LOG_FILE = path.join(__dirname, 'watchdog.log');
const STATE_FILE = path.join(__dirname, 'watchdog-state.json');

const CHECK_INTERVAL_MS = 6 * 60 * 60 * 1000; // 6 hours

function log(msg) {
  const timestamp = new Date().toISOString();
  const line = `[${timestamp}] ${msg}`;
  console.log(line);
  try {
    fs.appendFileSync(LOG_FILE, line + '\n', 'utf-8');
  } catch (e) {
    // Silently ignore if we can't write log
  }
}

function runNode(script, args = []) {
  return new Promise((resolve, reject) => {
    const child = spawn('node', [script, ...args], {
      cwd: __dirname,
      stdio: ['ignore', 'pipe', 'pipe'],
    });

    let stdout = '';
    let stderr = '';

    child.stdout.on('data', (data) => { stdout += data.toString(); });
    child.stderr.on('data', (data) => { stderr += data.toString(); });

    child.on('close', (code) => {
      if (code !== 0 && stderr) {
        reject(new Error(stderr.trim()));
      } else {
        resolve({ stdout: stdout.trim(), stderr: stderr.trim(), code });
      }
    });

    child.on('error', reject);
  });
}

async function checkReviews(quiet = false) {
  try {
    // Fetch new reviews
    const fetchResult = await runNode(REVIEW_MANAGER, ['fetch']);

    if (fetchResult.stdout.includes('No new reviews')) {
      if (!quiet) {
        log('📭 No new reviews found.');
      }
      return { newReviews: 0 };
    }

    // New reviews found! Log the output
    log('🔍 New reviews detected!');
    log(fetchResult.stdout);

    // Generate drafts
    const draftResult = await runNode(REVIEW_MANAGER, ['draft']);
    log('✍️ Drafts generated:');
    log(draftResult.stdout);

    // Count new reviews
    const match = fetchResult.stdout.match(/(\d+) new review/);
    const count = match ? parseInt(match[1]) : 0;

    // Save state
    const state = {
      lastCheck: new Date().toISOString(),
      lastNewReviews: new Date().toISOString(),
      newReviewCount: count,
    };
    fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2), 'utf-8');

    log(`✅ Watchdog: ${count} new review(s) processed.`);
    return { newReviews: count };
  } catch (err) {
    log(`❌ Watchdog error: ${err.message}`);
    return { error: err.message };
  }
}

async function main() {
  const args = process.argv.slice(2);
  const isQuiet = args.includes('--quiet');
  const isOnce = args.includes('--once');
  const isLoop = args.includes('--loop');

  log('🐶 Review Watchdog started');
  log(`   Mode: ${isLoop ? 'loop (6h interval)' : isOnce ? 'single run' : 'default'}`);

  if (isLoop) {
    // Continuous loop
    while (true) {
      const result = await checkReviews(isQuiet);
      log(`💤 Sleeping for ${CHECK_INTERVAL_MS / 1000 / 60 / 60}h...\n`);
      await new Promise(r => setTimeout(r, CHECK_INTERVAL_MS));
    }
  } else {
    // Single run
    await checkReviews(isQuiet);
    log('🐶 Watchdog run complete.');
  }
}

main().catch(err => {
  log(`💥 Fatal: ${err.message}`);
  process.exit(1);
});
