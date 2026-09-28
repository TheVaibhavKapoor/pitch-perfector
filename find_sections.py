import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
lines = c.split('\n')

print("Total lines:", len(lines))

# Search for section headings
for idx, line in enumerate(lines):
    if any(h in line.lower() for h in ['solitaire', 'lifestyle', 'investment', 'lending', 'credit card', 'banking', 'program intro']):
        if len(line.strip()) < 120 and ('<h' in line or 'class=' in line or 'id=' in line):
            print(f"Line {idx+1}: {line.strip()}")
