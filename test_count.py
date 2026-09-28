import sys
with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count('<span class="feat-icon">??</span>')
print('Count of ?? is:', count)

# Let's see what is inside the feat-icon span!
import re
matches = re.findall(r'<span class="feat-icon">(.*?)</span>', text)
print('Unique contents of feat-icon:', set(matches))
