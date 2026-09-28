import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


for fname in ["customer_overview_solitaire.html", "experience_solitaire_dashboard_new.html"]:
    c = get_content(fname)
    # Find positions of compare-modal div opening and where send-deck-modal is defined
    pos_compare_open = c.find('<div id="compare-modal"')
    pos_send_deck = c.find('<div id="send-deck-modal"')
    pos_create_lead = c.find('<div id="create-lead-modal"')
    # Find the closing of compare-modal
    # Find ntb-modal-overlay style
    pos_style = c.find('.ntb-modal-overlay')
    print(f"\n=== {fname} ===")
    print(f"compare-modal div at pos: {pos_compare_open}")
    print(f"send-deck-modal div at pos: {pos_send_deck}")
    print(f"create-lead-modal div at pos: {pos_create_lead}")
    print(f"ntb-modal-overlay style at pos: {pos_style}")
    # Is send-deck INSIDE compare-modal?
    if pos_compare_open != -1 and pos_send_deck != -1:
        if pos_compare_open < pos_send_deck:
            # Find closing of compare-modal (rough heuristic - look for </div> after compare-modal)
            # Better: find where compare-modal ends
            segment = c[pos_compare_open:]
            depth = 0
            end_pos = pos_compare_open
            i = 0
            while i < len(segment):
                if segment[i:i+4] == '<div':
                    depth += 1
                    i += 4
                elif segment[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        end_pos = pos_compare_open + i + 6
                        break
                    i += 6
                else:
                    i += 1
            print(f"compare-modal ends at approx pos: {end_pos}")
            print(f"send-deck INSIDE compare-modal: {pos_send_deck < end_pos}")
            print(f"create-lead INSIDE compare-modal: {pos_create_lead < end_pos if pos_create_lead != -1 else 'N/A'}")
