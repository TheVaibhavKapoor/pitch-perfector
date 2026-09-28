with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find all showPanel calls
print("showPanel calls:")
calls = re.findall(r'showPanel\([^\)]+\)', text)
for c in set(calls):
    print(" -", c)

print("\nPanel IDs:")
panels = re.findall(r'id="(panel-[^"]*)"', text)
for p in panels:
    print(" -", p)
