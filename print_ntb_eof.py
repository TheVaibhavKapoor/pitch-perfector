import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
print(f"File length: {len(content)}")
lines = content.splitlines()
print(f"Total lines: {len(lines)}")
for idx in range(len(lines) - 20, len(lines)):
    print(f"{idx+1}: {lines[idx]}")
