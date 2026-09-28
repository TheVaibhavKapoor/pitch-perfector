import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
depth = 0
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    depth += oc - cc
    if i >= 1295 and i <= 1350 and (oc > 0 or cc > 0):
        print(f'L{i} d={depth} (+{oc}/-{cc}): {repr(line[:100])}')
