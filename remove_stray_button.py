import re

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the button snippet right before <div class="info-panel" id="panel-dc">
stray_pattern = r'<!-- Calculate Benefit Button -->\s*<div style="margin-top: 48px; text-align: center;">\s*<button onclick="window\.open\(\'calculate_benefit\.html\', \'_blank\'\)".*?</button>\s*</div>\s*(?=<div class="info-panel" id="panel-dc">)'

content = re.sub(stray_pattern, '', content, flags=re.DOTALL)

with open('experience_solitaire_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed stray calculate benefit button before panel-dc in ETB file.")
