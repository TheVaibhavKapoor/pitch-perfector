import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

NEW_INVESTMENTS_PANEL = open('inv_panel.html', 'r', encoding='utf-8').read()
NEW_ASSETS_PANEL = open('assets_panel.html', 'r', encoding='utf-8').read()
INV_CALC_JS = open('inv_calc.js', 'r', encoding='utf-8').read()

for fname in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace investments panel
    inv_start = text.find('id="panel-investments"')
    inv_end = text.find('id="panel-forex"')
    if inv_start == -1 or inv_end == -1:
        print(f'{fname}: panel-investments or panel-forex not found!')
        continue
    div_start = text.rfind('<div ', 0, inv_start)
    text = text[:div_start] + NEW_INVESTMENTS_PANEL + '\n\n                ' + text[inv_end:]

    # Replace assets panel
    assets_start = text.find('id="panel-assets"')
    assets_end = text.find('id="panel-investments"')
    if assets_start == -1 or assets_end == -1:
        print(f'{fname}: panel-assets or panel-investments not found!')
        continue
    div_start = text.rfind('<div ', 0, assets_start)
    text = text[:div_start] + NEW_ASSETS_PANEL + '\n\n                ' + text[assets_end:]

    # Add investment calculator JS before </body>
    if 'function calcInv' not in text:
        text = text.replace('</body>', '\n    <script>\n' + INV_CALC_JS + '\n    </script>\n</body>')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f'Updated {fname}')

print('Done!')
