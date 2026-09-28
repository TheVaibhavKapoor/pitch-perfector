with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('<main')
if idx != -1:
    print(text[idx:idx+100])
else:
    print("Not found")
