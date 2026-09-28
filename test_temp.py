with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('id="panel-assets"')
if idx != -1:
    print(repr(text[idx-200:idx]))
else:
    print("Not found")
