import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'<div class=\"info-panel\" id=\"panel-cc\".*?(?=<div class=\"info-panel\" id=\"panel-loans\")', text, re.DOTALL)
if match:
    print(match.group(0)[:1000])
