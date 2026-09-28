import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('panel-cc:', text.find('id="panel-cc"'))
print('panel-assets:', text.find('id="panel-assets"'))
