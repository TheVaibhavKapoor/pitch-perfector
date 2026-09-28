import re
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'function showPanel[\s\S]*?\}', text)
if match:
    print(match.group(0))
