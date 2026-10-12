import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
txt = requests.get(base + '/_next/static/chunks/3yzbl7ojrs6o5.js').text

# Find all sections from 01 to 08
sections = [
    '01 / Đa ví',
    '02 / Dòng tiền tự do',
    '03 / Ngân sách chu kỳ lương',
    '04 / Báo cáo',
    '05 / Tiết kiệm',
    '06 / Giao diện',
    '07 / Độ tin cậy',
    '08 / Bắt đầu'
]

print("=== Analyzing Sections 01 to 08 ===")
for s in sections:
    idx = txt.find(s)
    if idx != -1:
        snippet = txt[idx:idx+1500]
        # find headings, numbers, buttons
        headings = re.findall(r'["\']([^"\']{4,60})["\']', snippet)
        vn_headings = [h for h in headings if any(c in h for c in ['á','à','ả','ã','ạ','é','è','ẻ','ẽ','ẹ','í','ì','ỉ','ĩ','ị','ó','ò','ỏ','õ','ọ','ú','ù','ủ','ũ','ụ','đ'])]
        print(f"\n--- Section: {s} ---")
        for v in vn_headings[:8]:
            print(f"  * {v}")
