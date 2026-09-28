from bs4 import BeautifulSoup
import re

with open('solitaire_cc.html', 'r', encoding='utf-8') as f:
    soup_cc = BeautifulSoup(f.read(), 'html.parser')

panel_cc = soup_cc.find(id='panel-cc')
if panel_cc:
    print('Found panel-cc in solitaire_cc.html! Length:', len(str(panel_cc)))
else:
    print('Not found')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    soup_orig = BeautifulSoup(f.read(), 'html.parser')

panel_assets = soup_orig.find(id='panel-assets')
print('Found panel-assets:', panel_assets is not None)
