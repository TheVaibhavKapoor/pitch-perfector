import re, codecs

def fix_dashboard_file(filepath):
    print(f'*** Auditing & fixing structural panel flow in {filepath} ***')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up broken panel start tags
    content = re.sub(r'</div>\s*<div id="panel-assets"', r'</div>\n                <div id="panel-assets"', content)
    content = re.sub(r'\s*id="panel-investments"\s*class="info-panel"\s*>', r'\n                <div id="panel-investments" class="info-panel">', content)
    content = re.sub(r'\s*id="panel-forex"\s*class="info-panel"\s*>', r'\n                <div id="panel-forex" class="info-panel">', content)
    content = re.sub(r'\s*id="panel-forex"\s*>', r'\n                <div id="panel-forex" class="info-panel">', content)
    content = re.sub(r'\s*id="panel-business-assets"\s*class="info-panel"\s*(&gt;|>)?', r'\n                <div id="panel-business-assets" class="info-panel">', content)

    # 2. Fix premature closure of panel-cc before reward-calculator
    # In NTB or ETB: panel-cc starts with <div ... id="panel-cc"...>
    # then feature cards, then reward-calculator.
    # We ensure reward-calculator is inside panel-cc, and panel-cc closes right before panel-assets.

    # 3. Clean up Loan card rainbow colors to elegant Solitaire Navy Blue (#1e3a8a)
    content = content.replace('border-left: 4px solid #8b5cf6;', 'border-left: 4px solid #1e3a8a;')
    content = content.replace('border-left: 4px solid #f59e0b;', 'border-left: 4px solid #1e3a8a;')
    content = content.replace('border-left: 4px solid #06b6d4;', 'border-left: 4px solid #1e3a8a;')
    content = content.replace('border-left: 4px solid #10b981;', 'border-left: 4px solid #1e3a8a;')
    content = content.replace('color: #8b5cf6;', 'color: #1e3a8a;')
    content = content.replace('color: #f59e0b;', 'color: #1e3a8a;')
    content = content.replace('color: #06b6d4;', 'color: #1e3a8a;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated panel tags and colors in {filepath}')

fix_dashboard_file('experience_solitaire_dashboard_new.html')
fix_dashboard_file('experience_solitaire_dashboard.html')
