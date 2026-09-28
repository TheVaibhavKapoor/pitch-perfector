import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Find the end of CC panel (right before panel-assets)
    pa_pos = text.find('id="panel-assets"')
    
    # Look at the context before panel-assets
    ctx = text[pa_pos-600:pa_pos]
    print(f'{filename}:')
    print('Context before panel-assets:')
    print(repr(ctx[-300:]))
    print()

fix_file('experience_solitaire_dashboard_new.html')
fix_file('experience_solitaire_dashboard.html')
