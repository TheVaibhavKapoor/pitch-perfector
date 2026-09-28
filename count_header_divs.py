import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Count divs between body and main
body_pos = text.find('<body')
main_pos = text.find('<main')
section = text[body_pos:main_pos]
opens = len(re.findall(r'<div[\s>]', section))
closes = len(re.findall(r'</div>', section))
print(f'Between body and main: opens={opens}, closes={closes}, net open={opens-closes}')

# So opens-closes should be the number of divs still open when main begins
# These need to be closed after </main>
# Specifically: app-layout (1) + content nesting inside aside
print()
print('The net open divs before main:', opens-closes, '(these will all be closed after main)')
print()

# Count divs inside main section  
main_pos2 = text.find('</main>')
main_section = text[main_pos:main_pos2]
m_opens = len(re.findall(r'<div[\s>]', main_section))
m_closes = len(re.findall(r'</div>', main_section))
print(f'Inside main: opens={m_opens}, closes={m_closes}, net={m_opens-m_closes}')
print('(All divs opened in main should be closed inside main, net should be 0)')
