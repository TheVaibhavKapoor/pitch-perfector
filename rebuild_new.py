import re
import os

with open('temp_check.html', 'r', encoding='utf-8') as f:
    html = f.read()

# temp_check.html has:
# <div id="segment-individual-content" class="segment-wrapper active">
#    <!-- Product Grid -->
#    ... panels ...
#    <button>CALCULATE OVERALL BENEFIT</button>
# </div> (wait, is it closed?)

# Actually, let's just find the start of <!-- Product Grid -->
start_idx = html.find('<!-- Product Grid -->')
# Find where the panels end (before CALCULATE OVERALL BENEFIT)
end_idx = html.find('<div style="text-align: center; margin-top: 40px;">', start_idx)

panels_content = html[start_idx:end_idx]

# Create business content by duplicating panels_content
business_content = panels_content
business_content = business_content.replace("showPanel('dc'", "showPanel('business-dc'")
business_content = business_content.replace("showPanel('cc'", "showPanel('business-cc'")
business_content = business_content.replace("showPanel('assets'", "showPanel('business-assets'")
business_content = business_content.replace("showPanel('investments'", "showPanel('business-investments'")
business_content = business_content.replace("showPanel('forex'", "showPanel('business-forex'")
business_content = business_content.replace("showPanel('other'", "showPanel('business-other'")

business_content = business_content.replace('id="panel-dc"', 'id="panel-business-dc"')
business_content = business_content.replace('id="panel-cc"', 'id="panel-business-cc"')
business_content = business_content.replace('id="panel-assets"', 'id="panel-business-assets"')
business_content = business_content.replace('id="panel-investments"', 'id="panel-business-investments"')
business_content = business_content.replace('id="panel-forex"', 'id="panel-business-forex"')
business_content = business_content.replace('id="panel-other"', 'id="panel-business-other"')

# Combine
new_inner = f'<div id="segment-individual-content" class="segment-wrapper active">\n                {panels_content}\n            </div>\n\n            <div id="segment-business-content" class="segment-wrapper" style="display: none;">\n                {business_content}\n            </div>\n\n            '

html = html[:start_idx] + new_inner + html[end_idx:]

with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Base recreated!')
