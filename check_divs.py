with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="panel-assets"')
end = html.find('id="assets-existing-table"')
substring = html[start:end]
opens = substring.count('<div')
closes = substring.count('</div')
print('assets Opens:', opens)
print('assets Closes:', closes)

start2 = html.find('id="panel-investments"')
end2 = html.find('id="investments-existing-table"')
sub2 = html[start2:end2]
print('investments Opens:', sub2.count('<div'))
print('investments Closes:', sub2.count('</div'))
