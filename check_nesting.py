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
    
    # Track div depth starting from compare-modal
    pos_compare = c.find('id="compare-modal"')
    pos_send = c.find('id="send-deck-modal"')
    pos_create = c.find('id="create-lead-modal"')
    
    # Let's parse HTML tags between compare-modal and send-deck-modal
    sub = c[pos_compare:pos_send]
    # count <div and </div>
    open_divs = len(re.findall(r'<div[\s>]', sub, re.IGNORECASE))
    close_divs = len(re.findall(r'</div>', sub, re.IGNORECASE))
    
    print(f"Between compare-modal (pos {pos_compare}) and send-deck-modal (pos {pos_send}):")
    print(f"  <div count: {open_divs}")
    print(f"  </div> count: {close_divs}")
    print(f"  Net open divs before send-deck-modal: {open_divs - close_divs}")
    if open_divs > close_divs:
        print("  🚨 ALERT: send-deck-modal IS INSIDE compare-modal!")
    else:
        print("  send-deck-modal is OUTSIDE compare-modal.")

    sub_create = c[pos_compare:pos_create]
    open_divs_c = len(re.findall(r'<div[\s>]', sub_create, re.IGNORECASE))
    close_divs_c = len(re.findall(r'</div>', sub_create, re.IGNORECASE))
    print(f"Between compare-modal (pos {pos_compare}) and create-lead-modal (pos {pos_create}):")
    print(f"  Net open divs before create-lead-modal: {open_divs_c - close_divs_c}")
    if open_divs_c > close_divs_c:
        print("  🚨 ALERT: create-lead-modal IS INSIDE compare-modal!")
    else:
        print("  create-lead-modal is OUTSIDE compare-modal.")
