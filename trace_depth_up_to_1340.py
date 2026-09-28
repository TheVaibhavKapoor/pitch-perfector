import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

depth = 0
lines = text.split('\n')
# Show depth in final 30 lines before the problem (1340 - 30)
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    depth += opens - closes
    if i >= 1310 and i <= 1345:
        print(f'Line {i} depth={depth}: {repr(line[:80])}')
