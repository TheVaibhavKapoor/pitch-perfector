import re, codecs

def fix_dashboard(filepath):
    print(f'=== Fixing {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix broken panel opening tags where '<div ' is missing or corrupted
    # Fix id="panel-investments"
    html = re.sub(r'(\s*)id="panel-investments"\s*class="info-panel"\s*>', r'\1<div id="panel-investments" class="info-panel">', html)
    # Fix id="panel-forex"
    html = re.sub(r'(\s*)id="panel-forex"\s*class="info-panel"\s*>', r'\1<div id="panel-forex" class="info-panel">', html)
    html = re.sub(r'(\s*)id="panel-forex"\s*>', r'\1<div id="panel-forex" class="info-panel">', html)
    # Fix id="panel-business-assets"
    html = re.sub(r'(\s*)id="panel-business-assets"\s*class="info-panel"\s*(&gt;|>)?', r'\1<div id="panel-business-assets" class="info-panel">', html)

    # 2. Harmonize loan card colors to Solitaire brand navy blue (#1e3a8a)
    html = html.replace('border-left: 4px solid #8b5cf6;', 'border-left: 4px solid #1e3a8a;')
    html = html.replace('border-left: 4px solid #f59e0b;', 'border-left: 4px solid #1e3a8a;')
    html = html.replace('border-left: 4px solid #06b6d4;', 'border-left: 4px solid #1e3a8a;')
    html = html.replace('border-left: 4px solid #10b981;', 'border-left: 4px solid #1e3a8a;')
    
    # Also harmonize inner strong rate tag colors to Solitaire blue/navy or emerald green for savings
    html = html.replace('color: #8b5cf6;', 'color: #1e3a8a;')
    html = html.replace('color: #f59e0b;', 'color: #1e3a8a;')
    html = html.replace('color: #06b6d4;', 'color: #1e3a8a;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Successfully updated {filepath}')

fix_dashboard('experience_solitaire_dashboard_new.html')
fix_dashboard('experience_solitaire_dashboard.html')
