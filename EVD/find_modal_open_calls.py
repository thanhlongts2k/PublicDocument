import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

# find where state variable `h` is declared: let [h, ...] = (0, o.useState)(!1) or similar
matches = re.finditer(r'([a-zA-Z0-9_$]+)\s*\(\s*!0\s*\)', txt)
for m in matches:
    start = max(0, m.start() - 200)
    end = min(len(txt), m.end() + 200)
    print("--- Setter call ---")
    print(txt[start:end])
