import codecs

for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean rupee symbol encoding
    text = text.replace('Loan Amount (?)', 'Loan Amount (&#8377;)')
    text = text.replace('? 1,00,00,000', '&#8377; 1,00,00,000')
    text = text.replace('?10 Lakh', '&#8377;10 Lakh')
    text = text.replace('?5 Crore', '&#8377;5 Crore')
    text = text.replace('? 82,404', '&#8377; 82,404')
    text = text.replace('? 80,559', '&#8377; 80,559')
    text = text.replace('? 1,845 / mo', '&#8377; 1,845 / mo')
    text = text.replace('? 4,42,800', '&#8377; 4,42,800')
    text = text.replace('?97.77 L', '&#8377;97.77 L')
    text = text.replace('?93.34 L', '&#8377;93.34 L')
    text = text.replace('?? SOLITAIRE', '?? SOLITAIRE')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed rupee entities in {filepath}")
