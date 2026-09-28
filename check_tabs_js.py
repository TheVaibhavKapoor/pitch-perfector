import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'nav-card', text)
for m in matches:
    print('nav-card at', m.start())

script_idx = text.find('navCards.forEach')
if script_idx != -1:
    print(text[script_idx-200:script_idx+500])
else:
    print('navCards not found!')
