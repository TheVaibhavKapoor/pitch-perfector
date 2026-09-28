import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


# NTB file length is 198255 but </html> is at 173101 — 25K chars after </html>!
# Those 25K chars are the injected modals + scripts that are OUTSIDE the HTML document!
# Browsers may ignore content after </html>, so the modals don't exist in the DOM.

c = get_content("experience_solitaire_dashboard_new.html")
html_end = c.find('</html>')
print(f"File length: {len(c)}, </html> at: {html_end}")
print(f"\nContent after </html> (first 200 chars):")
print(c[html_end+7:html_end+300])
