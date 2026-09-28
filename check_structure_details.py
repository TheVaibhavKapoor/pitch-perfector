import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
panels = re.findall(r'id=\"panel-[^\"]+\"', text)
print('Panels found:', panels)

for p in ['panel-dc', 'panel-cc', 'panel-assets', 'panel-investments', 'panel-forex', 'panel-other']:
    pos = text.find(f'id="{p}"')
    print(f'{p} pos:', pos)
