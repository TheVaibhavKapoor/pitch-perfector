import re

# 1. Read customer_overview_solitaire.html to extract the compare-modal HTML
with open('customer_overview_solitaire.html', 'r', encoding='utf-8') as f:
    solitaire_content = f.read()
    
# Extract compare-modal
match = re.search(r'(<!-- Compare Modal -->\s*<div id="compare-modal".*?</div>\s*</div>\s*</div>\s*<script>.*?</script>)', solitaire_content, re.DOTALL)
if match:
    compare_modal_html = match.group(1)
else:
    # Try another pattern
    match = re.search(r'(<!-- Compare Modal -->\s*<div id="compare-modal".*?</div>\s*</div>\s*</div>)', solitaire_content, re.DOTALL)
    compare_modal_html = match.group(1)
    
# Add the toggle script if not in the first match
if 'function toggleCompareCategory' not in compare_modal_html:
    script_match = re.search(r'(<script>\s*function toggleCompareCategory.*?</script>)', solitaire_content, re.DOTALL)
    if script_match:
        compare_modal_html += '\n' + script_match.group(1)

# 2. Add it to experience_solitaire_dashboard_new.html
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    target_content = f.read()

# Add button
btn_html = '''
                  <!-- Calculate Benefit Button -->
                  <div style="margin-top: 48px; text-align: center; display: flex; justify-content: center; gap: 16px;">
                      <button onclick="window.open('calculate_benefit.html', '_blank')" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; border: none; padding: 16px 32px; border-radius: 8px; font-weight: 600; font-size: 1.1rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                          CALCULATE OVERALL BENEFIT
                      </button>
                      <button onclick="document.getElementById('compare-modal').style.display='flex'" style="background: white; border: 2px solid #0f172a; color: #0f172a; padding: 16px 32px; border-radius: 8px; font-weight: 600; font-size: 1.1rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                          COMPARE PROGRAMS
                      </button>
                  </div>
'''

target_content = re.sub(
    r'<!-- Calculate Benefit Button -->\s*<div style="margin-top: 48px; text-align: center;">.*?</div>',
    btn_html,
    target_content,
    flags=re.DOTALL
)

# Append modal right before </body>
target_content = target_content.replace('</body>', compare_modal_html + '\n</body>')

with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Added compare modal and button to dashboard!")
