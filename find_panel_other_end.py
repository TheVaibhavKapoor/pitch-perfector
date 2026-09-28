import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

main_start = text.find('<main class="main-content">')
main_end = text.find('</main>')
main_section = text[main_start:main_end]

lines = main_section.split('\n')
depth = 0
# Show depth context from line 770 to 820
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    depth += oc - cc
    if i >= 770 and i <= 825:
        print(f'Line {i} depth={depth}: {repr(line[:80])}')
