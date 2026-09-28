with open('replace_panels2.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r"cc_panel_new = '''(.*?)'''", text, re.DOTALL)
if match:
    cc = match.group(1)
    print('<div count:', cc.count('<div'))
    print('</div> count:', cc.count('</div>'))
else:
    print('cc_panel_new not found')
