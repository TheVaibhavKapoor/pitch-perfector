import re
with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<div class="feat-card-header">.*?<h3>Home Loan</h3>\s*</div>', text, flags=re.DOTALL)
for i, m in enumerate(matches):
    print(f'Match {i}:', repr(m))
