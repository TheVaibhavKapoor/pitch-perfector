import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"

print("=== Searching for 'EXPERIENCE SOLITAIRE' buttons ===")

found_count = 0
for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                content = open(filepath, 'r', encoding='utf-8', errors='ignore').read()
            except Exception:
                continue
            
            matches = [m.start() for m in re.finditer(r'EXPERIENCE SOLITAIRE', content, re.IGNORECASE)]
            if matches:
                found_count += 1
                print(f"\nIn file: {f}")
                for m in matches:
                    print("  Snippet:", content[max(0, m-80):min(len(content), m+120)].replace('\n', ' '))

print(f"\nFound in {found_count} HTML file(s)!")
