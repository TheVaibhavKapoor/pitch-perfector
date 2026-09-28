# -*- coding: utf-8 -*-
import re
import os

solitaire_cc_path = r'c:\Users\vaibh\Desktop\Pitch Perfector\solitaire_cc.html'
dashboard_path = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'

with open(solitaire_cc_path, 'r', encoding='utf-8') as f:
    cc_content = f.read()

# Extract the product-features-grid (7 feature cards)
features_match = re.search(r'(<div class="product-features-grid">.*?</div>\s*</div>\s*</div>)', cc_content, re.DOTALL)
if features_match:
    features_html = features_match.group(1)
    # The regex might grab too much due to the nested divs.
    # Let's use a simpler regex for features.
    features_match = re.search(r'<div class="product-features-grid">.*?<!-- 7\. Hotel Benefits Card \(Span 2 Cols\) -->.*?</div>\s*</div>', cc_content, re.DOTALL)
    if features_match:
        features_html = features_match.group(0)

# Let's re-extract explicitly to be safe
# The grid starts at <div class="product-features-grid"> and ends after the 7th card.
features_start = cc_content.find('<!-- Structured Product Info Sections Grid -->')
features_end = cc_content.find('<!-- 2. Pitch Tab Content -->')
features_html = cc_content[features_start:features_end]
# Remove any closing tab-pane divs at the end of features_html
features_html = re.sub(r'</div>\s*</div>\s*$', '', features_html).strip()


# Extract the calculator html
calc_start = cc_content.find('<div class="tab-pane" id="reward-calculator">')
calc_end = cc_content.find('<!-- Right Side Floating Kompanion Tab -->')
calc_html = cc_content[calc_start:calc_end]
# Remove the <div class="tab-pane" id="reward-calculator"> wrapper so it's just the content, 
# or keep it but remove the "tab-pane" class so it's always visible.
calc_html = calc_html.replace('<div class="tab-pane" id="reward-calculator">', '<div id="reward-calculator" style="margin-top: 40px; margin-bottom: 40px;">')
# There's a couple of </div> at the end of calc_html that close the tab-pane and tab-content.
calc_html = re.sub(r'</div>\s*</div>\s*</div>\s*$', '', calc_html).strip()

# Extract the JS script
js_start = cc_content.find('// Flow-Matched Calculation Logic')
js_end = cc_content.find('</body>')
js_script = cc_content[js_start:js_end].strip()
if js_script.endswith('</script>'):
    js_script = js_script[:-9].strip()

# Combine features and calc
new_cc_content = f'''<div style="grid-column: 1 / -1;">
{features_html}
</div>
{calc_html}
'''

# Now update the dashboard
with open(dashboard_path, 'r', encoding='utf-8') as f:
    dashboard_content = f.read()

# Replace the inner grid of panel-cc
# We replace from <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px;"> 
# inside panel-cc down to the bottom of the button
replace_pattern = r'(<div id="panel-cc" class="info-panel active">\s*<h2[^>]*>Solitaire Credit Card</h2>\s*<p[^>]*>.*?</p>\s*)<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px;">.*?<div style="background: #f9fafb; padding: 24px; border-radius: 12px; text-align: center; grid-column: 1 / -1;">\s*<img src="solitaire_infinity_logo\.png"[^>]*>\s*<a href="solitaire_cc\.html"[^>]*>View EMI & Rewards Calculator</a>\s*</div>\s*</div>'

dashboard_content = re.sub(replace_pattern, r'\g<1>' + new_cc_content, dashboard_content, flags=re.DOTALL)


# Append the JS before </body>
js_to_append = f'''
    <script>
        {js_script}
    </script>
'''
dashboard_content = dashboard_content.replace('</body>', js_to_append + '\n</body>')

with open(dashboard_path, 'w', encoding='utf-8') as f:
    f.write(dashboard_content)

print("Merged features and calculator from CC into Dashboard")

# Remove solitaire_cc.html
if os.path.exists(solitaire_cc_path):
    os.remove(solitaire_cc_path)
    print("Deleted solitaire_cc.html")
