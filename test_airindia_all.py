import glob
for file in glob.glob('*.py'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        if 'Air India' in f.read():
            print(f'Found in {file}')
for file in glob.glob('*.html'):
    if 'temp' in file or 'solitaire' in file:
        continue
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        if 'Air India' in f.read():
            print(f'Found in HTML: {file}')
