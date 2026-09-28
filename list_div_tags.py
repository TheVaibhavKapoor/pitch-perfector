import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def list_all_div_tags(fname):
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    
    pos_comp = c.find('id="compare-modal"')
    pos_send = c.find('id="send-deck-modal"')
    
    block = c[pos_comp:pos_send]
    
    depth = 0
    for m in re.finditer(r'</?div[^>]*>', block, re.IGNORECASE):
        tag = m.group(0)
        is_close = tag.lower().startswith('</div')
        pos = pos_comp + m.start()
        line_num = c[:pos].count('\n') + 1
        if is_close:
            depth -= 1
            print(f"Line {line_num:4d} | Depth {depth:2d} | {tag}")
        else:
            print(f"Line {line_num:4d} | Depth {depth:2d} -> {depth+1:2d} | {tag[:50]}")
            depth += 1

list_all_div_tags("customer_overview_solitaire.html")
list_all_div_tags("experience_solitaire_dashboard_new.html")
