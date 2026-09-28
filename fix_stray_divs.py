import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove stray </div> <!-- close [panel]-new-grid --> which breaks the DOM
    new_content = re.sub(r'</div> <!-- close [a-z]+-new-grid -->\n?', '', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file}")
