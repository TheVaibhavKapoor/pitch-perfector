import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Show structure from body open to first main open
body_pos = text.find('<body')
main_pos = text.find('<main')
section = text[body_pos:main_pos]
print('Between <body> and <main>:')
print(section[:2000])
