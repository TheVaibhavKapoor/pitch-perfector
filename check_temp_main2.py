import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all </main> positions
import re
for m in re.finditer(r'</main>', text):
    print('</main> at pos:', m.start())
    print(text[m.start()-100:m.start()+100])
    print()
