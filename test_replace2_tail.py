with open('replace_panels2.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r"cc_panel_new = '''(.*?)'''", text, re.DOTALL)
if match:
    cc = match.group(1)
    print(cc[-500:])
else:
    print('cc_panel_new not found')
