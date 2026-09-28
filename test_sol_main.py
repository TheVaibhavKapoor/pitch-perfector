with open('solitaire_cc.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('</main>')
if idx != -1:
    print(repr(text[idx-50:idx+50]))
else:
    print("Not found")
