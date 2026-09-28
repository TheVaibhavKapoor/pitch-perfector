import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print('Lines 1008-1055:')
for i in range(1007, min(len(lines), 1055)):
    print(f'{i+1}: {repr(lines[i][:100])}')
