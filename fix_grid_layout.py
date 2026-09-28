import os
import re

dash_file = 'experience_solitaire_dashboard_new.html'

if not os.path.exists(dash_file):
    print("File not found")
    exit()

with open(dash_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix grid template
content = content.replace('grid-template-columns: repeat(12, 1fr);', 'grid-template-columns: repeat(12, minmax(0, 1fr));')

# Enforce spans
content = content.replace('.bento-col-8 { grid-column: span 8; }', '.bento-col-8 { grid-column: span 8 !important; }')
content = content.replace('.bento-col-4 { grid-column: span 4; }', '.bento-col-4 { grid-column: span 4 !important; }')
content = content.replace('.bento-col-6 { grid-column: span 6; }', '.bento-col-6 { grid-column: span 6 !important; }')
content = content.replace('.bento-col-12 { grid-column: span 12; }', '.bento-col-12 { grid-column: span 12 !important; }')

# For smaller screens, maybe the media query was 900px, but 1280px is what the user uses (from metadata: Viewport 1280x585).
# At 1280px, they should be span 8 and span 4.

with open(dash_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated grid CSS.")
