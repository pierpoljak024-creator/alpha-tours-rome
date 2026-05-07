#!/usr/bin/env node
/**
 * review-manager.mjs — Alpha Tours Rome Google Review Manager
 *
 * Uses NEW Places API v1 (places.googleapis.com) — no OAuth needed, just API key.
 * Copy/Paste only system — generates draft replies for CEO to post on business.google.com.
 *
 * Commands:
 *   node tools/review-manager.mjs fetch     — Fetch latest reviews from Google
 *   node tools/review-manager.mjs draft     — Generate brand-voice draft replies
 *   node tools/review-manager.mjs show      — Show current state
 *   node tools/review-manager.mjs list      — Show ALL reviews in cumulative archive
 *   node tools/review-manager.mjs approve   — Mark drafts as approved
 *   node tools/review-manager.mjs replied <id|--all> — Mark review(s) as replied
 */

import https from 'https';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// ── Configuration ──────────────────────────────────────────────────────────────
const API_KEY = 'AIzaSyBp0MQ_nXd6zhs6z9CU172Ua7q5FSzfBIg';
const PLACE_ID = 'ChIJHcAuWLqLJRMR-nD81t9OlAk';
const PLACES_API_URL = `https://places.googleapis.com/v1/places/${PLACE_ID}`;

// Data files
const SEEN_FILE = path.join(__dirname, 'seen-reviews.json');
const ALL_REVIEWS_FILE = path.join(__dirname, 'all-reviews.json');
const NEW_REVIEWS_FILE = path.join(__dirname, 'new-reviews.json');
const DRAFTS_FILE = path.join(__dirname, 'pending-drafts.json');
const REPLIED_FILE = path.join(__dirname, 'replied-reviews.json');

// ── Utility ────────────────────────────────────────────────────────────────────

function readJSON(filePath, fallback = null) {
  try {
    if (fs.existsSync(filePath)) {
      return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    }
  } catch (e) {
    console.error(`  ⚠ Error reading ${path.basename(filePath)}: ${e.message}`);
  }
  return fallback;
}

function writeJSON(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
}

function httpsGet(url, headers = {}) {
  return new Promise((resolve, reject) => {
    const parsed = new URL(url);
    const options = {
      hostname: parsed.hostname,
      path: parsed.pathname + parsed.search,
      method: 'GET',
      headers: {
        'X-Goog-Api-Key': API_KEY,
        'X-Goog-FieldMask': 'id,displayName,rating,userRatingCount,reviews',
        'X-Goog-Language': 'en',
        ...headers,
      },
      timeout: 15000,
    };
    const req = https.get(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`Parse error: ${e.message}`)); }
      });
    });
    req.on('error', reject);
    req.on('timeout', function () { this.destroy(); reject(new Error('Timeout')); });
    req.end();
  });
}

function generateDraftReply(review) {
  const name = review.name || review.authorAttribution?.displayName || 'Guest';
  const text = (review.originalText?.text || review.text?.text || review.text || '').toLowerCase();

  // Determine tour type from review text
  let tourContext = '';
  if (text.includes('golf cart') || text.includes('golf-cart') || text.includes('golfcart')) {
    tourContext = 'golf cart';
  } else if (text.includes('vespa') || text.includes('sidecar')) {
    tourContext = 'Vespa sidecar';
  } else if (text.includes('fiat') || text.includes('500') || text.includes('dolce vita')) {
    tourContext = 'Fiat 500';
  } else if (text.includes('food') || text.includes('eat') || text.includes('pasta') || text.includes('pizza') || text.includes('trastevere') || text.includes('testaccio') || text.includes('street food')) {
    tourContext = 'food';
  }

  // Generate appropriate reply
  let reply = '';
  const firstLine = `Thank you so much for your wonderful review, ${name}! 🇮🇹`;

  switch (tourContext) {
    case 'golf cart':
      reply = `${firstLine} We're thrilled you enjoyed discovering Rome's highlights with us. Next time, our Vespa sidecar tour is perfect for a romantic evening ride! – Alpha Tours Rome Team`;
      break;
    case 'Vespa sidecar':
      reply = `${firstLine} We're so glad you loved the Vespa sidecar experience! It's truly the most stylish way to see Rome. Next time, try our golf cart tour for a comfortable ride with the whole family! – Alpha Tours Rome Team`;
      break;
    case 'Fiat 500':
      reply = `${firstLine} Grazie mille! 🚗 We're delighted you enjoyed the Dolce Vita experience. Next time, our food tour in Testaccio is perfect for eating your way through Rome! – Alpha Tours Rome Team`;
      break;
    case 'food':
      reply = `${firstLine} Grazie mille! 🍝 We're so happy you loved eating your way through Rome with us. Next time, try our golf cart tour to see Rome's highlights in style! – Alpha Tours Rome Team`;
      break;
    default:
      reply = `${firstLine} We're thrilled you enjoyed the tour and hope to welcome you back for another Roman adventure soon! – Alpha Tours Rome Team`;
  }

  return reply;
}

