import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('panel-dc:', text.find('panel-dc'))
print('panel-cc:', text.find('panel-cc'))
print('panel-assets:', text.find('panel-assets'))
