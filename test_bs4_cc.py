with open('solitaire_cc.html', 'r', encoding='utf-8') as f:
    text = f.read()
print('literal id="panel-cc":', 'id="panel-cc"' in text)
