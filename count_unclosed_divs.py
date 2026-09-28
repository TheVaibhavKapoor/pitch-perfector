import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def count_divs(fname):
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    
    pos_comp = c.find('id="compare-modal"')
    pos_send = c.find('id="send-deck-modal"')
    
    block = c[pos_comp:pos_send]
    
    opens = []
    closes = []
    
    # find positions of <div and </div>
    for m in re.finditer(r'(</?div[\s>])', block, re.IGNORECASE):
        is_close = m.group(1).lower().startswith('</div')
        pos = pos_comp + m.start()
        line_num = c[:pos].count('\n') + 1
        snippet = block[m.start():m.start()+40].replace('\n', ' ')
        if is_close:
            closes.append((line_num, snippet))
        else:
            opens.append((line_num, snippet))
            
    print(f"Total <div opened: {len(opens)}")
    print(f"Total </div> closed: {len(closes)}")
    print(f"Difference (unclosed divs): {len(opens) - len(closes)}")
    
    # Let's print all unclosed divs if any
    depth = 0
    stack = []
    for m in re.finditer(r'(</?div[\s>])', block, re.IGNORECASE):
        is_close = m.group(1).lower().startswith('</div')
        pos = pos_comp + m.start()
        line_num = c[:pos].count('\n') + 1
        snippet = block[m.start():m.start()+50].replace('\n', ' ')
        if not is_close:
            stack.append((line_num, snippet))
        else:
            if stack:
                stack.pop()
                
    print("\nUnclosed divs remaining at end of block:")
    for line_num, snippet in stack:
        print(f"  Line {line_num}: {snippet}")

count_divs("experience_solitaire_dashboard_new.html")
count_divs("customer_overview_solitaire.html")
