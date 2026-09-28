import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check: at depth 1 line 1282, what div was closed?
depth = 0
lines = text.split('\n')
# Show significant div lines from 1250 to 1290
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    depth += opens - closes
    if i >= 1257 and i <= 1295 and (opens > 0 or closes > 0):
        print(f'Line {i} depth={depth} (+{opens}/-{closes}): {repr(line[:80])}')
