import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")

# Find all mentions of 'send-deck-modal'
import re
for m in re.finditer('send-deck-modal', c):
    pos = m.start()
    print(f"pos {pos}: {c[pos-50:pos+150]}")
    print("---")
