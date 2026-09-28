import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Line 849 has a stray </div> before </body>
# Find what's around line 849
lines = text.split('\n')
print('Lines 845-855:')
for i, l in enumerate(lines[844:856], start=845):
    print(f'{i}: {repr(l)}')
