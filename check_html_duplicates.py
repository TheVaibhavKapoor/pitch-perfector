import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")
# There are TWO html content blocks - the file has duplicate HTML!
# Let's check how many <!DOCTYPE html> there are
import re
doctype_positions = [m.start() for m in re.finditer('<!DOCTYPE html>', c, re.IGNORECASE)]
html_end_positions = [m.start() for m in re.finditer('</html>', c, re.IGNORECASE)]
print(f"DOCTYPE positions: {doctype_positions}")
print(f"</html> positions: {html_end_positions}")
print(f"Total length: {len(c)}")
