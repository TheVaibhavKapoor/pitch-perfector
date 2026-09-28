import re

files = [
    r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html',
    r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard_new.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update product card subtitle
    content = content.replace('<span class="product-subtitle">Wealth & Real Estate</span>', '<span class="product-subtitle">Premium Lending</span>')
    # Update product card description
    content = content.replace('<span class="product-timestamp">Manage your real estate portfolio</span>', '<span class="product-timestamp">Bespoke borrowing solutions</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated Loans write-ups!')
