import glob
for file in glob.glob('*.html'):
    if 'temp' in file or 'solitaire_cc' in file or 'new' in file or file == 'experience_solitaire_dashboard.html':
        continue
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        if '</main>' in text:
            print(f"Found </main> in {file}")
