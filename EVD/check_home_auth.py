import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
res = requests.get(base)
chunks = list(set(re.findall(r'src=["\'](/_next/static/chunks/[^"\']+)["\']', res.text)))

print("Searching for onAuthStateChanged or user profile logic in homepage chunks...")
for ch in chunks:
    txt = requests.get(base + ch).text
    if 'onAuthStateChanged' in txt or 'signOut' in txt or 'currentUser' in txt:
        print(f"Found Auth state in chunk: {ch}")
        # Find context
        for m in re.finditer(r'(onAuthStateChanged|signOut|currentUser)', txt):
            s = max(0, m.start() - 100)
            e = min(len(txt), m.end() + 300)
            print("--- Auth State snippet ---")
            print(txt[s:e])
