with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Has </body>?', '</body>' in text)
print('Has ???', '\U0001F3E0' in text)
print('Has feat-card-header?', 'feat-card-header' in text)

import re
matches = re.findall(r'<div class="feat-card-header">.*?</div>', text)
if matches:
    print('Header found:', matches[0])
