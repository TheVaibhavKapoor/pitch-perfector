with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# find end of cc_panel
idx1 = text.find('Point value: Value of 1 Maharaja Point (Air India) = ?1, Value of 1 Accor Point = ?2')
idx2 = text.find('</p>', idx1)
idx2 += 4 # length of </p>

idx3 = text.find('<div id="panel-assets"')

garbage = text[idx2:idx3]
import sys
sys.stdout.reconfigure(encoding='utf-8')
print(repr(garbage))
