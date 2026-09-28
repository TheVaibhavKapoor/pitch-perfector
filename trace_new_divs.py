import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

depth = 0
lines = text.split('\n')
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    prev = depth
    depth += opens - closes
    if i >= 990 and i <= 1010:
        print(f'Line {i} depth={depth} (+{opens}/-{closes}): {repr(line[:80])}')
