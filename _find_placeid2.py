import json, urllib.request, urllib.parse

KEY = 'AIzaSyDwXwrQVFKm9Uy5-uAw2yWKier3-l8Fz-M'

# Try searching with various queries
queries = [
    'alphatoursrome',
    'Alpha Tours Rome Circo Massimo',
    'Alpha Tours Rome +39 375 829 7864',
    'Alpha Tours Rome golf cart tour guide',
]

for q in queries:
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + urllib.parse.quote(q) + '&key=' + KEY
    try:
        d = json.loads(urllib.request.urlopen(url).read())
        print(f"[{d.get('status')}] \"{q}\" -> {len(d.get('results',[]))} results")
        for r in d.get('results', [])[:3]:
            print(f"    {r.get('place_id')} - {r.get('name')[:80]}")
    except Exception as e:
        print(f"[ERR] \"{q}\" -> {e}")

# Check old Place ID
print('\n=== Check old PlaceID: ChIJHcAuWLqLJRMR-nD81t9OlAk ===')
url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJHcAuWLqLJRMR-nD81t9OlAk&fields=name,status&key=' + KEY
try:
    d = json.loads(urllib.request.urlopen(url).read())
    print(f"  Status: {d.get('status')}")
    if d.get('status') == 'OK':
        print(f"  Name: {d['result']['name']}")
    else:
        print(f"  Error: {d.get('error_message','')}")
except Exception as e:
    print(f"  Exception: {e}")

# Try surrounding search near Circo Massimo
print('\n=== Nearby Circo Massimo - search for tour operators ===')
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=41.8833,12.4871&radius=500&keyword=tour&key=' + KEY
try:
    d = json.loads(urllib.request.urlopen(url).read())
    print(f"  Status: {d.get('status')} -> {len(d.get('results',[]))} results")
    for r in d.get('results', [])[:10]:
        print(f"    {r.get('place_id')} - {r.get('name')} - {r.get('vicinity','')}")
except Exception as e:
    print(f"  Exception: {e}")

# Search by alpha tours phone (just the number without +)
print('\n=== Search by phone ===')
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=3758297864&key=' + KEY
try:
    d = json.loads(urllib.request.urlopen(url).read())
    print(f"  Status: {d.get('status')} -> {len(d.get('results',[]))} results")
    for r in d.get('results', [])[:5]:
        print(f"    {r.get('place_id')} - {r.get('name')}")
except Exception as e:
    print(f"  Exception: {e}")
