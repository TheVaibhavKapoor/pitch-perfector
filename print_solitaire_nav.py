import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


solitaire = get_content("customer_overview_solitaire.html")
lines = solitaire.splitlines()
with open("solitaire_nav_print.txt", "w", encoding="utf-8") as out:
    for idx in range(70, 160):
        if idx < len(lines):
            out.write(f"{idx+1}: {lines[idx]}\n")
print("Wrote solitaire_nav_print.txt")
