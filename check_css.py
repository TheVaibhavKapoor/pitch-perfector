import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('info-panel matches in HTML/CSS:')
for m in re.finditer(r'\.info-panel[^{]*\{[^}]*\}', text):
    print(m.group(0))
