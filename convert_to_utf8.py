import os

# Read as UTF-16
try:
    content = open(
        "customer_overview_solitaire.html", "r", encoding="utf-16"
    ).read()
    print("Read customer_overview_solitaire.html as UTF-16 successfully")
except Exception as e:
    content = open(
        "customer_overview_solitaire.html", "r", encoding="utf-8"
    ).read()
    print("Read customer_overview_solitaire.html as UTF-8")

# Write as UTF-8
with open("customer_overview_solitaire.html", "w", encoding="utf-8") as out:
    out.write(content)

print("Successfully converted customer_overview_solitaire.html to UTF-8")
