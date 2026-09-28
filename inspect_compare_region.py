import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")
# Get surrounding context near where compare-modal ends / send-deck-modal should be
# The compare-modal is at 151103. Let's look at area around 149084 (style) and after the compare modal
# Grab 200 chars around position 151103
pos = 151103
segment = c[pos:pos+3000]
# Print lines from this to find where it closes
lines = segment.split("\n")
with open("compare_region.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(lines[:80]):
        f.write(f"{i}: {line}\n")
print("Wrote compare_region.txt")
