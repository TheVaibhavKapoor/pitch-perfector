import sys, re

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

for fname in ["program_type_selection.html", "experience_solitaire.html", "index.html", "solitaire.html"]:
    try:
        c = get(fname)
        matches = [m.start() for m in re.finditer(r'814D4B|EXPERIENCE SOLITAIRE', c, re.IGNORECASE)]
        print(f"\n==================== {fname} ====================")
        for m in matches:
            print(c[max(0, m-100):min(len(c), m+200)])
            print("-" * 40)
    except Exception as e:
        print(f"Could not read {fname}: {e}")
