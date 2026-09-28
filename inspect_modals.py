import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")

print("=== Checking all modal divs ===")
matches = [m.start() for m in re.finditer(r'id="[^"]*modal[^"]*"', c, re.IGNORECASE)]
print(f"Found {len(matches)} modal occurrence(s):")
for m in matches:
    print(c[max(0, m-20):min(len(c), m+150)])
    print("-" * 50)
