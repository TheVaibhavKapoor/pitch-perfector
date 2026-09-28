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
    
    # Check all modal divs
    for mid in ["send-deck-modal", "create-lead-modal", "compare-modal", "disposition-modal"]:
        idx = c.find(f'id="{mid}"')
        if idx != -1:
            print(f"\n--- Found id=\"{mid}\" at index {idx} ---")
            print(c[idx-50:idx+350])
        else:
            print(f"\n--- id=\"{mid}\" NOT FOUND ---")

