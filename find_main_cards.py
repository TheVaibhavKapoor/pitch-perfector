import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
pos_grid = c.find('class="products-grid"')
if pos_grid != -1:
    div_start = c.rfind('<div', 0, pos_grid)
    pos_end = c.find('id="panel-intro"', pos_grid)
    print(c[div_start:pos_end])
else:
    print("products-grid not found, searching product-card...")
    pos_card = c.find('class="product-card"')
    print(c[pos_card-100:pos_card+800])
