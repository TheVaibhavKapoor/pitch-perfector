import re

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

def get_div_content(div_id):
    start = text.find(f'id="{div_id}"')
    if start == -1: return 'not found'
    div_start = text.rfind('<div', 0, start)
    open_divs = 1
    i = text.find('>', start) + 1
    while open_divs > 0 and i < len(text):
        next_open = text.find('<div', i)
        next_close = text.find('</div', i)
        if next_open == -1: next_open = len(text)
        if next_close == -1: next_close = len(text)
        
        if next_open < next_close:
            open_divs += 1
            i = next_open + 4
        else:
            open_divs -= 1
            i = next_close + 5
    return text[div_start:i+1]

cc = get_div_content('panel-cc')
assets = get_div_content('panel-assets')
investments = get_div_content('panel-investments')

with open('panel_cc_debug.html', 'w', encoding='utf-8') as f:
    f.write(cc)
with open('panel_assets_debug.html', 'w', encoding='utf-8') as f:
    f.write(assets)
with open('panel_investments_debug.html', 'w', encoding='utf-8') as f:
    f.write(investments)
print('Extracted panels')
