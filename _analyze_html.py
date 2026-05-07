"""Analyze the scraped Google page HTML to find review selectors."""
from pathlib import Path
import re

# Find the saved HTML
html_dir = Path('c:/Users/pierf/AlphaTours-Project/tools')
html_files = list(html_dir.glob('page-*.html'))
if not html_files:
    print("No HTML files found")
    exit(1)

html_path = max(html_files, key=lambda p: p.stat().st_mtime)
print(f"Analyzing: {html_path}")
html = html_path.read_text(encoding='utf-8', errors='replace')

# Check for redirects / actual page content
print(f"\n--- Page info ---")
print(f"Size: {len(html)} bytes")
print(f"Title: {html.split('<title>')[1].split('</title>')[0] if '<title>' in html else 'N/A'}")

# Check if we got actual Google search results page
if 'kgmid' in html:
    print("✅ Has kgmid reference")

# Look for review-related data
print(f"\n--- Review-related patterns ---")
patterns = [
    ('review', r'[Rr]eview[s]?'),
    ('rating', r'[Rr]ating'),
    ('5 star', r'\d[- ]?star'),
    ('★', r'★'),
    ('Alpha Tours', r'Alpha\s*Tours'),
    ('business name', r'"name"\s*:'),
    ('starRating', r'starRating|star_rating|star rating'),
    ('g-t2o', r'g-t2o'),  # common Google review attribute
    ('data-reviewid', r'data-review-id|data-reviewid|reviewId'),
]

for label, pat in patterns:
    matches = re.findall(pat, html)
    print(f"  {label}: {len(matches)} matches")

# Show segments around "Alpha Tours" 
print(f"\n--- Alpha Tours mentions ---")
for m in re.finditer(r'.{100}(Alpha\s*Tours).{100}', html, re.IGNORECASE):
    ctx = m.group().replace('\n', ' ').replace('\r', '')
    print(f"...{ctx}...\n")

# Look for JSON-LD or structured data that might contain rating info
print(f"\n--- JSON-LD / structured data ---")
for m in re.finditer(r'<script[^>]*type="?application/ld\+json"?[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE):
    print(f"Found JSON-LD: {m.group(1)[:500]}")

# Check for popular CSS class patterns
print(f"\n--- Common Google class patterns ---")
class_patterns = [
    'jft14e', 'TSUbDb', 'A503be', 'w8YwRe', 'Myened', 'Jtu6Td',
    'dehysf', 'Qv1W1c', 'pi8zve', 'gy9vPe', 'D4rYp', 'review-card',
    'gws-localreviews', 'g-t2o', 'lP8Pdb', 'k1b9Kc', 'iXB6fe',
    'RfPPB', 'S4QrRc', 'M7eMe', 'BHMmbe', 'r-iBZm3a2',
    # Newer Google patterns
    'gwi0Yb', 'g4jT3d', 'KgLgD', 'uE1Jud', 'RfnDt', 'V1YFke',
    'HlGPGe', 'Sk0xKd', 'kLih7b', 'kQ1HIb', 'rWPxGd', 'A6x14e',
    'wDYxhc', 'xmB1Kb', 'E3BvAb', 'hCLkVc', 'bVj5Zb', 'ukVXfb',
    'lP8Pdb', 'iK3uPb', 'YhemCb', 'i8sZGe', 'k8Lt0', 'S1uJw',
    'p8QaT', 'p7kIoc', 'V0Dl8', 'vMhqMd', 'Q4pNd', 'Ggsf9d',
    'xPXDC', 'XzRcP', 'TSO0dd', 'ObM8ue', 'BKdL2d', 'bVj5Zb',
]

for cp in class_patterns:
    count = html.count(cp)
    if count > 0:
        print(f"  .{cp}: {count} occurrences")

# Show page structure - first div roles and key sections
print(f"\n--- Page structure (first 2000 chars) ---")
# Remove scripts and styles for cleaner view
cleaned = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
cleaned = re.sub(r'<style[^>]*>.*?</style>', '', cleaned, flags=re.DOTALL)
print(cleaned[:2000])
