import re
with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()
match = re.search(r'<span class="feat-icon">(.*?)</span><h3>Home Loan</h3>', text)
if match:
    s = match.group(1)
    print('Found string:', repr(s))
    print('Char codes:', [ord(c) for c in s])
else:
    print('Not found')
