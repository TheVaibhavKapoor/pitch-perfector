import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_privy.html")
lines = content.split("\n")
for i, line in enumerate(lines):
    if "top-header" in line:
        for idx in range(max(0, i - 2), min(len(lines), i + 25)):
            print(f"{idx+1}: {lines[idx]}")
        break
