import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/AgentAI/PublicDocument/EVD/login_component_decompiled.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('Đăng nhập thành công')
if idx != -1:
    print("=== Login Success Handler Snippet ===")
    print(txt[max(0, idx-400):min(len(txt), idx+600)])

idx2 = txt.find('Tạo tài khoản & Bắt đầu')
if idx2 != -1:
    print("\n=== Register Submit Handler Snippet ===")
    print(txt[max(0, idx2-400):min(len(txt), idx2+600)])

# Search for any URL or push strings
print("\n=== All String Literals with / or http ===")
urls = set(re.findall(r'["\']([a-zA-Z0-9_\-\./#?=&:]+)["\']', txt))
for u in sorted(urls):
    if any(k in u.lower() for k in ['http', '/', 'dashboard', 'app', 'home']):
        if len(u) < 80:
            print("  *", u)
