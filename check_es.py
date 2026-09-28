import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('dc-new-grid:', text.find('id="dc-new-grid"'))
print('LAP loan:', text.find('LAP loan'))
print('panel-cc:', text.find('id="panel-cc"'))
