import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def save(f, c):
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

c = get("experience_solitaire_dashboard_new.html")

# Fix panel-assets missing </div>
pos_inv = c.find('id="panel-investments"')
pos_close_assets = c.rfind('<!-- close panel-assets -->', 0, pos_inv)

c_fixed = c[:pos_close_assets] + "</div> <!-- Explicit close for panel-assets -->\n" + c[pos_close_assets:]
save("experience_solitaire_dashboard_new.html", c_fixed)
print("Added explicit closing </div> for panel-assets!")
