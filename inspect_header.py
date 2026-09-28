import sys, re

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
pos_header = c.find('<header')
if pos_header != -1:
    pos_header_end = c.find('</header>', pos_header)
    print("=== HEADER CONTENT ===")
    print(c[pos_header:pos_header_end+10])
