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
    if i >= 1380 and i <= 1410 and (oc > 0 or cc > 0):
        print(f'Line {i} depth={depth} (+{oc}/-{cc}): {repr(line[:100])}')
