with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx3 = text.find('id="panel-cc"')
idx4 = text.find('id="panel-assets"')
cc = text[idx3:idx4]
import sys
sys.stdout.reconfigure(encoding='utf-8')
print(cc[-300:])
