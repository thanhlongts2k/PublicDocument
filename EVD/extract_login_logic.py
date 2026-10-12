import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'https://finlux-0wxc.onrender.com'
chunk_url = base + '/_next/static/chunks/3pou6mbh53qj_.js'
txt = requests.get(chunk_url).text

# Find where the component begins and ends
print(f"Total chunk length: {len(txt)}")

# Search for handleSubmit or async functions
with open("d:/AgentAI/PublicDocument/EVD/login_component_decompiled.js", "w", encoding="utf-8") as f:
    f.write(txt)

print("Saved full login chunk to d:/AgentAI/PublicDocument/EVD/login_component_decompiled.js")

# Find Firebase config or auth methods
firebase_matches = re.findall(r'(apiKey|authDomain|projectId|storageBucket|messagingSenderId|appId|measurementId)[\s:]+["\']([^"\']+)["\']', txt)
print("\nFirebase config found in chunk:")
for k, v in firebase_matches:
    print(f"  {k}: {v}")

# Find error strings
error_strings = re.findall(r'["\']([^"\']*(?:lỗi|thành công|thất bại|vui lòng|không đúng|mật khẩu|tài khoản|auth/)[^"\']*)["\']', txt, re.IGNORECASE)
print(f"\nDiscovered error/status messages ({len(error_strings)}):")
for s in set(error_strings):
    if len(s) < 100:
        print(f"  - {s}")
