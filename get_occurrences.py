import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
lines = content.split("\n")
with open("solitaire_privy_occurrences.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "privy" in line.lower():
            out.write(f"Line {i+1}: {line.strip()}\n")
print("Wrote solitaire_privy_occurrences.txt")