// ── Commands ───────────────────────────────────────────────────────────────────

async function cmdFetch() {
  console.log('🔍 Fetching latest reviews from Google Places API...\n');

  const result = await httpsGet(PLACES_API_URL);

  if (result.error) {
    console.log(`❌ API Error: ${result.error.message}`);
    if (result.error.details) {
      result.error.details.forEach(d => console.log(`   ${d.field || ''}: ${d.reason || d.message}`));
    }
    process.exit(1);
  }

  const apiReviews = result.reviews || [];
  const placeName = result.displayName?.text || result.id;
  const rating = result.rating || 'N/A';
  const total = result.userRatingCount || 0;

  console.log(`🏪 ${placeName}`);
  console.log(`⭐ Rating: ${rating} / 5  (${total} total reviews)`);
  console.log(`📝 Reviews returned by API: ${apiReviews.length}`);

  // Normalize API reviews to our format
  const normalized = apiReviews.map(r => ({
    reviewId: r.name?.split('/').pop() || r.name,
    name: r.authorAttribution?.displayName || 'Unknown',
    rating: r.rating || 0,
    text: r.originalText?.text || r.text?.text || '',
    time: r.relativePublishTimeDescription || '',
    authorUri: r.authorAttribution?.uri || '',
    authorPhoto: r.authorAttribution?.photoUri || '',
  }));

  // Load seen IDs and all reviews
  const seenIds = new Set(readJSON(SEEN_FILE, []));
  let allReviews = readJSON(ALL_REVIEWS_FILE, []);

  // Find new (unseen) reviews
  const newReviews = normalized.filter(r => !seenIds.has(r.reviewId));

  // Update seen IDs with ALL returned reviews
  normalized.forEach(r => seenIds.add(r.reviewId));

  // Add new reviews to cumulative archive
  let addedCount = 0;
  for (const r of newReviews) {
    const exists = allReviews.some(a => a.reviewId === r.reviewId);
    if (!exists) {
      r.archivedAt = new Date().toISOString();
      allReviews.push(r);
      addedCount++;
    }
  }

  // Save files
  writeJSON(SEEN_FILE, [...seenIds]);
  writeJSON(ALL_REVIEWS_FILE, allReviews);

  if (newReviews.length > 0) {
    writeJSON(NEW_REVIEWS_FILE, newReviews);
    console.log(`\n✅ ${newReviews.length} new review(s) found and saved!`);
    newReviews.forEach(r => {
      console.log(`\n  👤 ${r.name} (${r.rating}⭐)`);
      console.log(`     "${(r.text || '').slice(0, 200)}"`);
      console.log(`     🕐 ${r.time}`);
    });
  } else {
    console.log(`\n📭 No new reviews. (${seenIds.size} total seen IDs)`);
  }

  if (addedCount > 0) {
    console.log(`\n💾 ${addedCount} new review(s) added to cumulative archive (${allReviews.length} total).`);
  }
}

