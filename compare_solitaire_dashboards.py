import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c1 = get_content("experience_solitaire_dashboard.html")
c2 = get_content("experience_solitaire_dashboard_new.html")
print(f"Lengths: solitaire_dashboard={len(c1)}, solitaire_dashboard_new={len(c2)}")
print(f"Is exact match: {c1 == c2}")
