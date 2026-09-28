import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

depth = 0
lines = text.split('\n')
problem_line = -1
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    prev_depth = depth
    depth += opens - closes
    if prev_depth >= 0 and depth < 0:
        problem_line = i
        print(f'First negative depth at line {i}: {repr(line[:120])}')
        # Show 5 lines before
        for j in range(max(0, i-6), i+2):
            print(f'  Line {j+1}: {repr(lines[j][:100])}')
        break
