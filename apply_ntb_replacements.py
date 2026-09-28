import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")

replacements = [
    ("Privy League", "Solitaire"),
    ("Privy Business", "Solitaire Business"),
    ("Privy Debit Card", "Solitaire Debit Card"),
    ("Privy Credit Card", "Solitaire Infinite Credit Card"),
    ("Privy Advantage", "Solitaire Advantage"),
    ("Privy proposition", "Solitaire proposition"),
    ("Privy relationship", "Solitaire relationship"),
    ("Privy Preferential Rate", "Solitaire Preferential Rate"),
    ("Privy Monthly EMI", "Solitaire Monthly EMI"),
    ("totalInterestPrivy", "totalInterestSolitaire"),
    ("emiPrivy", "emiSolitaire"),
    ("rPrivy", "rSolitaire"),
    ("designed for Privy members", "designed for Solitaire members"),
    ("Privy exclusive", "Solitaire exclusive"),
    ("with Privy", "with Solitaire"),
    ("Privy-linked", "Solitaire-linked"),
    ("Cloud Bank Privy", "Cloud Bank Solitaire"),
    ("Kotak Privy Program", "Kotak Solitaire Program"),
    ("Kotak Privy Business Credit Card", "Kotak Solitaire Business Credit Card"),
    ("Personal Loan (Privy)", "Personal Loan (Solitaire)"),
    ("All Privy Loan Products", "All Solitaire Loan Products"),
    ("Nil charges with Privy Program", "Nil charges with Solitaire Program"),
    ("🟢 Privy → AIR", "🟢 Solitaire → Solitaire Infinite"),
    (
        "for your Privy relationship, we also have the Kotak Air Credit Card.",
        "for your Solitaire relationship, we have the Solitaire Infinite Credit Card.",
    ),
    (
        "So if your objective is to get a straightforward travel card with lounge access and earn Air Miles on your regular spends, this is a good fit within the Privy proposition.",
        "So if your objective is to get an ultra-premium travel card with unlimited lounge access and earn accelerated Air Miles on your regular spends, this is a perfect fit.",
    ),
    (
        "Kotak Privy is a premium banking programme",
        "Kotak Solitaire is the elite, invitation-only banking programme",
    ),
    (
        "linked to Privy CA variant (Ace Variant)",
        "linked to Solitaire CA variant (Ace Variant)",
    ),
    ("// Kotak Privy (10 RP", "// Kotak Solitaire (10 RP"),
]

new_content = content
for old, new in replacements:
    new_content = new_content.replace(old, new)

# Write the file back with same encoding (try utf-8 or utf-16 depending on original)
try:
    # check original encoding
    open("experience_solitaire_dashboard_new.html", "r", encoding="utf-16").read()
    with open(
        "experience_solitaire_dashboard_new.html", "w", encoding="utf-16"
    ) as out:
        out.write(new_content)
    print("Wrote experience_solitaire_dashboard_new.html as UTF-16")
except Exception:
    with open(
        "experience_solitaire_dashboard_new.html", "w", encoding="utf-8"
    ) as out:
        out.write(new_content)
    print("Wrote experience_solitaire_dashboard_new.html as UTF-8")
