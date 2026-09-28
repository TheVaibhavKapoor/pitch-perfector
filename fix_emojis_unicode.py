import re

files = ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Emojis
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Home Loan</h3>', '<span class="feat-icon">\U0001F3E0</span><h3>Home Loan</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Car Loan</h3>', '<span class="feat-icon">\U0001F697</span><h3>Car Loan</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Pre-approved Credit Line</h3>', '<span class="feat-icon">\U0001F4B3</span><h3>Pre-approved Credit Line</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Working Capital</h3>', '<span class="feat-icon">\U0001F4BC</span><h3>Working Capital</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Loan Against Property \(LAP\)</h3>', '<span class="feat-icon">\U0001F3E2</span><h3>Loan Against Property (LAP)</h3>', content)
    
    # Dealer Support etc for investments
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Dealer Support</h3>', '<span class="feat-icon">\U0001F91D</span><h3>Dealer Support</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Equity &amp; Futures</h3>', '<span class="feat-icon">\U0001F4C8</span><h3>Equity &amp; Futures</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Margin Trading \(MTF\)</h3>', '<span class="feat-icon">\U0001F4B0</span><h3>Margin Trading (MTF)</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Options Trading</h3>', '<span class="feat-icon">\U0001F4CA</span><h3>Options Trading</h3>', content)
    content = re.sub(r'<span class="feat-icon">\?\?+</span><h3>Demat Account</h3>', '<span class="feat-icon">\U0001F4D1</span><h3>Demat Account</h3>', content)

    # Rupee symbols (using string concatenation to avoid re.sub raw string escape issues)
    content = re.sub(r'<strong>\? (\d+(?:\.\d+)?) (Crore|lakhs)</strong>', '<strong>\u20B9 \\1 \\2</strong>', content)
    content = re.sub(r'Options \?(\d+) per lot', 'Options \u20B9\\1 per lot', content)

    # Some ? without the <strong> tags
    content = re.sub(r'Up to <strong>\? 7\.5 Crore</strong>', 'Up to <strong>\u20B9 7.5 Crore</strong>', content)
    content = re.sub(r'Up to <strong>\? 1 Crore</strong>', 'Up to <strong>\u20B9 1 Crore</strong>', content)
    content = re.sub(r'Up to <strong>\? 25 lakhs</strong>', 'Up to <strong>\u20B9 25 lakhs</strong>', content)
    content = re.sub(r'\? 7\.5 Crore', '\u20B9 7.5 Crore', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done with unicode escapes")
