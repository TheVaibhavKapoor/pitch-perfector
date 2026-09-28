with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()
print('Has sparkle emoji:', '\u2728' in text)
print('Has house emoji:', '\U0001F3E0' in text)
print('Has ?? string:', '??' in text)
