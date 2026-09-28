import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
# search for panel-investments
pos = c.find('id="panel-investments"')
print(f"id=\"panel-investments\" at pos {pos}:")
print(c[pos-200:pos+200])
