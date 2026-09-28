import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


for fname in ["customer_overview_solitaire.html", "experience_solitaire_dashboard_new.html"]:
    c = get_content(fname)
    print(f"\n=== {fname} ===")
    # Check button labels and onclick
    btn_matches = re.findall(r'<button[^>]*onclick="([^"]+)"[^>]*>([^<]+)</button>', c)
    header_btns = [(onclick, label) for onclick, label in btn_matches
                   if any(x in label for x in ['Compare', 'Send', 'Lead', 'Disposition', 'Reliability'])]
    for onclick, label in header_btns:
        print(f"  Button '{label.strip()}' -> onclick: {onclick[:80]}")

    # Check if functions exist
    for fn in ['openDispositionModal', 'openSendDeckModal', 'handleSendDeck', 'handleDisposition', 'addProductRow']:
        print(f"  {fn} defined: {fn in c}")

    # Check if modal divs exist
    for mid in ['compare-modal', 'send-deck-modal', 'create-lead-modal']:
        print(f"  id=\"{mid}\" div exists: {f'id=\"{mid}\"' in c}")
