import re, codecs

def verify_file(filepath):
    print(f'=== Verifying Panel Isolation in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    panel_ids = ['panel-dc', 'panel-cc', 'panel-assets', 'panel-investments', 'panel-forex', 'panel-other']
    
    positions = []
    for pid in panel_ids:
        # Match <div ... id="pid" or id="pid"
        pattern = r'<div[^>]*id="' + pid + r'"[^>]*>'
        matches = list(re.finditer(pattern, text))
        if not matches:
            print(f'  [ERROR] Tag for {pid} NOT FOUND or broken!')
        else:
            for m in matches:
                positions.append((m.start(), m.end(), pid, m.group(0)))
                print(f'  [OK] {pid} starts at char {m.start()}: {m.group(0)}')

    # Sort positions by start char
    positions.sort(key=lambda x: x[0])
    
    # Check div balance inside each panel range
    for i in range(len(positions)):
        start_char, end_char, pid, full_tag = positions[i]
        next_start = positions[i+1][0] if i+1 < len(positions) else text.find('<!-- Calculate Benefit Button', start_char)
        if next_start == -1:
            next_start = text.find('</main>', start_char)
            
        panel_content = text[start_char:next_start]
        opens = len(re.findall(r'<div[\s>]', panel_content))
        closes = len(re.findall(r'</div>', panel_content))
        print(f'  Panel {pid}: range ({start_char} to {next_start}) | opens={opens}, closes={closes}, net diff={opens-closes}')
        if opens != closes:
            print(f'    [WARNING] Panel {pid} is NOT balanced! diff = {opens-closes}')

verify_file('experience_solitaire_dashboard_new.html')
print()
verify_file('experience_solitaire_dashboard.html')
