import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# What comes AFTER </html> ?
html_end = text.find('</html>')
print('After </html>:')
print(text[html_end:html_end + 2000])
