import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

inv_start = text.find('id="panel-investments"')
inv_end = text.find('id="panel-forex"')
print('=== INVESTMENTS PANEL ===')
print(text[inv_start:inv_end])

print()
assets_start = text.find('id="panel-assets"')
assets_end = text.find('id="panel-investments"')
print('=== ASSETS/LOANS PANEL ===')
print(text[assets_start:assets_end])
