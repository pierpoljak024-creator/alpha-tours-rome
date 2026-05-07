"""
Research all possible methods to fetch Google reviews for Alpha Tours Rome.
"""
import json, urllib.request, urllib.parse

KEY = 'AIzaSyDwXwrQVFKm9Uy5-uAw2yWKier3-l8Fz-M'
KGMID = '/g/11nb78xf_8'

# === METHOD 4: Knowledge Graph API ===
print("=" * 60)
print("METHOD 4: Knowledge Graph API (kgsearch.googleapis.com)")
print("=" * 60)
url = 'https://kgsearch.googleapis.com/v1/entities:search?ids=' + urllib.parse.quote(KGMID) + '&key=' + KEY + '&languages=en'
try:
    d = json.loads(urllib.request.urlopen(url).read())
    item_list = d.get('itemListElement', [])
    print(f"  Results: {len(item_list)}")
    for item in item_list[:3]:
        entity = item.get('result', {})
        print(f"  Name: {entity.get('name')}")
        print(f"  Desc: {str(entity.get('description',''))[:100]}")
        print(f"  Score: {item.get('resultScore','')}")
        dd = entity.get('detailedDescription', {})
        if dd:
            print(f"  URL: {dd.get('url','')}")
        print()
except Exception as e:
    print(f"  Error: {e}\n")

# === METHOD 9: Place Autocomplete ===
print("=" * 60)
print("METHOD 9: Place Autocomplete (find Place ID)")
print("=" * 60)
url = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Alpha+Tours+Rome&types=establishment&key=' + KEY
try:
    d = json.loads(urllib.request.urlopen(url).read())
    print(f"  Status: {d.get('status')}")
    predictions = d.get('predictions', [])
    print(f"  Predictions: {len(predictions)}")
    for p in predictions[:5]:
        print(f"  - {p.get('description')} -> {p.get('place_id')}")
except Exception as e:
    print(f"  Error: {e}")

print()
print("=" * 60)
print("SUMMARY - Best approaches:")
print("=" * 60)
print("""
1. My Business API OAuth - wait 3min, cache account+location
2. Puppeteer scrape - kgmid URL, extract reviews from DOM
3. googleLocations:search - POST camelCase format
""")
