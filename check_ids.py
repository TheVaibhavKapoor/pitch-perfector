import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'id=\"panel-.*?\"', text)
for m in matches:
    print(m.group(0))
