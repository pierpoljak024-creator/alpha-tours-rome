import json, urllib.request, urllib.parse

KEY = 'AIzaSyDwXwrQVFKm9Uy5-uAw2yWKier3-l8Fz-M'
CID = '9944edfd6fc70fa'

# Try various queries
queries = [
    'Alpha Tours Rome',
    'Alpha Tours Roma',
    'Circo Massimo tour operator',
    'alphatoursrome.com',
    'Rome golf cart tour',
    'Alpha Tours Rome Italy',
    'Roma Tour Guide golf cart',
]

for q in queries:
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + urllib.parse.quote(q) + '&key=' + KEY
    try:
        d = json.loads(urllib.request.urlopen(url).read())
        status = d.get('status', '?')
        results = d.get('results', [])
        if results:
            r = results[0]
            print(f"[{status}] '{q}' -> {r.get('place_id')} - {r.get('name')} - {r.get('formatted_address','')}")
        else:
            print(f"[{status}] '{q}' -> no results")
    except Exception as e:
        print(f"[ERR] '{q}' -> {e}")

# Try CID API (original)
print('\n=== CID lookup ===')
url_cid = 'https://maps.googleapis.com/maps/api/place/details/json?cid=' + CID + '&fields=name,place_id,formatted_address,rating&key=' + KEY
try:
    d = json.loads(urllib.request.urlopen(url_cid).read())
    print(f"CID {CID}: Status={d.get('status')}")
    if d.get('status') == 'OK':
        r = d['result']
        print(f"  {r.get('place_id')} - {r.get('name')} - {r.get('formatted_address','')} - Rating: {r.get('rating')}")
except Exception as e:
    print(f"CID error: {e}")
