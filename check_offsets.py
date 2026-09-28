with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()
print('assets start:', html.find('id="panel-assets"'))
print('assets close:', html.find('<!-- close panel-assets -->'))
print('investments start:', html.find('id="panel-investments"'))
print('investments close:', html.find('<!-- close panel-investments -->'))
