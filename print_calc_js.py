import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
lines = content.split("\n")
with open("calc_js.txt", "w", encoding="utf-8") as out:
    for idx in range(1780, 1830):
        out.write(f"{idx+1}: {lines[idx]}\n")
    out.write("\n" + "=" * 50 + "\n")
    for idx in range(2480, 2530):
        out.write(f"{idx+1}: {lines[idx]}\n")
print("Wrote calc_js.txt")
