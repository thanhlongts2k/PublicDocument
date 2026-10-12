import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

# find usage of the modal component I
# In JSX, it would be (0,s.jsx)(I,{isOpen:...})
matches = re.finditer(r'\(0,s\.jsx\)\(I,\{isOpen:([a-zA-Z0-9_$]+)', txt)
for m in matches:
    state_var = m.group(1)
    print(f"Modal is controlled by state variable: {state_var}")
    # find where state_var is declared or set to true
    setter_pattern = rf'([a-zA-Z0-9_$]+)\s*\((\s*!0\s*|\s*true\s*)\)'
    # find occurrences around the modal usage
    start = max(0, m.start() - 2000)
    end = min(len(txt), m.end() + 500)
    snippet = txt[start:end]
    print("Context around modal usage:")
    # look for buttons that call setter
    btns = re.findall(r'(\bbutton\b[^}}]+onClick:[^}}]+)', snippet)
    for b in btns:
        print("  Button in context:", b[:120])

# Also search for all buttons with text in Vietnamese across the landing page
all_button_texts = re.findall(r'<button[^>]*>([^<]+)</button>|\bchildren:\s*["\']([^"\']*(?:thêm|giao dịch|thử|tính|chuyển|ví|chi|thu|xem|bắt đầu|mở)[^"\']*)["\']', txt, re.IGNORECASE)
print("\nVietnamese button texts in landing chunk:")
for b1, b2 in set(all_button_texts):
    b = b1 or b2
    if b:
        print("  -", b)
