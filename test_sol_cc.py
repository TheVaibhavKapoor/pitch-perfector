with open('solitaire_cc.html', 'r', encoding='utf-8') as f:
    text = f.read()
import re
match = re.search(r'(<div class="product-features-grid">.*)', text, re.DOTALL)
if match:
    print('Found product-features-grid!')
    content = match.group(1)
    print(content[:200])
