import re

for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Standardize Loans product card writeups
    text = text.replace('<span class="product-subtitle">Premium Lending</span>', '<span class="product-subtitle">Asset-Backed Lending</span>')
    text = text.replace('<span class="product-timestamp">Bespoke borrowing solutions</span>', '<span class="product-timestamp">Bespoke borrowing &amp; credit solutions</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Standardized Loans card writeup in {filepath}")
