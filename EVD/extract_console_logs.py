import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

transcript_path = 'C:/Users/LongLouis/.gemini/antigravity-ide/brain/a6d5b7e0-198c-4b5e-acbe-5dae50f1ca08/.system_generated/logs/transcript.jsonl'
output_path = 'd:/AgentAI/PublicDocument/EVD/console_logs.txt'

logs_found = []

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        # Check tool result
        content = obj.get('content', '')
        if 'capture_browser_console_logs' in str(obj) or 'console' in str(content).lower():
            logs_found.append(obj)

with open(output_path, 'w', encoding='utf-8') as out:
    for item in logs_found:
        out.write(json.dumps(item, ensure_ascii=False, indent=2))
        out.write("\n" + "="*80 + "\n")

print(f"Extracted {len(logs_found)} console/interaction steps into {output_path}")
