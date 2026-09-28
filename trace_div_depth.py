import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def trace_divs(fname):
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    pos_comp = c.find('id="compare-modal"')
    pos_send = c.find('id="send-deck-modal"')
    
    comp_block = c[pos_comp:pos_send]
    
    # find all div tags
    tags = re.findall(r'</?div[^>]*>', comp_block, re.IGNORECASE)
    depth = 0
    for t in tags:
        if t.startswith('</div'):
            depth -= 1
        else:
            depth += 1
        print(f"Depth {depth:2d}: {t[:60]}")

trace_divs("experience_solitaire_dashboard_new.html")
trace_divs("customer_overview_solitaire.html")
