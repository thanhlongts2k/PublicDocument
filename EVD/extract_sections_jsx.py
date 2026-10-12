import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

# Find all occurrences of 01 /, 02 /, etc.
for i in range(1, 9):
    pattern = f'0{i} /'
    idx = txt.find(pattern)
    if idx != -1:
        print(f"\n=================== SECTION {i} ===================")
        # find surrounding text
        s = max(0, idx - 50)
        e = min(len(txt), idx + 800)
        print(txt[s:e])
