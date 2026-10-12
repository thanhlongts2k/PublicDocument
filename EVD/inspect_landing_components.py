import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
res = requests.get(base)
chunks = list(set(re.findall(r'src=["\'](/_next/static/chunks/[^"\']+)["\']', res.text)))

# inspect 3yzbl7ojrs6o5.js
for ch in chunks:
    txt = requests.get(base + ch).text
    if 'FINLUX' in txt and ('Dòng tiền FCF' in txt or 'Đa ví' in txt):
        print(f"Main landing page component chunk: {ch} ({len(txt)} bytes)")
        
        # Check all section titles, buttons, modals, tabs
        titles = re.findall(r'["\'](0[0-9]\s*/\s*[^"\']+)["\']', txt)
        print("Discovered section titles:", set(titles))
        
        # Check if there are modals / popups
        modals = [w for w in re.findall(r'["\']([^"\']*(?:modal|popup|dialog|toast)[^"\']*)["\']', txt, re.IGNORECASE) if len(w) < 40]
        print("Discovered modal/dialog keywords:", set(modals[:15]))
        
        # Check navigation anchors (#s0, #s1...)
        anchors = re.findall(r'["\'](#[a-zA-Z0-9_\-]+)["\']', txt)
        print("Discovered anchors:", set(anchors))
        
        # Check all links
        hrefs = re.findall(r'href:\s*["\']([^"\']+)["\']', txt)
        print("Discovered hrefs:", set(hrefs))
