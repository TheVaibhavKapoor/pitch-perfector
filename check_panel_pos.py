import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

for p in ['panel-dc', 'panel-cc', 'panel-assets', 'panel-investments', 'panel-forex', 'panel-other']:
    print(f"{p}:", text.find(f'id="{p}"'))
