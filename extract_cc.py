# -*- coding: utf-8 -*-
import json

transcript_path = r'C:\Users\vaibh\.gemini\antigravity-ide\brain\485ac52c-f610-4a0c-861b-11a1c1471871\.system_generated\logs\transcript_full.jsonl'
output_path = r'C:\Users\vaibh\Desktop\Pitch Perfector\solitaire_cc.html'

found = False
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'PLANNER_RESPONSE' and data.get('tool_calls'):
                for tool in data['tool_calls']:
                    if tool['name'] == 'write_to_file' or tool['name'] == 'write_to_file':
                        args = tool.get('args', {})
                        target = args.get('TargetFile', '')
                        if 'solitaire_cc.html' in target:
                            with open(output_path, 'w', encoding='utf-8') as out_f:
                                out_f.write(args.get('CodeContent', ''))
                            found = True
                            # We want the FIRST creation (which has the full content)
                            break
            if found:
                break
        except Exception as e:
            pass

if found:
    print("Found and restored solitaire_cc.html")
else:
    print("Not found in transcript")
