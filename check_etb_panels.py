import sys

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("customer_overview_solitaire.html")
print("panel-assets in ETB:", c.find('id="panel-assets"'))
print("panel-investments in ETB:", c.find('id="panel-investments"'))
