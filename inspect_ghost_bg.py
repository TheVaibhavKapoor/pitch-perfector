import sys, re

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")

print("=== Checking all position: fixed / absolute elements ===")
pos_matches = [m.start() for m in re.finditer(r'position:\s*fixed', c)]
print(f"Found {len(pos_matches)} position:fixed occurrence(s):")
for p in pos_matches:
    print(c[max(0, p-50):min(len(c), p+300)])
    print("=" * 60)
