import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"

DARK_BLUE = "#182545"

print(f"=== Replacing Solitaire Button Color #814D4B with Dark Blue ({DARK_BLUE}) across all files ===")

files_changed = 0

for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.endswith('.html') or f.endswith('.js') or f.endswith('.css'):
            filepath = os.path.join(root, f)
            try:
                content = open(filepath, 'r', encoding='utf-8', errors='ignore').read()
            except Exception:
                continue
            
            new_content = content
            
            # Replace #814D4B / #814d4b in btnBg or inline styles
            if '#814D4B' in new_content or '#814d4b' in new_content or '#814d4b' in new_content.lower():
                new_content = re.sub(r'#814[dD]4[bB]', DARK_BLUE, new_content)
                print(f"Replaced #814D4B in {f}")
            
            # Replace background: #814D4B or background:#814D4B
            # Check for inline style background on EXPERIENCE SOLITAIRE buttons
            button_pattern = re.compile(r'(<button[^>]*>EXPERIENCE SOLITAIRE</button>)', re.IGNORECASE)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)
                files_changed += 1

print(f"\n==================== SUCCESS: Updated button color to Dark Blue in {files_changed} file(s)! ====================")
