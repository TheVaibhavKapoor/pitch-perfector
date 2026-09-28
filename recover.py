import json
import os

log_path = r'c:\Users\vaibh\.gemini\antigravity-ide\brain\485ac52c-f610-4a0c-861b-11a1c1471871\.system_generated\logs\transcript_full.jsonl'

last_content = None
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            continue
            
        if 'tool_calls' in entry:
            for tc in entry['tool_calls']:
                if tc['name'] == 'write_to_file' and 'experience_solitaire_dashboard_new.html' in tc['args'].get('TargetFile', ''):
                    last_content = tc['args'].get('CodeContent')
                    
if last_content:
    with open('recovered.html', 'w', encoding='utf-8') as f:
        f.write(last_content)
    print(f'Recovered file length: {len(last_content)}')
else:
    print('Not found')
