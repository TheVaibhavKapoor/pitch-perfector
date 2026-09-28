import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
lines = content.split("\n")
with open("solitaire_tail.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(lines[-150:]))
print("Wrote solitaire_tail.txt")
