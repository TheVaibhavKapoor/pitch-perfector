import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

for fname in ["experience_solitaire_dashboard_new.html", "customer_overview_solitaire.html"]:
    c = get(fname)
    print(f"=== {fname} ===")
    print("File length:", len(c))
    
    # Find header buttons
    btns = re.findall(r'<button[^>]*>.*?</button>', c, re.DOTALL)
    for b in btns:
        if any(w in b for w in ["Send Deck", "Disposition", "Compare", "Lead"]):
            print("  BUTTON:", repr(b.replace('\n', ' ')))
            
    # Find modal divs
    print("  div id=send-deck-modal:", 'id="send-deck-modal"' in c)
    print("  div id=create-lead-modal:", 'id="create-lead-modal"' in c)
    print("  div id=compare-modal:", 'id="compare-modal"' in c)
    
    # Check openSendDeckModal and openDispositionModal definitions
    print("  openSendDeckModal in file:", 'openSendDeckModal' in c)
    print("  openDispositionModal in file:", 'openDispositionModal' in c)
