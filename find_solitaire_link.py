import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
lines = content.split("\n")
print("Occurrences of solitaire.html:")
for i, line in enumerate(lines):
    if "solitaire.html" in line.lower():
        print(f"Line {i+1}: {line.strip()}")
