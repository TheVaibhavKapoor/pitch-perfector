with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

dc = html.find('id="panel-dc"')
cc = html.find('id="panel-cc"')
assets = html.find('id="panel-assets"')
inv = html.find('id="panel-investments"')
forex = html.find('id="panel-forex"')
other = html.find('id="panel-other"')

def print_depth(name1, p1, name2, p2):
    segment = html[p1:p2]
    opens = segment.count('<div')
    closes = segment.count('</div')
    print(f'{name1} -> {name2} depth change: {opens - closes}')

print_depth('dc', dc, 'cc', cc)
print_depth('cc', cc, 'assets', assets)
print_depth('assets', assets, 'inv', inv)
print_depth('inv', inv, 'forex', forex)
print_depth('forex', forex, 'other', other)
