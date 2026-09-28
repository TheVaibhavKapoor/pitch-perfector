import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
lines = content.split("\n")
with open("solitaire_buttons.txt", "w", encoding="utf-8") as out:
    for idx in range(165, 205):
        if idx < len(lines):
            out.write(f"{idx+1}: {lines[idx]}\n")
print("Wrote solitaire_buttons.txt")
