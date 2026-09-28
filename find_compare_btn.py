import sys

sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
pos_btn = c.find('Compare Program')
while pos_btn != -1:
    print(f"Found 'Compare Program' at pos {pos_btn}:")
    print(c[pos_btn-100:pos_btn+200])
    print("-" * 50)
    pos_btn = c.find('Compare Program', pos_btn + 1)