async function cmdDraft() {
  console.log('✍️  Generating brand-voice draft replies...\n');

  const newReviews = readJSON(NEW_REVIEWS_FILE, []);

  if (!newReviews || newReviews.length === 0) {
    console.log('📭 No new reviews to draft. Run `fetch` first.');
    return;
  }

  let pendingDrafts = readJSON(DRAFTS_FILE, []);

  for (const review of newReviews) {
    const exists = pendingDrafts.some(d => d.reviewId === review.reviewId);
    if (!exists) {
      const draft = {
        reviewId: review.reviewId,
        name: review.name,
        rating: review.rating,
        reviewText: review.text || '',
        time: review.time || '',
        draftReply: generateDraftReply(review),
      };
      pendingDrafts.push(draft);
      console.log(`  ✅ Draft generated for ${review.name}`);
    } else {
      console.log(`  ⏭  Draft already exists for ${review.name}`);
    }
  }

  writeJSON(DRAFTS_FILE, pendingDrafts);

  console.log(`\n📝 ${pendingDrafts.length} pending draft(s) ready.`);
  console.log('   Run `node tools/review-manager.mjs show` to view them.');
}

function cmdShow() {
  console.log('📊 Review Manager — Current State\n');

  const allReviews = readJSON(ALL_REVIEWS_FILE, []);
  const seenIds = readJSON(SEEN_FILE, []);
  const pendingDrafts = readJSON(DRAFTS_FILE, []);
  const repliedIds = new Set(readJSON(REPLIED_FILE, []));
  const newReviews = readJSON(NEW_REVIEWS_FILE, []);

  const totalSeen = seenIds.length;
  const repliedCount = repliedIds.size;
  const awaitingReply = allReviews.filter(r => !repliedIds.has(r.reviewId));
  const draftCount = pendingDrafts.length;

  console.log(`🏪 Alpha Tours Rome — Google Reviews`);
  console.log(`⭐ Rating: 5.0 / 5.0`);
  console.log('');
  console.log(`📚 Cumulative archive: ${allReviews.length} reviews`);
  console.log(`👁  Seen IDs tracked:  ${totalSeen}`);
  console.log(`✅ Replied:           ${repliedCount}`);
  console.log(`❌ Awaiting reply:    ${awaitingReply.length}`);
  console.log('');
  console.log(`📝 Pending drafts:    ${draftCount}`);
  console.log(`🆕 New reviews:       ${newReviews.length}`);

  if (pendingDrafts.length > 0) {
    console.log('\n─── PENDING DRAFTS ───\n');
    pendingDrafts.forEach((d, i) => {
      console.log(`[${i + 1}] ${d.name} (${d.rating}⭐)`);
      console.log(`    Review: "${(d.reviewText || '').slice(0, 150)}"`);
      console.log(`    Draft:  "${d.draftReply}"`);
      console.log('');
    });
    console.log('📋 Copy the draft replies above and paste them into business.google.com');
  }

  if (newReviews.length > 0) {
    console.log('\n─── NEW REVIEWS (not yet drafted) ───\n');
    newReviews.forEach((r, i) => {
      console.log(`[${i + 1}] ${r.name} (${r.rating}⭐): "${(r.text || '').slice(0, 150)}"`);
    });
  }
}

function cmdList() {
  console.log('📚 ALL Reviews — Cumulative Archive\n');

  const allReviews = readJSON(ALL_REVIEWS_FILE, []);
  const repliedIds = new Set(readJSON(REPLIED_FILE, []));

  if (allReviews.length === 0) {
    console.log('No reviews in archive yet. Run `fetch` first.');
    return;
  }

  console.log(`🏪 Alpha Tours Rome — ${allReviews.length} reviews total\n`);

  allReviews.forEach((r, i) => {
    const isReplied = repliedIds.has(r.reviewId);
    const status = isReplied ? '✅' : '❌';
    const ratingStars = '⭐'.repeat(r.rating);
    console.log(`${status} [${i + 1}] ${r.name} — ${ratingStars} (${r.rating}/5)`);
    console.log(`   "${(r.text || '').slice(0, 200)}"`);
    console.log(`   🕐 ${r.time || 'N/A'}`);
    console.log('');
  });

  const replied = allReviews.filter(r => repliedIds.has(r.reviewId)).length;
  const awaiting = allReviews.length - replied;
  console.log(`✅ Replied: ${replied}  ·  ❌ Awaiting reply: ${awaiting}`);
}

