import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")

print("=== panel-assets snippet ===")
pos_assets = c.find('id="panel-assets"')
if pos_assets != -1:
    div_start = c.rfind('<div', 0, pos_assets)
    pos_inv = c.find('id="panel-investments"')
    print(c[div_start:pos_assets+500])

print("\n=== panel-investments snippet ===")
pos_inv = c.find('id="panel-investments"')
if pos_inv != -1:
    div_start = c.rfind('<div', 0, pos_inv)
    pos_forex = c.find('id="panel-forex"')
    print(c[div_start:pos_inv+500])
