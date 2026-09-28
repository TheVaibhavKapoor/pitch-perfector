with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

dc = html.find('id="panel-dc"')
dc_close = html.find('<!-- close panel-dc -->')
cc = html.find('id="panel-cc"')

print(f"dc start: {dc}, dc close: {dc_close}, cc start: {cc}")
