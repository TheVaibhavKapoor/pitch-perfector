import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find </main> position and show surrounding area    
main_pos = text.find('</main>')
print(f'</main> at pos: {main_pos}')
print('Context:')
print(text[main_pos-200:main_pos+300])
