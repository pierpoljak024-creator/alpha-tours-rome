/**
 * Test Google My Business API with proper wait before first call.
 * Goal: Wait 10+ minutes with NO API calls, then try once.
 * 
 * Run: node _test_clean.mjs
 */
import https from 'https';

const CREDS = {
  client_id: "723098435736-hb10eius0c5rform1j56b1bu81tjb13f.apps.googleusercontent.com",
  client_secret: "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",
  refresh_token: "1//096WoECPUC0v5CgYIARAAGAkSNwF-L9Ir7d7_gstTSuEvDMWSXgGvWkZ8M__UYMMhBDXy5T8VyiO5x7RW2B3_wuYDsTh436QAmC0",
};

async function main() {
  console.log("⏳ Waiting 10 minutes with ZERO API calls to reset rate limit...");
  console.log(`   Started at: ${new Date().toLocaleTimeString()}`);
  
  await new Promise(r => setTimeout(r, 10 * 60 * 1000)); // 10 min wait
  
  console.log(`   Resuming at: ${new Date().toLocaleTimeString()}`);
  console.log("🔐 Getting access token...");
  
  // Step 1: Get token
  const token = await new Promise((resolve, reject) => {
    const body = new URLSearchParams({
      client_id: CREDS.client_id, client_secret: CREDS.client_secret,
      refresh_token: CREDS.refresh_token, grant_type: 'refresh_token',
    }).toString();
    const req = https.request("https://oauth2.googleapis.com/token", {
      method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    }, res => {
      let data = ""; res.on("data", c => data += c);
      res.on("end", () => {
        const j = JSON.parse(data);
        if (j.error) reject(new Error(`OAuth: ${j.error}`));
        else resolve(j.access_token);
      });
    });
    req.on("error", reject);
    req.write(body); req.end();
  });
  console.log("✅ Token obtained.");

  // Step 2: Make ONE single call to accounts API
  console.log("\n📋 Fetching accounts (1 attempt only)...");
  try {
    const accts = await new Promise((resolve, reject) => {
      const req = https.get("https://mybusinessaccountmanagement.googleapis.com/v1/accounts", {
        headers: { Authorization: `Bearer ${token}` }
      }, res => {
        let data = "";
        res.on("data", c => data += c);
        res.on("end", () => {
          if (res.statusCode === 429) reject(new Error(`429: ${data.slice(0, 200)}`));
          else if (res.statusCode >= 400) reject(new Error(`HTTP ${res.statusCode}: ${data.slice(0, 200)}`));
          else resolve(JSON.parse(data));
        });
      });
      req.on("error", reject);
      req.end();
    });
    
    const accounts = accts.accounts || [];
    console.log(`✅ Accounts found: ${accounts.length}`);
    
    if (accounts.length === 0) {
      console.log("   Raw response:", JSON.stringify(accts).slice(0, 300));
      return;
    }
    
    for (const a of accounts) {
      console.log(`   Account: ${a.name} (${a.accountName})`);
    }
    
    // Step 3: Get locations for the first account
    const accountName = accounts[0].name;
    console.log(`\n📋 Fetching locations for ${accountName}...`);
    
    try {
      const locs = await new Promise((resolve, reject) => {
        const req = https.get(`https://mybusinessbusinessinformation.googleapis.com/v1/${accountName}/locations`, {
          headers: { Authorization: `Bearer ${token}` }
        }, res => {
          let data = "";
          res.on("data", c => data += c);
          res.on("end", () => {
            if (res.statusCode >= 400) reject(new Error(`HTTP ${res.statusCode}: ${data.slice(0, 200)}`));
            else resolve(JSON.parse(data));
          });
        });
        req.on("error", reject);
        req.end();
      });
      
      const locations = locs.locations || [];
      console.log(`✅ Locations found: ${locations.length}`);
      
      for (const l of locations) {
        console.log(`   Location: ${l.name} — ${l.title || l.locationName || "?"}`);
      }
      
      // Step 4: Get reviews for first location
      if (locations.length > 0) {
        const locName = locations[0].name;
        console.log(`\n📋 Fetching reviews for ${locName}...`);
        
        try {
          const reviews = await new Promise((resolve, reject) => {
            const req = https.get(`https://mybusiness.googleapis.com/v4/${locName}/reviews`, {
              headers: { Authorization: `Bearer ${token}` }
            }, res => {
              let data = "";
              res.on("data", c => data += c);
              res.on("end", () => {
                if (res.statusCode >= 400) reject(new Error(`HTTP ${res.statusCode}: ${data.slice(0, 200)}`));
                else resolve(JSON.parse(data));
              });
            });
            req.on("error", reject);
            req.end();
          });
          
          const reviewList = reviews.reviews || [];
          console.log(`✅ ${reviewList.length} reviews found!`);
          
          for (const r of reviewList.slice(0, 10)) {
            const name = r.reviewer?.displayName || "?";
            const stars = r.starRating || 5;
            const text = (r.comment || "").slice(0, 120);
            const time = r.createTime || "";
            console.log(`   ${name} (${stars}★) [${time.slice(0, 10)}]: ${text}`);
          }
          
          // Save to file for review-fetcher
          const { writeFileSync } = await import('fs');
          const { join, dirname } = await import('path');
          const { fileURLToPath } = await import('url');
          
          const result = { accountName, locationName: locName, accountId: accountName.split("/")[1], locationId: locName.split("/")[3] };
          writeFileSync(join(dirname(fileURLToPath(import.meta.url)), "tools", "cache.json"), JSON.stringify(result));
          console.log(`\n💾 Cached: accountId=${result.accountId}, locationId=${result.locationId}`);
          
          const seenFile = join(dirname(fileURLToPath(import.meta.url)), "tools", "seen-reviews.json");
          const seenIds = reviewList.map(r => r.reviewId).filter(Boolean);
          writeFileSync(seenFile, JSON.stringify(seenIds));
          console.log(`💾 Saved ${seenIds.length} review IDs to seen-reviews.json`);
          
        } catch (err) {
          console.log(`❌ Reviews error: ${err.message}`);
        }
      }
    } catch (err) {
      console.log(`❌ Locations error: ${err.message}`);
    }
  } catch (err) {
    console.log(`❌ Accounts error: ${err.message}`);
  }
}

main().catch(err => console.error(`Fatal: ${err.message}`));
