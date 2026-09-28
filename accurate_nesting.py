import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def analyze_modal_structure(fname):
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    
    # Find all modal divs
    modals = ["compare-modal", "send-deck-modal", "create-lead-modal"]
    for mid in modals:
        pos = c.find(f'id="{mid}"')
        if pos == -1:
            print(f"Modal {mid} NOT FOUND!")
            continue
            
        # Find where this modal ends by matching div tags
        depth = 0
        end_pos = -1
        # scan from pos
        i = pos
        # find the <div id="mid" ... >
        div_start = c.rfind('<div', 0, pos)
        
        # let's iterate through tags from div_start
        tokens = re.finditer(r'</?div[\s>]', c[div_start:], re.IGNORECASE)
        for t in tokens:
            tag = t.group(0).lower()
            if tag.startswith('<div'):
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end_pos = div_start + t.end()
                    break
                    
        print(f"Modal '{mid}': starts at {div_start}, ends at {end_pos}")
        
        # Check if other modals are inside [div_start, end_pos]
        for other in modals:
            if other != mid:
                opos = c.find(f'id="{other}"')
                if div_start <= opos <= end_pos:
                    print(f"  🚨 '{other}' (pos {opos}) IS INSIDE '{mid}'!")
                else:
                    print(f"  '{other}' is OUTSIDE '{mid}'.")

analyze_modal_structure("experience_solitaire_dashboard_new.html")
analyze_modal_structure("customer_overview_solitaire.html")
