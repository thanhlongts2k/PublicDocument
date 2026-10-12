import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
res = requests.get(base)
chunks = list(set(re.findall(r'src=["\'](/_next/static/chunks/[^"\']+)["\']', res.text)))
login_res = requests.get(base + '/login')
login_chunks = list(set(re.findall(r'src=["\'](/_next/static/chunks/[^"\']+)["\']', login_res.text)))

all_chunks = set(chunks + login_chunks)
print(f"Total unique chunks to search: {len(all_chunks)}")

for ch in all_chunks:
    txt = requests.get(base + ch).text
    if 'apiKey' in txt or 'projectId' in txt:
        print(f"\nFound Firebase keys in {ch}:")
        configs = re.findall(r'apiKey:\s*["\']([^"\']+)["\']', txt)
        projects = re.findall(r'projectId:\s*["\']([^"\']+)["\']', txt)
        authDomains = re.findall(r'authDomain:\s*["\']([^"\']+)["\']', txt)
        for c in set(configs):
            print("  apiKey:", c)
        for p in set(projects):
            print("  projectId:", p)
        for a in set(authDomains):
            print("  authDomain:", a)
