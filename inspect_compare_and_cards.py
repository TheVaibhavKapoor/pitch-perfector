import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")

print("=== openCompareModal occurrences ===")
matches_func = [m.start() for m in re.finditer(r'openCompareModal', c)]
print("Count:", len(matches_func))
for m in matches_func:
    print(c[m-50:m+200])
    print("-" * 40)

print("\n=== product-card occurrences ===")
matches_card = [m.start() for m in re.finditer(r'class="product-card', c)]
print("Count:", len(matches_card))
for m in matches_card:
    print(c[m-20:m+150])
    print("-" * 40)
