# -*- coding: utf-8 -*-
import json
import os

transcript_path = r'C:\Users\vaibh\.gemini\antigravity-ide\brain\485ac52c-f610-4a0c-861b-11a1c1471871\.system_generated\logs\transcript_full.jsonl'
output_dir = r'C:\Users\vaibh\Desktop\Pitch Perfector'

count = 0
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'PLANNER_RESPONSE' and data.get('tool_calls'):
                for tool in data['tool_calls']:
                    if tool['name'] == 'write_to_file':
                        args = tool.get('args', {})
                        target = args.get('TargetFile', '')
                        if 'solitaire_cc.html' in target:
                            content = args.get('CodeContent', '')
                            if len(content) > 1000:
                                count += 1
                                out_path = os.path.join(output_dir, f'solitaire_cc_{count}.html')
                                with open(out_path, 'w', encoding='utf-8') as out_f:
                                    out_f.write(content)
                                print(f"Restored version {count} with size {len(content)}")
        except Exception as e:
            pass

