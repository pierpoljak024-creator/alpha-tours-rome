/**
 * _test_places_api.mjs — Test ALL Google API keys
 */
import https from 'https';

const KEYS = {
  key1: 'AIzaSyDwXwrQVFKm9Uy5-uAw2yWKier3-l8Fz-M',  // from review-config.json
  key2: 'AIzaSyBp0MQ_nXd6zhs6z9CU172Ua7q5FSzfBIg',  // from test_new_places_api.py
};
const PLACE_ID = 'ChIJHcAuWLqLJRMR-nD81t9OlAk';

function httpsGet(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { timeout: 15000 }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch(e) { reject(new Error('Parse error: ' + e.message)); }
      });
    }).on('error', reject).on('timeout', function() { this.destroy(); reject(new Error('Timeout')); });
  });
}

async function testKey(name, apiKey) {
  console.log(`\n=== Testing API Key: ${name} ===`);
  
  // Test: text search
  const searchUrl = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=Alpha+Tours+Rome&key=${apiKey}`;
  const searchResult = await httpsGet(searchUrl);
  console.log(`  Text Search: ${searchResult.status}`);
  if (searchResult.status === 'OK') {
    const place = searchResult.results[0];
    console.log(`  Found: ${place.name}, Place ID: ${place.place_id}, Rating: ${place.rating || 'N/A'}`);
    
    // Place Details
    const detailsUrl = `https://maps.googleapis.com/maps/api/place/details/json?place_id=${place.place_id}&fields=name,rating,reviews,user_ratings_total&key=${apiKey}&reviews_no_translations=true`;
    const detailsResult = await httpsGet(detailsUrl);
    console.log(`  Details: ${detailsResult.status}`);
    if (detailsResult.status === 'OK') {
      const revs = detailsResult.result.reviews || [];
      console.log(`  Reviews: ${revs.length}`);
      revs.forEach(r => console.log(`    - ${r.author_name}: ${r.rating}⭐ "${(r.text||'').slice(0,80)}"`));
    }
    return { name, works: true, reviews: detailsResult.result?.reviews || [] };
  } else if (searchResult.status === 'ZERO_RESULTS') {
    // Try direct Place ID lookup
    const directUrl = `https://maps.googleapis.com/maps/api/place/details/json?place_id=${PLACE_ID}&fields=name,rating,reviews,user_ratings_total&key=${apiKey}`;
    const directResult = await httpsGet(directUrl);
    console.log(`  Direct Place ID: ${directResult.status}`);
    if (directResult.status === 'OK') {
      const revs = directResult.result.reviews || [];
      console.log(`  Reviews: ${revs.length}`);
      revs.forEach(r => console.log(`    - ${r.author_name}: ${r.rating}⭐ "${(r.text||'').slice(0,80)}"`));
      return { name, works: true, reviews: revs };
    }
    return { name, works: false, error: 'NOT_FOUND' };
  } else {
    const err = searchResult.error_message || searchResult.status;
    console.log(`  Error: ${err}`);
    return { name, works: false, error: err };
  }
}

async function main() {
  // Try the NEW Places API (v1) with key2
  console.log('\n=== Testing NEW Places API (places.googleapis.com) ===');
  for (const [name, key] of Object.entries(KEYS)) {
    const url = 'https://places.googleapis.com/v1/places/ChIJHcAuWLqLJRMR-nD81t9OlAk';
    const headers = {
      'X-Goog-Api-Key': key,
      'X-Goog-FieldMask': 'id,displayName,rating,userRatingCount,reviews,goodForChildren,paymentOptions',
      'Content-Type': 'application/json',
      'X-Goog-Language': 'en',
    };
    try {
      const result = await new Promise((resolve, reject) => {
        const req = https.get(url, { headers, timeout: 10000 }, (res) => {
          let data = '';
          res.on('data', chunk => data += chunk);
          res.on('end', () => {
            try { resolve(JSON.parse(data)); }
            catch(e) { reject(new Error('Parse error')); }
          });
        });
        req.on('error', reject);
        req.on('timeout', function() { this.destroy(); reject(new Error('Timeout')); });
        req.end();
      });
      console.log(`  ${name}: Status =`, result.error ? result.error.message : 'OK');
      if (!result.error) {
        console.log(`  Name: ${result.displayName?.text || result.id}`);
        console.log(`  Rating: ${result.rating}`);
        console.log(`  Total reviews: ${result.userRatingCount}`);
        if (result.reviews) console.log(`  Reviews returned: ${result.reviews.length}`);
        else console.log('  No reviews field in response (needs specific fieldMask)');
      }
    } catch(e) {
      console.log(`  ${name}: ${e.message}`);
    }
  }

  // Test the old Places API
  console.log('\n=== Testing OLD Places API (maps.googleapis.com) ===');
  const results = [];
  for (const [name, key] of Object.entries(KEYS)) {
    results.push(await testKey(name, key));
  }
  
  console.log('\n=== SUMMARY ===');
  for (const r of results) {
    console.log(`  ${r.name}: ${r.works ? '✅ WORKS' : '❌ FAILED'} ${r.error || ''}`);
    if (r.reviews?.length > 0) console.log(`     → ${r.reviews.length} reviews available`);
  }
}

main().catch(e => console.error('Fatal:', e.message));
