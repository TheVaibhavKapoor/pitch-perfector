import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

for fname in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pos = text.find('id="panel-assets"')
    print(f'=== {fname} ===')
    print(text[pos-400:pos])
