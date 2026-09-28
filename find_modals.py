import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
# search for definitions: id="send-deck-modal" or id='send-deck-modal'
for modal_id in [
    'id="send-deck-modal"',
    "id='send-deck-modal'",
    'id="create-lead-modal"',
    "id='create-lead-modal'",
]:
    pos = content.find(modal_id)
    print(f"{modal_id} position: {pos}")
    if pos != -1:
        # print 500 chars around it
        print(content[pos - 50 : pos + 500])
        print("-" * 50)
