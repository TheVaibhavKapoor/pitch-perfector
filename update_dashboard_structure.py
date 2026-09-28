# -*- coding: utf-8 -*-
import re

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

# 2. Extract Individual Content (from <!-- Product Grid --> to the closing div of the last panel)
# We know the content body starts right before <!-- Product Grid -->
# and ends right before <script>

body_match = re.search(r'(<!-- Product Grid -->.*?)(\n\s*</script>|\n\s*<script>)', html, flags=re.DOTALL)
if body_match:
    inner_content = body_match.group(1)
    
    # We need to wrap it. However, inner_content currently goes all the way to the first script tag.
    # We only want it to go up to the end of the panels.
    # The last panel is 'panel-other'. We can find its closing </div>.
    last_panel_idx = inner_content.rfind('id="panel-other"')
    if last_panel_idx != -1:
        # Find the end of this panel. It's an info-panel, so it has a h2, p, grid, etc.
        # Let's just find the closing </div></div></div></div> sequence.
        # Actually, it's safer to just split by the exact marker.
        pass

# Let's do string replacement instead.
html = html.replace('<!-- Product Grid -->', '<div id="segment-individual-content" class="segment-wrapper active">\n                <!-- Product Grid -->')

# Now find where the panels end. We can place the closing </div> and the start of segment-business-content
# right before the <script> tags begin.
# Wait, there's a </div> for content-body before <script>? Let's check the file contents around line 850.

with open('temp_check.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Check generated")
