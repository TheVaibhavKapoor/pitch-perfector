import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<div class=\"feature-card\">', text)
m = next(matches)
print('First feature-card at:', m.start())
