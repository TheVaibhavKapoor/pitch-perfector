import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
matches = list(re.finditer(r"compare-modal|comparisonModal", content, re.IGNORECASE))
print(f"Found {len(matches)} matches in experience_solitaire_dashboard_new.html:")
for i, m in enumerate(matches):
    start = m.start()
    print(f"Match {i+1} at position {start}: {content[start-50:start+150]}")
