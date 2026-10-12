import json

with open('d:/AgentAI/PublicDocument/EVD/console_logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in console_logs.txt: {len(lines)}")
for line in lines[:30]:
    print(line.rstrip())