function cmdApprove() {
  console.log('✅ Approving pending drafts...\n');

  const pendingDrafts = readJSON(DRAFTS_FILE, []);
  const repliedIds = new Set(readJSON(REPLIED_FILE, []));

  if (pendingDrafts.length === 0) {
    console.log('📭 No pending drafts to approve.');
    return;
  }

  console.log(`📝 ${pendingDrafts.length} draft(s) to approve:\n`);

  pendingDrafts.forEach((d, i) => {
    console.log(`[${i + 1}] ${d.name} (${d.rating}⭐)`);
    console.log(`    Reply: "${d.draftReply}"`);
    console.log('');
  });

  console.log('📋 Copy each draft reply above and paste into business.google.com.');
  console.log('   After posting, run: node tools/review-manager.mjs replied --all\n');

  // Mark drafts as approved (add to replied)
  pendingDrafts.forEach(d => {
    if (d.reviewId) repliedIds.add(d.reviewId);
  });

  writeJSON(REPLIED_FILE, [...repliedIds]);
  writeJSON(DRAFTS_FILE, []);

  console.log(`✅ ${pendingDrafts.length} review(s) marked as replied.`);
  console.log('   (Make sure you actually posted them on business.google.com first!)');
}

function cmdReplied(args) {
  if (args.length === 0) {
    console.log('Usage: node tools/review-manager.mjs replied <id|--all>');
    console.log('  --all    Mark all unreplied reviews as replied');
    console.log('  <id>     Mark a specific review ID as replied');
    return;
  }

  const allReviews = readJSON(ALL_REVIEWS_FILE, []);
  const repliedIds = new Set(readJSON(REPLIED_FILE, []));
  let count = 0;

  if (args[0] === '--all') {
    allReviews.forEach(r => {
      if (!repliedIds.has(r.reviewId)) {
        repliedIds.add(r.reviewId);
        count++;
      }
    });
    console.log(`✅ ${count} review(s) marked as replied.`);
  } else {
    args.forEach(id => {
      if (!repliedIds.has(id)) {
        repliedIds.add(id);
        count++;
      }
    });
    console.log(`✅ ${count} review(s) marked as replied.`);
  }

  writeJSON(REPLIED_FILE, [...repliedIds]);

  const total = repliedIds.size;
  const unreplied = allReviews.filter(r => !repliedIds.has(r.reviewId)).length;
  console.log(`📊 Total replied: ${total}  ·  Still awaiting: ${unreplied}`);
}

function cmdHelp() {
  console.log(`
📋 Review Manager — Commands

  node tools/review-manager.mjs fetch       Fetch latest reviews from Google
  node tools/review-manager.mjs draft       Generate brand-voice draft replies
  node tools/review-manager.mjs show        Show current state (seen, new, drafts, archive)
  node tools/review-manager.mjs list        Show ALL reviews in cumulative archive
  node tools/review-manager.mjs approve     Mark drafts as approved, output for copying
  node tools/review-manager.mjs replied --all  Mark all reviews as replied (after posting)
  node tools/review-manager.mjs replied <id>   Mark specific review as replied
`);
}

// ── Main ───────────────────────────────────────────────────────────────────────

async function main() {
  const command = process.argv[2] || 'help';

  switch (command) {
    case 'fetch':
      await cmdFetch();
      break;
    case 'draft':
      await cmdDraft();
      break;
    case 'show':
      cmdShow();
      break;
    case 'list':
      cmdList();
      break;
    case 'approve':
      cmdApprove();
      break;
    case 'replied':
      cmdReplied(process.argv.slice(3));
      break;
    case 'help':
    default:
      cmdHelp();
      break;
  }
}

main().catch(e => {
  console.error(`\n❌ Fatal error: ${e.message}`);
  process.exit(1);
});
