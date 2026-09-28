import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'<h3>Important Note</h3>', text)
for m in matches:
    print('Found at', m.start())
    print(text[m.start()-50:m.start()+50])
