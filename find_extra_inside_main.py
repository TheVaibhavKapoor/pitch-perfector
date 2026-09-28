import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

main_start = text.find('<main class="main-content">')
main_end = text.find('</main>')
main_section = text[main_start:main_end]

# Track depth inside main section and find where it goes negative
depth = 0
lines = main_section.split('\n')
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    prev = depth
    depth += oc - cc
    if depth < 0 and prev >= 0:
        print(f'Depth goes negative in main at relative line {i}:')
        for j in range(max(0,i-5), min(len(lines), i+3)):
            print(f'  main-line {j+1}: {repr(lines[j][:100])}')
        break
