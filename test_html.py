with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find index of panel-cc, panel-assets, etc
print('panel-cc at', text.find('id="panel-cc"'))
print('panel-assets at', text.find('id="panel-assets"'))
print('panel-investments at', text.find('id="panel-investments"'))
print('panel-business-cc at', text.find('id="panel-business-cc"'))
