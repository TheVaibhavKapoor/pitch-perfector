import os
filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)\customer_overview_solitaire.html'
try:
    with open(filepath, 'r', encoding='utf-16') as f:
        content = f.read()
except Exception:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

content = content.replace('<input type="email" value="vaibhavkapoorwork@gmail.com" readonly', '<input type="email" id="send-deck-email" value="vaibhavkapoorwork@gmail.com" readonly')

try:
    with open(filepath, 'w', encoding='utf-16') as f:
        f.write(content)
except Exception:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done fixing missing ID')
