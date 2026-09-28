import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
lines = content.split("\n")
with open("calculator_section.txt", "w", encoding="utf-8") as out:
    for idx in range(660, 720):
        if idx < len(lines):
            out.write(f"{idx+1}: {lines[idx]}\n")
print("Wrote calculator_section.txt")
