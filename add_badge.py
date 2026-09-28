import re

files = ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_header = '<div class="feat-card-header"><span class="feat-icon">\U0001F3E0</span><h3>Home Loan</h3><span class="featured-badge" onclick="openHomeLoanModal()">\u2728 Featured</span></div>'
    
    # Replace the exact match
    content = re.sub(r'<div class="feat-card-header">\s*<span class="feat-icon">.*?</span>\s*<h3>Home Loan</h3>\s*</div>', new_header, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done replacing header")
