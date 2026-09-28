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

def fix_file(fname):
    c = get(fname)
    print(f"\n==================== Fixing {fname} ====================")
    
    pos_send = c.find('<!-- Send Deck Modal -->')
    if pos_send == -1:
        pos_send = c.find('id="send-deck-modal"')
        pos_send = c.rfind('<div', 0, pos_send)
        
    # Insert an explicit </div> right before <!-- Send Deck Modal -->
    c_fixed = c[:pos_send] + "\n</div> <!-- Explicit close for #compare-modal -->\n\n" + c[pos_send:]
    save(fname, c_fixed)
    print(f"Added closing </div> for #compare-modal in {fname}")

fix_file("experience_solitaire_dashboard_new.html")
fix_file("customer_overview_solitaire.html")
