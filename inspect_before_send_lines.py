import sys
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

for fname in ["experience_solitaire_dashboard_new.html", "customer_overview_solitaire.html"]:
    c = get(fname)
    print(f"\n==================== {fname} ====================")
    
    pos_send = c.find('id="send-deck-modal"')
    # print 30 lines before pos_send
    lines = c[:pos_send].split('\n')
    for idx, l in enumerate(lines[-25:]):
        print(f"Line {len(lines)-25+idx}: {l}")
