import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def inspect_file(fpath):
    print(f"\nInspecting {fpath}...")
    content = get_content(fpath)
    # Search for compare-modal, send-deck-modal, create-lead-modal
    for modal_id in ["compare-modal", "send-deck-modal", "create-lead-modal"]:
        idx = content.find(f'id="{modal_id}"')
        if idx != -1:
            # print surrounding 100 chars
            context = content[idx - 100 : idx + 200]
            print(f"  Found {modal_id} at index {idx}: {repr(context)}")
        else:
            print(f"  {modal_id} NOT found!")


inspect_file("customer_overview_solitaire.html")
inspect_file("experience_solitaire_dashboard_new.html")
inspect_file("experience_solitaire_dashboard.html")
