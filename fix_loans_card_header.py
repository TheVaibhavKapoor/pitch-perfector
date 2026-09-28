import codecs

for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    print(f'=== Fixing Loans card title & writeup in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace('<h3 class="product-title">Home Loan</h3>', '<h3 class="product-title">Loans</h3>')
    text = text.replace('<span class="product-timestamp">7.50% Solitaire vs 7.80% Normal Rate</span>', '<span class="product-timestamp">Bespoke borrowing &amp; credit solutions</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done in {filepath}')
