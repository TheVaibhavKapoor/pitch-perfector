import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")
# Look at what comes before compare-modal to understand the overall page structure
# The compare modal (151103) is INSIDE the main html body
# Let's look at 149000-152000 area
with open("around_compare.txt", "w", encoding="utf-8") as f:
    f.write(c[149000:152500])
print("Wrote around_compare.txt")
