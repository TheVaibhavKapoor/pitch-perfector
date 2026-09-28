import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="panel-dc"')
end = text.find('id="panel-cc"')
print('Div balance of panel-dc in temp_check:', text[start:end].count('<div') - text[start:end].count('</div'))
