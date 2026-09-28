import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="panel-dc"')
end = text.find('id="dc-existing-table"')
print(text[start:end].count('<div') - text[start:end].count('</div'))
