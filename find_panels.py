import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_privy_dashboard_new.html")
matches = re.finditer(r'id=["\']panel-([^"\']+)["\']', content)
print("Panels in experience_privy_dashboard_new.html:")
for m in matches:
    name = m.group(1)
    pos = m.start()
    print(f"- {name} at position {pos}")
