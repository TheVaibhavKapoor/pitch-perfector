import os
import re

dash_file = 'experience_solitaire_dashboard_new.html'
with open(dash_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the global html and body resets that we accidentally brought in from calculate_benefit.html
content = re.sub(r'html\s*\{\s*font-size:\s*93%;\s*\}', '', content)
content = re.sub(r'html,\s*body\s*\{[^}]*\}', '', content)

with open(dash_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Removed global html/body resets from {dash_file}")
