import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<div class=\"info-panel\" id=\"panel-dc\">')
end = text.find('<div class=\"info-panel\" id=\"panel-cc\">')
dc_panel = text[start:end]
print(dc_panel)
