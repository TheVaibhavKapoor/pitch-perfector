import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


for f in [
    "customer_overview.html",
    "customer_overview_privy.html",
    "customer_overview_solitaire.html",
    "experience_privy_dashboard.html",
    "experience_solitaire_dashboard.html",
]:
    c = get_content(f)
    title = re.search(r"<title>(.*?)</title>", c)
    title_text = title.group(1) if title else "NONE"
    print(f"{f}: title='{title_text}', len={len(c)}")
