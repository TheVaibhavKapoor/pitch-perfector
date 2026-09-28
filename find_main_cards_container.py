import sys

sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
pos_card = c.find('class="product-card"')
div_start = c.rfind('<div', 0, pos_card-10)
div_start = c.rfind('<div', 0, div_start-10)
pos_intro = c.find('id="panel-intro"')
print(c[div_start:pos_intro])
