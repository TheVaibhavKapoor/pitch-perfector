import re, codecs

def print_panels(filepath):
    print(f'=== All Panel Header Lines in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, start=1):
        if 'class="info-panel' in line or 'id="panel-' in line:
            print(f'  Line {i}: {line.strip()}')

print_panels('experience_solitaire_dashboard_new.html')
print()
print_panels('experience_solitaire_dashboard.html')
