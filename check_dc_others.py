import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<h2.*?Solitaire Debit Card</h2>', text)
for m in matches:
    print('Found Solitaire Debit Card at:', m.start())
