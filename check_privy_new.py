import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_privy_dashboard_new.html")
print(f"File length: {len(content)}")
lines = content.split("\n")
print("Occurrences containing 'modal':")
count = 0
for i, line in enumerate(lines):
    if "modal" in line.lower():
        print(f"Line {i+1}: {line.strip()[:100]}")
        count += 1
        if count >= 30:
            break
