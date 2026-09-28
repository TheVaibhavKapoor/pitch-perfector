import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

for fname in ["experience_solitaire_dashboard_new.html", "customer_overview_solitaire.html"]:
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    
    pos_compare = c.find('id="compare-modal"')
    pos_send = c.find('id="send-deck-modal"')
    
    # Print 200 chars before send-deck-modal
    print(f"Context before send-deck-modal (pos {pos_send}):")
    print(c[pos_send-300:pos_send])
