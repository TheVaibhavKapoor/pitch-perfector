import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
matches = re.findall(r'href=["\']([^"\']*)["\']', content, re.IGNORECASE)
print("Href targets found:")
for m in set(matches):
    print(f"  {m}")
