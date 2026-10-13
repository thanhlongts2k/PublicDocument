import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
res = requests.get(base + '/login')
chunks = list(set(re.findall(r'src=["\'](/_next/static/chunks/[^"\']+)["\']', res.text)))

found_chunk = None
for ch in chunks:
    txt = requests.get(base + ch).text
    if 'Đăng nhập FinLux' in txt or 'Email tài khoản' in txt:
        found_chunk = ch
        print(f"Found login component in chunk: {ch}")
        
        # Search for input, button, onClick, onSubmit handlers
        idx = txt.find('Email tài khoản')
        start = max(0, idx - 500)
        end = min(len(txt), idx + 2000)
        print("\n=== Login Component Logic Snippet ===")
        print(txt[start:end])
        break

if not found_chunk:
    print("Could not find 'Email tài khoản' in current chunks.")
