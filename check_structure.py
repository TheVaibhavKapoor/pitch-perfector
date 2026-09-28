import os

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('panel-assets index:', html.find('id="panel-assets"'))
print('assets-existing-table index:', html.find('id="assets-existing-table"'))
print('close panel-assets index:', html.find('close panel-assets'))
print('panel-investments index:', html.find('id="panel-investments"'))
print('investments-existing-table index:', html.find('id="investments-existing-table"'))
print('close panel-investments index:', html.find('close panel-investments'))
