import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
print("panel-intro in file:", 'id="panel-intro"' in c)
print("panel-lifestyle in file:", 'id="panel-lifestyle"' in c)
print("panel-investments in file:", 'id="panel-investments"' in c)

# find all info-panels
panels = re.findall(r'<div class="info-panel[^"]*" id="[^"]+"', c)
print("\nAll info panels:")
for p in panels:
    print(" ", p)
