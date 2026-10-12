import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

subagent_id = 'a6d5b7e0-198c-4b5e-acbe-5dae50f1ca08'
transcript_path = f'C:/Users/LongLouis/.gemini/antigravity-ide/brain/{subagent_id}/.system_generated/logs/transcript.jsonl'

print(f"Reading transcript from {transcript_path}...")
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        step = obj.get('step_index')
        src = obj.get('source')
        stype = obj.get('type')
        if obj.get('tool_calls'):
            for tc in obj['tool_calls']:
                print(f"[Step {step}] TOOL CALL: {tc.get('name')} -> args: {tc.get('args')}")
        if obj.get('type') == 'PLANNER_RESPONSE' and obj.get('thinking'):
            # print first 150 chars of thinking
            think = obj['thinking'].replace('\n', ' ')[:140]
            print(f"[Step {step}] THINK: {think}...")
        if 'error' in str(obj).lower() and 'error' in obj:
            print(f"[Step {step}] ERROR: {obj.get('error')}")
