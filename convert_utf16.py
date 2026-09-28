import os

fpath = r"customer_overview_solitaire.html"
try:
    with open(fpath, "r", encoding="utf-16") as f:
        content = f.read()
except Exception:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

with open("current_solitaire_content.txt", "w", encoding="utf-8") as f:
    f.write(content)
print("Done converting solitaire HTML to UTF-8")
