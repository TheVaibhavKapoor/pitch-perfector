import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Track div nesting and find where it goes wrong
depth = 0
lines = text.split('\n')
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    depth += opens - closes
    if depth < 0 or (i > 1330 and i < 1345):
        print(f'Line {i}: depth={depth} opens={opens} closes={closes} | {repr(line[:100])}')
    if depth < -2:
        break
