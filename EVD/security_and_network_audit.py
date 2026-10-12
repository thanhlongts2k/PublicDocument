import requests
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
print("=== SECURITY & NETWORK AUDIT FOR FINLUX WEB ===")

# 1. Test Latency
latencies = []
for i in range(5):
    t0 = time.time()
    r = requests.get(base + '/api/health')
    latencies.append((time.time() - t0) * 1000)

avg_lat = sum(latencies) / len(latencies)
print(f"\n1. API Latency (/api/health):")
print(f"   - Min: {min(latencies):.1f}ms | Max: {max(latencies):.1f}ms | Avg: {avg_lat:.1f}ms")

# 2. Security Headers Audit
r_home = requests.get(base)
headers = r_home.headers
print("\n2. HTTP Security Headers Audit:")
sec_headers = {
    'Strict-Transport-Security': 'HSTS',
    'Content-Security-Policy': 'CSP',
    'X-Frame-Options': 'Clickjacking protection',
    'X-Content-Type-Options': 'MIME-sniffing protection',
    'Referrer-Policy': 'Referrer leakage protection',
    'Permissions-Policy': 'Browser features restriction'
}

for h, desc in sec_headers.items():
    val = headers.get(h)
    if val:
        print(f"   [PASS] {h}: {val}")
    else:
        print(f"   [FAIL - MISSING] {h} ({desc})")

print(f"\n   Server Info: {headers.get('Server', 'Not disclosed')}")
print(f"   Cloudflare Ray: {headers.get('CF-RAY', 'None')}")

# 3. Missing SEO / Meta Files
print("\n3. Public SEO / System Files:")
for path in ['/robots.txt', '/sitemap.xml', '/manifest.json', '/favicon.ico', '/finlux_logo.png']:
    res = requests.get(base + path)
    status_str = f"Status {res.status_code}"
    if res.status_code == 200:
        print(f"   [PASS] {path:18}: {status_str} ({len(res.content)} bytes)")
    else:
        print(f"   [FAIL] {path:18}: {status_str} (Resource missing)")

# 4. URL Param Reflected XSS / Injection Check
print("\n4. URL Parameter Injection Test (/login?mode=...):")
xss_payload = '"><script>alert(1)</script>'
r_xss = requests.get(base + f'/login?mode={xss_payload}')
if xss_payload in r_xss.text:
    print(f"   [CRITICAL] Reflected XSS vulnerability detected in /login?mode=")
else:
    print(f"   [PASS] Payload safely handled / sanitized (not reflected in raw HTML)")

# 5. Invalid Route 404 Handling
print("\n5. 404 Error Page Handling:")
r_404 = requests.get(base + '/non-existent-route-999')
print(f"   Status Code: {r_404.status_code}")
if '404' in r_404.text:
    print("   [PASS] Returns standard 404 status and page")
else:
    print("   [FAIL] Did not return 404 page")
