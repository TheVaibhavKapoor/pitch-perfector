import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
print(f"File length: {len(content)}")
print(f"send-deck-modal found: {content.find('send-deck-modal')}")
print(f"create-lead-modal found: {content.find('create-lead-modal')}")
