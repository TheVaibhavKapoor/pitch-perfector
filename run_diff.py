import os, difflib

f_sol = r"experience_solitaire_dashboard_new.html"
f_prv = r"experience_privy_dashboard_new.html"


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


sol = get_content(f_sol).splitlines()
prv = get_content(f_prv).splitlines()

diff = difflib.unified_diff(
    prv, sol, fromfile="privy", tofile="solitaire", lineterm=""
)
with open("dashboards_diff.txt", "w", encoding="utf-8") as out:
    for line in diff:
        out.write(line + "\n")
print("Diff written to dashboards_diff.txt")
