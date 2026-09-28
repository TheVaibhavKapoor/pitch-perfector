with open('update_all_products_grid.py', 'r', encoding='utf-8') as f:
    text = f.read()
import re
match = re.search(r"cc_grid = '''(.*?)'''", text, re.DOTALL)
cc_grid = match.group(1)
print("Accor in cc_grid?", 'Accor' in cc_grid)
