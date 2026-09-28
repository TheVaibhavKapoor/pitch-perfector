with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('id="panel-assets"')
print(repr(text[idx-20:idx+30]))
