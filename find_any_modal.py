import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")
# find all occurrences of 'modal' in the file
matches = re.finditer(
    r'id=["\']([^"\']*modal[^"\']*)["\']|class=["\']([^"\']*modal[^"\']*)["\']',
    content,
    re.IGNORECASE,
)
print("Modal occurrences in customer_overview_solitaire.html:")
for m in matches:
    print(f"Match: {m.group(0)} at position {m.start()}")
