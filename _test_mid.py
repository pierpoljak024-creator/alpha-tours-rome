"""Test Google MID g:11nb78xf_8 for Alpha Tours Rome."""
import json, urllib.request, urllib.parse

KEY = 'AIzaSyDwXwrQVFKm9Uy5-uAw2yWKier3-l8Fz-M'
MID = 'g:11nb78xf_8'

# Try the MID as a Place ID
print('=== MID as Place ID ===')
url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={MID}&fields=name,rating,user_ratings_total,reviews,formatted_address,website,international_phone_number&reviews_sort=newest&key={KEY}'
try:
    d = json.loads(urllib.request.urlopen(url).read())
    print(f'Status: {d.get("status")}')
    if d.get('status') == 'OK':
        r = d['result']
        print(f'Name: {r.get("name")}')
        print(f'Address: {r.get("formatted_address")}')
        print(f'Website: {r.get("website")}')
        print(f'Phone: {r.get("international_phone_number")}')
        print(f'Rating: {r.get("rating")}')
        print(f'Total ratings: {r.get("user_ratings_total")}')
        reviews = r.get('reviews', [])
        print(f'Reviews returned: {len(reviews)}')
        for rev in reviews[:5]:
            print(f'  - {rev.get("author_name")} ({rev.get("rating")}★): {rev.get("text","")[:80]}...')
    else:
        print(f'Error: {d.get("error_message","")}')
except Exception as e:
    print(f'Exception: {e}')

# Also try with the google prefix
print('\n=== Full place_id format ===')
url2 = f'https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJHcAuWLqLJRMR-nD81t9OlAk&fields=name,status&key={KEY}'
try:
    d2 = json.loads(urllib.request.urlopen(url2).read())
    print(f'Old PlaceID: Status={d2.get("status")}')
except Exception as e:
    print(f'Exception: {e}')
