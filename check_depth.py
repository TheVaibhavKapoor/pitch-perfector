import glob

def check_divs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    depth = 0
    for i, line in enumerate(lines):
        opens = line.count('<div')
        closes = line.count('</div')
        depth += opens - closes
    print(f"{filepath}: final depth = {depth}")

check_divs('experience_solitaire_dashboard.html')
check_divs('experience_solitaire_dashboard_new.html')
check_divs('experience_solitaire_dashboard_v1.html')
