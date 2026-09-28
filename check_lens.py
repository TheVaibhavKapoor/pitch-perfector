with open('experience_solitaire_dashboard_v1.html', 'r', encoding='utf-8') as f:
    html_v1 = f.read()
print('v1 investments len:', html_v1.find('<!-- close panel-investments -->') - html_v1.find('id="panel-investments"'))

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html_new = f.read()
print('new investments len:', html_new.find('<!-- close panel-investments -->') - html_new.find('id="panel-investments"'))
