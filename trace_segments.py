import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

main_start = text.find('<main class=')
main_end = text.find('</main>')
main_section = text[main_start:main_end]
main_lines = main_section.split('\n')

# Find panel-other section
depth = 0
for i, line in enumerate(main_lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    depth += oc - cc
    
    # Print lines where depth changes around the individual->business transition
    if i >= 820 and i <= 875:
        if oc > 0 or cc > 0:
            print(f'main-{i} depth={depth} (+{oc}/-{cc}): {repr(line[:100])}')
        elif 'panel-other' in line or 'segment-' in line or 'Calculate' in line:
            print(f'main-{i} depth={depth}: {repr(line[:100])}')
