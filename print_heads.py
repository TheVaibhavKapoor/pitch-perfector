import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


solitaire = get_content("customer_overview_solitaire.html")
privy = get_content("customer_overview_privy.html")

with open("heads_compare.txt", "w", encoding="utf-8") as out:
    out.write("=== SOLITAIRE HEAD ===\n")
    out.write("\n".join(solitaire.splitlines()[:80]))
    out.write("\n\n=== PRIVY HEAD ===\n")
    out.write("\n".join(privy.splitlines()[:80]))
print("Wrote heads_compare.txt")
