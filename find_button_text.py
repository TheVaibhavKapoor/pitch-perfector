import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
lines = content.split("\n")
print("Occurrences containing 'benefit':")
for i, line in enumerate(lines):
    if "benefit" in line.lower() or "overall" in line.lower():
        print(f"Line {i+1}: {line.strip()[:120]}")
