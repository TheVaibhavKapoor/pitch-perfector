import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
# Find all product cards with their onclick
cards = list(re.finditer(r'<div class="product-card[^"]*" onclick="([^"]+)"', c))
for i, m in enumerate(cards):
    pos = m.start()
    line_num = c[:pos].count('\n') + 1
    print(f"Card {i} (Line {line_num}): {m.group(1)}")
