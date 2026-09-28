import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
print(f"File length: {len(content)}")
for target in ["send-deck-modal", "create-lead-modal"]:
    print(f"Occurrences of {target}:")
    for m in re.finditer(re.escape(target), content):
        start = m.start()
        print(f"  Found at {start}: {content[start-50:start+150]}")
