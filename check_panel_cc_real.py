import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

for filename in ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    print(filename, 'panel-cc in text:', 'panel-cc' in text)
    matches = re.finditer(r'<div[^>]*id=\"panel-cc\"[^>]*>', text)
    for m in matches:
        print(filename, 'Match:', m.group(0))
