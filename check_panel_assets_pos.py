import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

for fname in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    main_close = text.find('</main>')
    panel_assets = text.find('id="panel-assets"')
    
    print(f'{fname}:')
    print(f'  </main> at: {main_close}')
    print(f'  panel-assets at: {panel_assets}')
    print(f'  panel-assets is AFTER </main>: {panel_assets > main_close}')
    print()
