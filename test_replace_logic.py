with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div id="panel-cc" class="info-panel">.*?(?=<div id="panel-assets" class="info-panel">)', text, flags=re.DOTALL)
print('Number of matches:', len(matches))
