import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

# Find where fx-modal or fx-modal-overlay is used
idx = txt.find('fx-modal-overlay')
if idx != -1:
    print("=== Modal Definition Snippet ===")
    print(txt[max(0, idx-500):min(len(txt), idx+1500)])

# Find state that opens the modal
matches = re.findall(r'(\b[a-zA-Z0-9_$]+\b\s*\(\s*!0\s*\)|\bset[a-zA-Z0-9_$]*Modal\b|\bsetShow[a-zA-Z0-9_$]*\b)', txt)
print("\nModal open state triggers:")
for m in matches[:10]:
    print(" ", m)
