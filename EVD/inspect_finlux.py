import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_url = 'https://finlux-0wxc.onrender.com'
res = requests.get(base_url)
print('Homepage status:', res.status_code)

# Check common web routes
test_routes = [
    '/login', '/register', '/signup', '/auth', '/dashboard', 
    '/wallets', '/transactions', '/reports', '/budget', '/settings',
    '/api', '/api/health', '/api/auth', '/api/users', '/api/transactions',
    '/robots.txt', '/sitemap.xml', '/manifest.json', '/favicon.ico'
]

print('\nTesting common routes:')
for route in test_routes:
    try:
        r = requests.get(base_url + route, allow_redirects=False, timeout=5)
        print(f"Route {route:20}: Status {r.status_code} (Redirect: {r.headers.get('Location', 'None')})")
    except Exception as e:
        print(f"Route {route:20}: Error {e}")

js_files = list(set(re.findall(r'src=["\'](/_next/static/chunks/[^"\']+)["\']', res.text)))
print(f'\nAnalyzing {len(js_files)} JS chunks for routes & API calls...')

all_urls = set()
for js in js_files:
    content = requests.get(base_url + js).text
    # Find all path-like strings
    paths = re.findall(r'["\'](/[a-zA-Z0-9_\-\./#?=&]+)["\']', content)
    for p in paths:
        if any(keyword in p.lower() for keyword in ['/api', '/login', '/auth', '/dashboard', '/app', '/user', '/v1', '/v2', 'http']):
            all_urls.add(p)

print('\nDiscovered API / Link strings in chunks:')
for u in sorted(all_urls):
    print('  *', u)
