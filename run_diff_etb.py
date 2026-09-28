import os, difflib

f_sol = r"customer_overview_solitaire.html"
f_prv = r"customer_overview_privy.html"


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


sol = get_content(f_sol).splitlines()
prv = get_content(f_prv).splitlines()

diff = difflib.unified_diff(
    prv, sol, fromfile="privy_etb", tofile="solitaire_etb", lineterm=""
)
with open("etb_diff.txt", "w", encoding="utf-8") as out:
    for line in diff:
        out.write(line + "\n")
print("Diff written to etb_diff.txt")
