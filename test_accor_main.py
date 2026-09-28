with open('solitaire_cc.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx1 = text.find('Accor')
idx2 = text.find('</main>')
print(f"Accor at {idx1}, </main> at {idx2}")
