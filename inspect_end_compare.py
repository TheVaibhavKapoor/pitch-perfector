import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def inspect_compare_end(fname):
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    
    pos_comp = c.find('id="compare-modal"')
    pos_send = c.find('id="send-deck-modal"')
    
    comp_html = c[pos_comp:pos_send]
    
    # Print the last 600 characters of comp_html
    print("--- Last 600 chars of compare modal block before Send Deck Modal ---")
    print(comp_html[-600:])

inspect_compare_end("experience_solitaire_dashboard_new.html")
inspect_compare_end("customer_overview_solitaire.html")
