import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/AgentAI/PublicDocument/EVD/console_logs.txt', 'r', encoding='utf-8') as f:
    entries = f.read().split("="*80)

print(f"Total entries: {len(entries)}")
for i, e in enumerate(entries):
    if 'capture_browser_console_logs' in e:
        print(f"\n--- Entry {i} (Console logs call) ---")
        try:
            data = json.loads(e.strip())
            print(json.dumps(data, ensure_ascii=False, indent=2)[:1000])
        except:
            print(e[:1000])
