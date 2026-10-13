import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

idx = txt.find('id:"fx-view"')
if idx != -1:
    print("=== App View Condition Context ===")
    print(txt[max(0, idx-1000):min(len(txt), idx+200)])
