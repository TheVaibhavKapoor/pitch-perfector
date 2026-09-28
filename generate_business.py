# -*- coding: utf-8 -*-
import re
import os

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update setSegment JavaScript
new_set_segment = '''function setSegment(segmentName, element) {
            document.querySelectorAll('.segment-tab').forEach(tab => {
                tab.style.color = '#6b7280';
                tab.style.borderBottomColor = 'transparent';
            });
            element.style.color = '#d61f26';
            element.style.borderBottomColor = '#d61f26';
            
            document.querySelector('.top-header p').textContent = 'Explore the privileges of Cloud Bank Solitaire tailored for ' + segmentName + 's.';

            // Segment content toggling
            document.querySelectorAll('.segment-wrapper').forEach(wrapper => {
                wrapper.style.display = 'none';
                wrapper.classList.remove('active');
            });

            if (segmentName === 'Business') {
                const bContent = document.getElementById('segment-business-content');
                if (bContent) {
                    bContent.style.display = 'block';
                    bContent.classList.add('active');
                    if (!bContent.querySelector('.product-card.active')) {
                        bContent.querySelector('.product-card').click();
                    }
                }
            } else {
                const iContent = document.getElementById('segment-individual-content');
                if (iContent) {
                    iContent.style.display = 'block';
                    iContent.classList.add('active');
                    if (!iContent.querySelector('.product-card.active')) {
                        iContent.querySelector('.product-card').click();
                    }
                }
            }
        }'''

html = re.sub(r'function setSegment\(segmentName, element\) \{.*?(?=function showPanel)', new_set_segment + '\n\n        ', html, flags=re.DOTALL)

# 2. Extract and duplicate content
start_marker = '<!-- Product Grid -->'
end_marker = 'CALCULATE OVERALL BENEFIT\n                    </button>\n                </div>'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx) + len(end_marker)

inner_content = html[start_idx:end_idx]

# Create business content by duplicating inner_content and modifying IDs
business_content = inner_content
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

# Add wrappers
new_inner = f'<div id="segment-individual-content" class="segment-wrapper active">\n                {inner_content}\n            </div>\n\n            <div id="segment-business-content" class="segment-wrapper" style="display: none;">\n                {business_content}\n            </div>'

html = html[:start_idx] + new_inner + html[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Restructured successfully")
