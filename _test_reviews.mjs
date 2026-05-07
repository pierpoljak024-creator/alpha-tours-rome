/**
 * _test_reviews.mjs — Get FULL review data from NEW Places API
 * Key2 works! Let's extract all review details.
 */
import https from 'https';

const API_KEY = 'AIzaSyBp0MQ_nXd6zhs6z9CU172Ua7q5FSzfBIg';
const PLACE_ID = 'ChIJHcAuWLqLJRMR-nD81t9OlAk';

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
        catch(e) { reject(new Error('Parse error: ' + e.message)); }
      });
    });
    req.on('error', reject);
    req.on('timeout', function() { this.destroy(); reject(new Error('Timeout')); });
    req.end();
  });
}

async function main() {
  console.log('=== Fetching FULL review data from NEW Places API ===\n');
  
  const result = await httpsGet(`https://places.googleapis.com/v1/places/${PLACE_ID}`);
  
  if (result.error) {
    console.log(`❌ Error: ${result.error.message}`);
    console.log(JSON.stringify(result, null, 2));
    return;
  }
  
  console.log(`🏪 ${result.displayName?.text || result.id}`);
  console.log(`⭐ Rating: ${result.rating} / 5`);
  console.log(`📊 Total reviews: ${result.userRatingCount}`);
  
  const reviews = result.reviews || [];
  console.log(`\n📝 Reviews returned: ${reviews.length}`);
  
  reviews.forEach((r, i) => {
    console.log(`\n  [${i + 1}] Review:`);
    console.log(`      name: ${r.name}`);
    console.log(`      relativePublishTimeDescription: ${r.relativePublishTimeDescription}`);
    console.log(`      rating: ${r.rating}`);
    
    // Get the text
    if (r.originalText?.text) {
      console.log(`      originalText.text: "${r.originalText.text.slice(0, 300)}"`);
    }
    if (r.text?.text) {
      console.log(`      text.text: "${r.text.text.slice(0, 300)}"`);
    }
    
    // Author
    if (r.authorAttribution) {
      console.log(`      author: ${r.authorAttribution.displayName} (${r.authorAttribution.uri})`);
      console.log(`      photoUri: ${r.authorAttribution.photoUri}`);
    }
    
    // Review ID (extract from name)
    console.log(`      reviewId (from name): ${r.name?.split('/').pop()}`);
  });
  
  if (reviews.length === 0) {
    console.log('\n  No reviews in response. Full response:');
    console.log(JSON.stringify(result, null, 2).slice(0, 2000));
  }
}

main().catch(e => console.error('Fatal:', e.message));
