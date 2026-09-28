import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"

print("=== Checking all button tags containing 'EXPERIENCE SOLITAIRE' ===")

for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                content = open(filepath, 'r', encoding='utf-8', errors='ignore').read()
            except Exception:
                continue
            
            matches = [m.start() for m in re.finditer(r'EXPERIENCE SOLITAIRE', content, re.IGNORECASE)]
            for m in matches:
                tag_start = content.rfind('<', 0, m)
                tag_end = content.find('>', m)
                if tag_start != -1 and tag_end != -1:
                    tag = content[tag_start:tag_end+1]
                    if 'button' in tag.lower() or 'a ' in tag.lower():
                        print(f"File {f}:")
                        print("  Tag:", tag)
                        print("-" * 50)
