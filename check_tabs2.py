import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<div class=.*?>.*?Debit Card.*?</div>', text)
for m in matches:
    print('Found Debit Card:', text[m.start():m.start()+200])
