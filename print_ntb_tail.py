import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
lines = content.split("\n")
with open("ntb_tail.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(lines[-150:]))
print("Wrote ntb_tail.txt")
