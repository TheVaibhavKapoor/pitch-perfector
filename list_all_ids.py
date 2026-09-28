import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("customer_overview_solitaire.html")
# Find all ids
ids = re.findall(r'id="([^"]+)"', c)
print("All IDs in customer_overview_solitaire.html:")
for i in sorted(set(ids)):
    print(f"  {i}")
