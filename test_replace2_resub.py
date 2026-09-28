with open('replace_panels2.py', 'r', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
for line in lines:
    if 're.sub' in line:
        print(line)
