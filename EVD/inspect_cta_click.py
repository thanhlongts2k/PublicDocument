import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

idx = txt.find('Trải nghiệm ngay')
while idx != -1:
    print("=== 'Trải nghiệm ngay' Snippet ===")
    print(txt[max(0, idx-300):min(len(txt), idx+300)])
    idx = txt.find('Trải nghiệm ngay', idx + 1)
