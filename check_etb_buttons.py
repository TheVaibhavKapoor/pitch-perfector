import os

def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()

c = get_content("customer_overview_solitaire.html")
lines = c.split("\n")

for i, line in enumerate(lines):
    if "create" in line.lower() and "lead" in line.lower():
        print(f"Line {i+1}: {line.strip()[:150]}")
    if "disposition" in line.lower():
        print(f"Line {i+1}: {line.strip()[:150]}")
