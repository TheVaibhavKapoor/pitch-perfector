import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<div class="info-panel" id="panel-dc">')
end = text.find('<div class="info-panel" id="panel-cc">')
if start != -1 and end != -1:
    dc_panel = text[start:end]
    print('Open divs:', dc_panel.count('<div') - dc_panel.count('</div'))
