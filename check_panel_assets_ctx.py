import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find panel-assets position and show surrounding area    
pa_pos = text.find('id="panel-assets"')
print(f'panel-assets at pos: {pa_pos}')
print('Context (500 chars before):')
print(repr(text[pa_pos-500:pa_pos]))
