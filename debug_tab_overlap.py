import sys

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")

print("=== Checking kompanion-tab and spoc-tab in experience_solitaire_dashboard_new.html ===")
pos = 0
while True:
    pos1 = c.find('kompanion-tab', pos)
    pos2 = c.find('spoc-tab', pos)
    if pos1 == -1 and pos2 == -1:
        break
    
    if pos1 != -1 and (pos2 == -1 or pos1 < pos2):
        print(f"Found kompanion-tab at pos {pos1}:")
        print(c[max(0, pos1-100):min(len(c), pos1+300)])
        print("-" * 50)
        pos = pos1 + 13
    else:
        print(f"Found spoc-tab at pos {pos2}:")
        print(c[max(0, pos2-100):min(len(c), pos2+300)])
        print("-" * 50)
        pos = pos2 + 8
