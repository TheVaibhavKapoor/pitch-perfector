with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('homeLoanModal')
if idx != -1:
    print(text[idx-50:idx+200])
else:
    print("Not found")
