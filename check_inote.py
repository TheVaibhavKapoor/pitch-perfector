import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<h3>Important Note</h3>')
print(text[idx-50:idx+300])
