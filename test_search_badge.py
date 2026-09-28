with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Has featured-badge?', 'featured-badge' in text)
