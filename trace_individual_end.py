import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

main_start = text.find('<main class=')
main_end = text.find('</main>')
main_section = text[main_start:main_end]
main_lines = main_section.split('\n')

# Track depth inside main
depth = 0
for i, line in enumerate(main_lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    prev = depth
    depth += oc - cc
    if depth < 0 and prev >= 0:
        print(f'Main-relative line {i}: depth goes negative ({prev}->{depth})')
        for j in range(max(0,i-5), min(len(main_lines), i+5)):
            print(f'  {j+1}: {repr(main_lines[j][:100])}')
        break

# Also show total counts
oc_total = len(re.findall(r'<div[\s>]', main_section))
cc_total = len(re.findall(r'</div>', main_section))
print(f'\nMain section: opens={oc_total}, closes={cc_total}, diff={oc_total-cc_total}')
