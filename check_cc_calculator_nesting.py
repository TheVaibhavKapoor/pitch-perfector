import codecs

def check_nesting(filepath):
    print(f'=== Checking CC & Reward Calculator in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, start=1):
        if 'id="panel-cc"' in line:
            print(f'Line {i}: panel-cc OPEN -> {line.strip()[:60]}')
        if 'id="reward-calculator"' in line:
            print(f'Line {i}: reward-calculator OPEN -> {line.strip()[:60]}')
        if 'id="panel-assets"' in line:
            print(f'Line {i}: panel-assets OPEN -> {line.strip()[:60]}')
        if 'id="panel-investments"' in line:
            print(f'Line {i}: panel-investments OPEN -> {line.strip()[:60]}')

check_nesting('experience_solitaire_dashboard_new.html')
check_nesting('experience_solitaire_dashboard.html')
