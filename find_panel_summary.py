import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
pos = c.find('id="panel-summary"')
print(f"id=\"panel-summary\" at pos {pos}:")
print(c[pos-50:pos+500])
