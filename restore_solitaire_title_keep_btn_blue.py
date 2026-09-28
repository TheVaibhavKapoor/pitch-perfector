import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"

ORIGINAL_GRADIENT = "linear-gradient(135deg, #CDA4A1 0%, #AA7774 25%, #814D4B 50%, #552B2A 75%, #E3CDCC 100%)"
DARK_BLUE_BTN_BG = "#1e3a8a"

print("=== Restoring original title/logo gradient while keeping ONLY EXPERIENCE SOLITAIRE button dark blue ===")

for fname in ["program_type_selection.html", "experience_solitaire.html", "temp_exp.html"]:
    filepath = os.path.join(workspace_dir, fname)
    if not os.path.exists(filepath):
        continue
    
    c = open(filepath, 'r', encoding='utf-8', errors='ignore').read()
    
    # Restore title/logo background gradient containing #182545 back to #814D4B
    c = c.replace(
        "linear-gradient(135deg, #CDA4A1 0%, #AA7774 25%, #182545 50%, #552B2A 75%, #E3CDCC 100%)",
        ORIGINAL_GRADIENT
    )
    
    # Ensure btnBg is Dark Blue (#1e3a8a or #182545)
    c = c.replace("btnBg: '#814D4B'", "btnBg: '#1e3a8a'")
    c = c.replace("btnBg: '#182545'", "btnBg: '#1e3a8a'")
    
    # Ensure button background inline style is #1e3a8a
    c = re.sub(
        r'(<button[^>]*style="[^"]*background:\s*)[^;"]+([^"]*">EXPERIENCE SOLITAIRE</button>)',
        r'\g<1>#1e3a8a\g<2>',
        c,
        flags=re.IGNORECASE
    )
    
    with open(filepath, 'w', encoding='utf-8') as fp:
        fp.write(c)
    
    print(f"Updated {fname}: Title gradient restored to original, button kept in Dark Blue (#1e3a8a)!")

print("\n==================== SUCCESS: Title/Logo restored, ONLY button is Dark Blue! ====================")
