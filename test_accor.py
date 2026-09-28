with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()
print('Accor occurrences:', text.count('Accor Point ='))
