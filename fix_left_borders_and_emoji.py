import codecs

for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    print(f'=== Fixing left borders & emoji in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove border-left from feature-cards
    text = text.replace('<div class="feature-card" style="border-left: 4px solid #1e3a8a;">', '<div class="feature-card">')

    # 2. Fix tennis ball emoji to calculator emoji HTML entity
    text = text.replace('?? CALCULATE', '&#129358; CALCULATE')
    text = text.replace('? CALCULATE', '&#129358; CALCULATE')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done in {filepath}')
