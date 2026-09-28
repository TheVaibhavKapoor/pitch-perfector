import codecs

for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace('?? CALCULATE INTEREST SAVINGS', '?? CALCULATE INTEREST SAVINGS')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed emoji encoding in {filepath}")
