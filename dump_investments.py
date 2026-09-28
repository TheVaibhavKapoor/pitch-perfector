with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="panel-investments"')
end = html.find('<!-- close panel-investments -->')

with open('dump_investments.html', 'w', encoding='utf-8') as f:
    f.write(html[start:end])
