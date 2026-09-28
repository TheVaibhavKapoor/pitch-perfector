import codecs

for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace('? FEATURED', '&#11088; FEATURED')
    text = text.replace('?? CALCULATE', '&#129358; CALCULATE')
    text = text.replace('? CALCULATE', '&#129358; CALCULATE')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed hero badge emojis in {filepath}")
