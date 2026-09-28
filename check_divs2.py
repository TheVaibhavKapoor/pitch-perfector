with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="panel-assets"')
end = html.find('close panel-assets') + len('close panel-assets')
substring = html[start:end]
opens = substring.count('<div')
closes = substring.count('</div')
print('Total panel-assets Opens:', opens)
print('Total panel-assets Closes:', closes)

start2 = html.find('id="panel-investments"')
end2 = html.find('close panel-investments') + len('close panel-investments')
sub2 = html[start2:end2]
print('Total panel-investments Opens:', sub2.count('<div'))
print('Total panel-investments Closes:', sub2.count('</div'))
