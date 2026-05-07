"""Deep analysis of Google Knowledge Panel HTML for review data extraction."""
from pathlib import Path
import re
import json

html_path = Path('c:/Users/pierf/AlphaTours-Project/tools/google-page.html')
if not html_path.exists():
    print("❌ google-page.html not found!")
    exit(1)

html = html_path.read_text(encoding='utf-8', errors='replace')
print(f"📄 Size: {len(html):,} bytes\n")

# 1. JSON-LD structured data
print("=" * 60)
print("1️⃣ JSON-LD BLOCKS")
print("=" * 60)
jsonld = re.findall(r'<script[^>]*type="?application/ld\+json"?[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
print(f"   Found: {len(jsonld)}")
for i, j in enumerate(jsonld[:5]):
    print(f"\n   --- JSON-LD #{i+1} ({len(j)} chars) ---")
    try:
        data = json.loads(j.strip())
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, (str, int, float)):
                    print(f"   {k}: {v}")
                elif k == 'aggregateRating':
                    print(f"   aggregateRating: {json.dumps(v, indent=4)[:200]}")
                elif k == 'review':
                    print(f"   review: {len(v)} items")
                else:
                    print(f"   {k}: {type(v).__name__}")
    except json.JSONDecodeError as e:
        print(f"   ❌ JSON parse error: {e}")

# 2. Search for reviewId pattern (most reliable Google review identifier)
print("\n" + "=" * 60)
print("2️⃣ REVIEW ID PATTERNS")
print("=" * 60)
review_ids = re.findall(r'data-review[id][= ][\'"]?([^\'"&\s>]+)', html)
print(f"   data-reviewid: {len(review_ids)} found")
if review_ids:
    for rid in review_ids[:10]:
        print(f"   → {rid}")

# Also check for JSON inside scripts
review_ids_json = re.findall(r'"reviewId"\s*:\s*"([^"]+)"', html)
print(f"   \"reviewId\" in JSON: {len(review_ids_json)} found")
if review_ids_json:
    for rid in review_ids_json[:5]:
        print(f"   → {rid}")

# 3. Star rating patterns
print("\n" + "=" * 60)
print("3️⃣ STAR RATING PATTERNS")
print("=" * 60)
star_ratings = re.findall(r'"starRating"\s*:\s*(\d+)', html)
print(f"   \"starRating\" in JSON: {len(star_ratings)} found")
if star_ratings:
    for s in star_ratings[:10]:
        print(f"   → {int(s)/10:.1f} stars")

# 4. Display names (reviewer names)
print("\n" + "=" * 60)
print("4️⃣ DISPLAY NAMES")
print("=" * 60)
names = re.findall(r'"displayName"\s*:\s*"([^"]+)"', html)
print(f"   \"displayName\" in JSON: {len(names)} found")
if names:
    for n in names[:10]:
        print(f"   → {n}")

# 5. Original review text
print("\n" + "=" * 60)
print("5️⃣ REVIEW TEXT (originalText)")
print("=" * 60)
texts = re.findall(r'"originalText"\s*:\s*"([^"]+)"', html)
print(f"   \"originalText\" in JSON: {len(texts)} found")
if texts:
    for t in texts[:5]:
        print(f"   → {t[:100]}...")
# Also with escaped unicode
texts2 = re.findall(r'"text"\s*:\s*"([^"]+)"', html)
print(f"   \"text\" in JSON: {len(texts2)} found (includes non-review ones)")

# 6. Try to find the full review JSON block
print("\n" + "=" * 60)
print("6️⃣ FULL REVIEW JSON BLOCKS")
print("=" * 60)
# Look for objects that contain reviewId, starRating, and displayName
blocks = re.findall(r'\{[^{}]*"reviewId"[^{}]*"starRating"[^{}]*"displayName"[^{}]*\}', html)
print(f"   Pattern reviewId+starRating+displayName: {len(blocks)}")
if blocks:
    for i, b in enumerate(blocks[:3]):
        try:
            data = json.loads(b)
            print(f"\n   --- Block #{i+1} ---")
            print(f"   Name: {data.get('displayName', '?')}")
            print(f"   Rating: {int(data.get('starRating', 0))/10:.1f}")
            print(f"   Text: {data.get('originalText', data.get('text', 'N/A'))[:100]}")
            print(f"   Time: {data.get('createTime', data.get('relativeTime', 'N/A'))}")
        except:
            print(f"   → (parse error, raw: {b[:150]}...)")

# 7. Check for any Google reviews API endpoint in page
print("\n" + "=" * 60)
print("7️⃣ API ENDPOINTS / GRAPHQL")
print("=" * 60)
apis = re.findall(r'https?://[^"\']*(?:review|business)[^"\']*', html)
print(f"   Review-related URLs: {len(apis)}")
if apis:
    for a in apis[:5]:
        print(f"   → {a[:150]}")

# 8. Check aggregate rating
print("\n" + "=" * 60)
print("8️⃣ AGGREGATE RATING")
print("=" * 60)
ar = re.findall(r'"aggregateRating"\s*:\s*(\{[^}]+\})', html)
if ar:
    print(f"   Found: {ar[0][:200]}")
else:
    print("   Not found in simple form, checking nested...")
    ar2 = re.findall(r'"aggregateRating".{0,200}', html)
    if ar2:
        for a in ar2[:3]:
            print(f"   → {a[:200]}")

# 9. Full page structure analysis - key data
print("\n" + "=" * 60)
print("9️⃣ KEY DATA SUMMARY")
print("=" * 60)
data_points = {
    'data-reviewid ATTRS': len(review_ids),
    'reviewId in JSON': len(review_ids_json),
    'starRating values': len(star_ratings),
    'displayName values': len(names),
    'originalText values': len(texts),
    'JSON-LD blocks': len(jsonld),
}
for k, v in data_points.items():
    print(f"   {k}: {v}")
