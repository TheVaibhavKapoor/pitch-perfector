with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

cc_start = html.find('id="panel-cc"')
assets_start = html.find('id="panel-assets"')
inv_start = html.find('id="panel-investments"')

print('cc start:', cc_start)
print('assets start:', assets_start)
print('inv start:', inv_start)

# find the depth between cc_start and assets_start
segment = html[cc_start:assets_start]
opens = segment.count('<div')
closes = segment.count('</div')
print('cc -> assets depth change:', opens - closes)
