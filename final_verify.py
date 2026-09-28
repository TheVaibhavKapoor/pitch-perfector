import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

for fname in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f'=== {fname} ===')
    
    # Check all panels have content
    panel_ids = ['panel-dc', 'panel-cc', 'panel-assets', 'panel-investments', 'panel-forex', 'panel-other']
    for pid in panel_ids:
        start = text.find(f'id="{pid}"')
        next_panel_pos = min([text.find(f'id="{p}"') for p in panel_ids if text.find(f'id="{p}"') > start] or [len(text)])
        content = text[start:next_panel_pos]
        # Count feature-cards in this panel
        fc_count = content.count('feature-card')
        h2_count = content.count('<h2 ')
        print(f'  {pid}: h2={h2_count}, feature-cards={fc_count}')
    
    # Check rupee symbol is correct
    question_marks = len(re.findall(r'\?(?=\d)', text))
    rupee_count = text.count('\u20b9')
    print(f'  Rupee (?): {rupee_count}, Broken ?: {question_marks}')
    
    # Ensure active card is CC (so it shows on load)
    active_cc = 'product-card active' in text and 'showPanel(\'cc\'' in text
    print(f'  CC active on load: {active_cc}')
    print()
