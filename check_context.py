with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="panel-investments"')
print(html[idx-500:idx+100])
