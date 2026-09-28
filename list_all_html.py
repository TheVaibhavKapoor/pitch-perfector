import os

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"
html_files = []

for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML file(s):")
for hf in html_files:
    print(" -", hf)
