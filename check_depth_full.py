import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The correct depth when hitting </main> should be 1 (just the app-layout div open)
# Currently it's 0 which means we've over-closed (by 1 div)
# This means there's one EXTRA </div> somewhere in the business content or similar

# Find the depth sequence
depth = 0
lines = text.split('\n')
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    depth += opens - closes
    # Show all div-significant lines in range 1278-1342
    if i >= 1278 and i <= 1342 and (opens > 0 or closes > 0):
        print(f'Line {i} depth={depth} (+{opens}/-{closes}): {repr(line[:80])}')
