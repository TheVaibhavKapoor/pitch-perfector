with open('experience_solitaire_dashboard_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()
idx = html.find('id="panel-business-other"')
segment = html[idx:]
opens = segment.count('<div')
closes = segment.count('</div')
print('panel-business-other to end depth:', opens - closes)
