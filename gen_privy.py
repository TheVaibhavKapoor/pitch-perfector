import re

with open("experience_solitaire_dashboard.html", "r", encoding="utf-8") as f:
    solitaire_html = f.read()

# For Privy:
privy_html = solitaire_html.replace('Solitaire', 'Privy')
privy_html = privy_html.replace('#d61f26', '#182545') # Change red theme to dark blue
privy_html = privy_html.replace('cloud_bank_logo_red', 'cloud_bank_logo_blue') # if applicable

with open("experience_privy_dashboard.html", "w", encoding="utf-8") as f:
    f.write(privy_html)

# For Privy +:
privy_plus_html = solitaire_html.replace('Solitaire', 'Privy +')
privy_plus_html = privy_plus_html.replace('#d61f26', '#182545')
privy_plus_html = privy_plus_html.replace('cloud_bank_logo_red', 'cloud_bank_logo_blue')

with open("experience_privy_plus_dashboard.html", "w", encoding="utf-8") as f:
    f.write(privy_plus_html)

print("Generated Privy and Privy+ dashboards")
