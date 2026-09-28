import json
log_path = r'c:\Users\vaibh\.gemini\antigravity-ide\brain\485ac52c-f610-4a0c-861b-11a1c1471871\.system_generated\logs\transcript_full.jsonl'

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if 'Copy-Item' in line and 'experience_solitaire_dashboard' in line:
            print(line[:1000])
