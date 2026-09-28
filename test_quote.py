with open('solitaire_cc.html', 'r', encoding='utf-8') as f:
    text = f.read()
print("Has '''?", "'''" in text)
