import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import re

files = ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    rupee_count = content.count('\u20b9')
    entity_count = content.count('&#8377;')
    print(f'{fname}: {rupee_count} ₹ + {entity_count} &#8377; entities')
    
    if '? FEATURED' in content:
        print('  WARNING: still has ? FEATURED')
    else:
        print('  OK: ? FEATURED fixed')
    
    js_breaks = re.findall(r"'\? '", content)
    if js_breaks:
        print(f'  WARNING: still has JS broken rupee: {len(js_breaks)}')
    else:
        print('  OK: JS rupee strings fixed')
    
    if 'p.a. ?' in content:
        print('  WARNING: still has p.a. ?')
    else:
        print('  OK: p.a. ? fixed')
