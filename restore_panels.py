from bs4 import BeautifulSoup
import re

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

start = orig_html.find('<div class="info-panel" id="panel-assets">')
end = orig_html.find('<!-- close segment-individual-content -->')
missing_panels_html = orig_html[start:end]

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    new_html = f.read()

insert_pos = new_html.find('<!-- close segment-individual-content -->')
if start != -1 and insert_pos != -1:
    fixed_html = new_html[:insert_pos] + missing_panels_html + new_html[insert_pos:]
    with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
        f.write(fixed_html)
    print('Restored missing panels to Solitaire NTB')
else:
    print('Failed to restore missing panels', start, insert_pos)
