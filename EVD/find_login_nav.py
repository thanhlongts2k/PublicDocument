with open('d:/AgentAI/PublicDocument/EVD/login_component_decompiled.js', 'r', encoding='utf-8') as f:
    txt = f.read()

import re

# find router navigation
matches = re.findall(r'(router\.(?:push|replace)\([^)]+\)|window\.location[^;,\n]+)', txt)
print("Router / navigation calls:")
for m in set(matches):
    print("  ", m)

# find functions and state variables
print("\nSubmit handler snippets:")
for m in re.finditer(r'(handleSubmit|signInWith|createUserWith|sendPasswordReset)', txt):
    s = max(0, m.start() - 100)
    e = min(len(txt), m.end() + 300)
    print("--- Function context ---")
    print(txt[s:e])
