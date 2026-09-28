with open('replace_panels2.py', 'r', encoding='utf-8') as f:
    text = f.read()
import re
match = re.search(r"cc_panel_new = '''(.*?)'''", text, re.DOTALL)
cc_new = match.group(1)
print("Accor in cc_panel_new?", 'Accor' in cc_new)
