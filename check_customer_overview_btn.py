import os

def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()

c = get_content("customer_overview_solitaire.html")
# Find the create lead button
import re
matches = list(re.finditer(r'onclick.*?(?:Disposition|Create Lead)</button>', c))
for m in matches:
    print(repr(m.group(0)[:200]))
    print()
