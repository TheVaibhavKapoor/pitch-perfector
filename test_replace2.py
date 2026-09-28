with open('replace_panels2.py', 'r', encoding='utf-8') as f:
    text = f.read()
if '</main>' in text:
    print('Found in replace_panels2.py!!')
