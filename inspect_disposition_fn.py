import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("customer_overview_solitaire.html")
# Grep for sidebarCustName in UTF-8 version
print(f"'sidebarCustName' in file: {'sidebarCustName' in c}")
# Look for openDispositionModal function
pos = c.find("openDispositionModal")
print(f"\nopenDispositionModal at pos: {pos}")
if pos != -1:
    print(c[pos:pos+800])
