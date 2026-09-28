with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('id="panel-assets"')
with open('out.txt', 'w', encoding='utf-8') as out:
    out.write(text[idx-500:idx])
