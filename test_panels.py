import re

for filepath in ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f'{filepath} panels:')
    matches = re.findall(r'id="(panel-[^"]*)"', text)
    print(matches)
