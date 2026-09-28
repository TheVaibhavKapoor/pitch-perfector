import re, codecs

def fix_loans_writeup(filepath):
    print(f'=== Updating Loans card writeup in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Replace Wealth & Real Estate with Premium Lending or Asset-Backed Lending
    text = text.replace('<span class="product-subtitle">Wealth & Real Estate</span>', '<span class="product-subtitle">Asset-Backed Lending</span>')
    text = text.replace('<span class="product-subtitle">Wealth &amp; Real Estate</span>', '<span class="product-subtitle">Asset-Backed Lending</span>')

    # 2. Replace Manage your real estate portfolio with Bespoke borrowing & credit solutions
    text = text.replace('<span class="product-timestamp">Manage your real estate portfolio</span>', '<span class="product-timestamp">Bespoke borrowing &amp; credit solutions</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done updating {filepath}')

fix_loans_writeup('experience_solitaire_dashboard_new.html')
fix_loans_writeup('experience_solitaire_dashboard.html')
