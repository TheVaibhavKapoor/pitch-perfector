import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
print("id=\"panel-investments\" in file:", 'id="panel-investments"' in c)

# Find where panel-investments is located
pos = c.find('id="panel-investments"')
if pos != -1:
    print(c[pos-100:pos+300])
