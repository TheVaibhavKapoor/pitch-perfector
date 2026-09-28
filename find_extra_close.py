import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the transition from depth 0 to depth -1 (the extra close)
depth = 0
lines = text.split('\n')
problem_lines = []
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    prev = depth
    depth += oc - cc
    if depth < 0 and prev >= 0:
        problem_lines.append(i)
        print(f'Line {i} goes negative (depth={depth}): {repr(line[:100])}')
        # Show context
        for j in range(max(0,i-4), min(len(lines), i+3)):
            print(f'  Line {j+1}: {repr(lines[j][:80])}')
        break
