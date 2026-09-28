import glob
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        if 'panel-business-cc' in f.read():
            print(f'Found in {file}')
