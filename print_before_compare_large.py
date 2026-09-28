import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
pos = content.find("compare-modal")
with open("before_compare.txt", "w", encoding="utf-8") as out:
    out.write(content[pos - 1500 : pos])
print("Wrote before_compare.txt")
