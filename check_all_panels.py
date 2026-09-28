import re

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

panels = ['dc', 'cc', 'assets', 'investments', 'forex', 'other', 'business-dc', 'business-cc', 'business-assets', 'business-investments', 'business-forex', 'business-other']

for p in panels:
    start_str = f'id="panel-{p}"'
    end_str = f'<!-- close panel-{p} -->'
    start = html.find(start_str)
    end = html.find(end_str)
    if start == -1 or end == -1:
        continue
    
    segment = html[start:end]
    opens = segment.count('<div')
    closes = segment.count('</div')
    print(f'{p}: opens={opens}, closes={closes}, diff={opens-closes}')
