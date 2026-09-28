import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

opens = len(re.findall(r'<div[\s>]', text))
closes = len(re.findall(r'</div>', text))
print(f'Opens: {opens}, Closes: {closes}, Diff: {opens-closes}')
print()

# We have 1 extra </div> - need to find which one is extra
# The correct closing at end should be:
# </div> (close panel-other or last panel)
# </div> (close content-body at depth=2->1)
# </div> (close segment-individual or similar, 1->0)
# Wait but we also have </main> then </div> for app-layout

# Let's trace around the injection points to find the extra </div>
# The panels themselves (inv_panel.html and assets_panel.html) might have extra divs

# Check inv_panel.html
with open('inv_panel.html', 'r', encoding='utf-8') as f:
    inv = f.read()
inv_opens = len(re.findall(r'<div[\s>]', inv))
inv_closes = len(re.findall(r'</div>', inv))
print(f'inv_panel.html: opens={inv_opens}, closes={inv_closes}, diff={inv_opens-inv_closes}')

with open('assets_panel.html', 'r', encoding='utf-8') as f:
    assets = f.read()
assets_opens = len(re.findall(r'<div[\s>]', assets))
assets_closes = len(re.findall(r'</div>', assets))
print(f'assets_panel.html: opens={assets_opens}, closes={assets_closes}, diff={assets_opens-assets_closes}')
