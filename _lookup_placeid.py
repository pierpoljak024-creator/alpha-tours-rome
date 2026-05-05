import json, urllib.request
KEY = "AIzaSyDwXwrQVFKm9Uy5-uAw2yWKier3-l8Fz-M"

# Try CID API
cid = "9944edfd6fc70fa"
url = f"https://maps.googleapis.com/maps/api/place/details/json?cid={cid}&fields=name,rating,reviews,place_id,formatted_address&key={KEY}"
d = json.loads(urllib.request.urlopen(url).read())
print(f"CID {cid}: {d.get('status')}")
if d.get("status") == "OK":
    r = d["result"]
    print(f"  Name: {r['name']}")
    print(f"  Place ID: {r['place_id']}")
    print(f"  Reviews: {len(r.get('reviews',[]))}")

# Try g: prefix
pid2 = "g:11nb78xf_8"
url2 = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={pid2}&fields=name,rating,reviews,place_id&key={KEY}"
d2 = json.loads(urllib.request.urlopen(url2).read())
print(f"\nPlace ID g:11nb78xf_8: {d2.get('status')}")

# Search near Circo Massimo (Rome center)
print("\n=== Nearby: Circo Massimo area ===")
url3 = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=41.8833,12.4871&radius=200&key={KEY}"
d3 = json.loads(urllib.request.urlopen(url3).read())
print(f"Status: {d3.get('status')}")
for r in d3.get("results",[])[:10]:
    print(f"  {r['place_id']} - {r['name']}")

# Search by phone
print("\n=== Phone search +393758297864 ===")
url4 = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=%2B393758297864&key={KEY}"
d4 = json.loads(urllib.request.urlopen(url4).read())
print(f"Status: {d4.get('status')}")
for r in d4.get("results",[])[:5]:
    print(f"  {r['place_id']} - {r['name']}")
