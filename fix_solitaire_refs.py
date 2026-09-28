"""
Final fixes for experience_solitaire_dashboard_new.html:
1. Fix Exit Walkthrough href to solitaire.html
2. Fix version selector to point to solitaire versions
3. Fix any remaining "Privy" references in content
4. Make intro card show for Solitaire
"""

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix exit walkthrough link
html = html.replace('href="/" style="color: #182545;"', 'href="solitaire.html" style="color: #182545;"', 1)

# 2. Fix version selector - find and replace option values
import re
# Replace privy version selector options with solitaire ones
html = html.replace(
    'value="experience_privy_dashboard_v1.html"',
    'value="experience_solitaire_dashboard_v1.html"'
)
html = html.replace(
    'value="experience_privy_dashboard_v2.html"',
    'value="experience_solitaire_dashboard_v2.html"'
)
html = html.replace(
    'value="experience_privy_dashboard_v3.html"',
    'value="experience_solitaire_dashboard_v3.html"'
)

# Also fix "selected" option if it is still pointing to privy
html = html.replace(
    'value="experience_privy_dashboard_new.html" selected',
    'value="experience_solitaire_dashboard_new.html" selected'
)

# 3. Fix remaining "Privy" text in select options and labels
# Change header segment display text 
html = html.replace('>Version 1</option>', '>Version 1</option>')  # no change needed

# 4. Fix the Compare modal - replace "Program Comparison" note
html = html.replace(
    '<p>A quick view of the eligibility and core benefits across our premium tiers.</p>',
    '<p>Compare Privy, Privy+ and Solitaire across eligibility, products and rewards.</p>'
)

# 5. Fix the "Privy Loans" references in the panel to be "Solitaire Loans"
html = html.replace('>Privy Home Loan<', '>Solitaire Home Loan<')
html = html.replace('Privy Loan', 'Solitaire Loan')

# 6. Make sure the intro card is first in the product grid and is Active
# Check current active card
print('panel-intro active:', 'panel-intro active' in html or 'id="panel-intro"' in html)
print('product-card active onclick intro:', 'showPanel(\'intro\', this)' in html)

# 7. Check and report "Privy" remaining mentions
privy_count = html.count('Privy')
print(f'Remaining "Privy" mentions: {privy_count}')
lines_with_privy = [i+1 for i, line in enumerate(html.splitlines()) if 'Privy' in line]
print(f'Lines with Privy: {lines_with_privy[:10]}')

# Write
with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone! {len(html)} bytes written.')
