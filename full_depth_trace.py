import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
depth = 0
first_neg = None
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    prev = depth
    depth += oc - cc
    if depth < 0 and first_neg is None:
        first_neg = i
        print(f'First negative at line {i}: depth={depth}')
        for j in range(max(0, i-4), min(len(lines), i+3)):
            print(f'  {j+1}: {repr(lines[j][:80])}')
        break

if first_neg is None:
    print('No negative depth found')

# Show end state
depth = 0
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    depth += oc - cc
print(f'Final depth: {depth}')
oc_all = len(re.findall(r'<div[\s>]', text))
cc_all = len(re.findall(r'</div>', text))
print(f'Total opens={oc_all}, closes={cc_all}, diff={oc_all-cc_all}')
