import re

files = ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Emojis
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Home Loan</h3>', '<span class="feat-icon">??</span><h3>Home Loan</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Car Loan</h3>', '<span class="feat-icon">??</span><h3>Car Loan</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Pre-approved Credit Line</h3>', '<span class="feat-icon">??</span><h3>Pre-approved Credit Line</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Working Capital</h3>', '<span class="feat-icon">??</span><h3>Working Capital</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Loan Against Property \(LAP\)</h3>', '<span class="feat-icon">??</span><h3>Loan Against Property (LAP)</h3>', content)
    
    # Dealer Support etc for investments
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Dealer Support</h3>', '<span class="feat-icon">??</span><h3>Dealer Support</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Equity &amp; Futures</h3>', '<span class="feat-icon">??</span><h3>Equity &amp; Futures</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Margin Trading \(MTF\)</h3>', '<span class="feat-icon">??</span><h3>Margin Trading (MTF)</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Options Trading</h3>', '<span class="feat-icon">??</span><h3>Options Trading</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Demat Account</h3>', '<span class="feat-icon">??</span><h3>Demat Account</h3>', content)

    # Rupee symbols
    content = re.sub(r'<strong>\? (\d+(?:\.\d+)?) (Crore|lakhs)</strong>', r'<strong>? \1 \2</strong>', content)
    content = re.sub(r'Options \?(\d+) per lot', r'Options ?\1 per lot', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
