import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
# We want to grab from <!-- Send Deck Modal --> to the end of the script or modals
pos_send = content.find("<!-- Send Deck Modal -->")
pos_end = content.find("<!-- END MODALS -->")
if pos_send != -1 and pos_end != -1:
    with open("etb_modals.txt", "w", encoding="utf-8") as out:
        out.write(content[pos_send : pos_end + len("<!-- END MODALS -->")])
    print("Wrote etb_modals.txt")
else:
    print(f"Could not find markers: pos_send={pos_send}, pos_end={pos_end}")
