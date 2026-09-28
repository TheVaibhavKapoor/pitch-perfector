import re
import sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

files = ['home_loan_calculator.html', 'customer_overview.html', 'experience_solitaire.html']
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    for i, line in enumerate(content.splitlines(), 1):
        if '?' in line:
            clean = line.strip()
            # Filter out obvious non-rupee patterns
            if not re.search(r'css2\?family|selectedIndex\]\?|=== .* \? |m === mode \? |type === .* \? |points\?`|savings\?|const.*\?.*:|return.*\?.*:', clean):
                print(f'{fname}:{i}: {clean[:120]}')
