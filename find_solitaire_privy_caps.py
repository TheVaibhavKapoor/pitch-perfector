import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_solitaire_dashboard_new.html")
lines = content.split("\n")

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
]

temp_content = content
for old, new in replacements:
    temp_content = temp_content.replace(old, new)

# find remaining privy occurrences
lines_temp = temp_content.split("\n")
print("Remaining Privy occurrences:")
for i, line in enumerate(lines_temp):
    if "privy" in line.lower():
        # skip comparison modal class/id occurrences
        if any(
            x in line.lower()
            for x in [
                ".col-privy",
                ".cg-privy",
                'class="col-privy"',
                'class="cg-privy"',
                '"cg-privy"',
                '"col-privy"',
                ">privy<",
                ">privy+<",
            ]
        ):
            continue
        print(f"Line {i+1}: {line.strip()[:100]}")
print("End of remaining check")
