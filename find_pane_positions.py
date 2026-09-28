import sys

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
print("loan-content-hl pos:", c.find('id="loan-content-hl"'))
print("inv-content-mf pos:", c.find('id="inv-content-mf"'))
