with open('update_all_products_grid.py', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('Air India')
if idx != -1:
    print(repr(text[idx-50:idx+50]))
else:
    print("Not found")
