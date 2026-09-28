import os
import re

file_path = 'customer_overview_solitaire.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the Personalised offers (Slim) section
pattern = r'<!-- Personalised offers \(Slim\) -->.*?<!-- Customer Cues \(Slim\) -->'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find Personalised offers (Slim) section")
    exit(1)

# Replace it with just the Customer Cues comment
content = content[:match.start()] + '<!-- Customer Cues (Slim) -->' + content[match.end():]

# Make the Customer Cues take up the full width instead of flex: 2
# Currently it has flex: 2; min-width: 450px;
content = content.replace('flex: 2; min-width: 450px;', 'flex: 1; min-width: 100%;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed Personalised offers box and expanded Customer Cues box.")
