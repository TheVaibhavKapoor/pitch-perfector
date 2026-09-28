with open('update_all_products_grid.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r"cc_grid = '''(.*?)'''", text, re.DOTALL)
if match:
    cc = match.group(1)
    print('<div count:', cc.count('<div'))
    print('</div> count:', cc.count('</div>'))
else:
    print('cc_grid not found')
