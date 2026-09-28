with open('update_all_products_grid.py', 'r', encoding='utf-8') as f:
    text = f.read()
import re
match = re.search(r"cc_grid = '''(.*?)'''", text, re.DOTALL)
cc_grid = match.group(1)

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check if cc_grid is in html
print('Is cc_grid in html?', cc_grid[:100] in html)
