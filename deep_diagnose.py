import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


# Deep inspect - check if modals are nested inside other modals (the real issue)
for fname in ["customer_overview_solitaire.html", "experience_solitaire_dashboard_new.html"]:
    c = get_content(fname)
    print(f"\n=== {fname} ===")

    # Find positions of key elements
    pos_compare = c.find('<div id="compare-modal"')
    pos_send    = c.find('<div id="send-deck-modal"')
    pos_create  = c.find('<div id="create-lead-modal"')
    pos_html_end = c.find('</html>')
    pos_body_end = c.find('</body>')

    print(f"compare-modal pos:    {pos_compare}")
    print(f"send-deck-modal pos:  {pos_send}")
    print(f"create-lead-modal pos:{pos_create}")
    print(f"</body> pos:          {pos_body_end}")
    print(f"</html> pos:          {pos_html_end}")
    print(f"file length:          {len(c)}")

    # Check if modals are AFTER </html> (common issue - appended outside html)
    if pos_send != -1:
        print(f"send-deck-modal after </html>: {pos_send > pos_html_end}")
    if pos_create != -1:
        print(f"create-lead-modal after </html>: {pos_create > pos_html_end}")

    # Check if modals are inside compare-modal
    # Rough check - is send-deck between compare start and compare end?
    if pos_compare != -1 and pos_send != -1:
        # Find compare-modal end by looking for its closing div
        seg = c[pos_compare:]
        depth = 0
        ci = 0
        while ci < len(seg):
            if seg[ci:ci+4] == '<div':
                depth += 1
                ci += 4
            elif seg[ci:ci+6] == '</div>':
                depth -= 1
                if depth == 0:
                    compare_end = pos_compare + ci + 6
                    break
                ci += 6
            else:
                ci += 1
        else:
            compare_end = -1
        print(f"compare-modal end pos: {compare_end}")
        if compare_end > 0 and pos_send != -1:
            print(f"send-deck INSIDE compare-modal: {pos_compare < pos_send < compare_end}")
        if compare_end > 0 and pos_create != -1:
            print(f"create-lead INSIDE compare-modal: {pos_compare < pos_create < compare_end}")

    # Check ntb-modal-overlay style - display none or flex?
    style_match = re.search(r'\.ntb-modal-overlay\s*\{([^}]+)\}', c)
    if style_match:
        print(f"ntb-modal-overlay style: {style_match.group(1).strip()[:100]}")

    # Check the send-deck-modal style attribute
    sdm_match = re.search(r'<div id="send-deck-modal"([^>]+)>', c)
    if sdm_match:
        print(f"send-deck-modal opening tag attrs: {sdm_match.group(1)[:120]}")
    clm_match = re.search(r'<div id="create-lead-modal"([^>]+)>', c)
    if clm_match:
        print(f"create-lead-modal opening tag attrs: {clm_match.group(1)[:120]}")
