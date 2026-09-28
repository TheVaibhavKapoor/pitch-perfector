import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")

# Find compare-modal opening
pos_start = c.find('<div id="compare-modal"')
print(f"compare-modal starts at: {pos_start}")

# Find the END MODALS comment or where the compare modal section finishes
# Let's check what's between compare-modal and the send-deck (which is apparently missing)
# Check if send-deck-modal is somewhere
pos_send = c.find('send-deck-modal')
print(f"send-deck-modal mention at: {pos_send}")
print(f"Context around pos_send: {c[pos_send-100:pos_send+300]}")
