import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
print(f"File length: {len(content)}")
matches = list(re.finditer(r"<script", content, re.IGNORECASE))
print(f"Found {len(matches)} <script tags:")
for i, m in enumerate(matches):
    start = m.start()
    print(f"  Tag {i+1} at position {start}: {content[start:start+100]}")
