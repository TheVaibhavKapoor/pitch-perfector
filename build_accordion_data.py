import glob
import re

categories = [
    {
        "name": "Eligibility",
        "items": [
            {"benefit": "Relationship Value", "privy": "₹10L", "privy_plus": "₹30L", "solitaire": "₹75L+"},
            {"benefit": "Salary Route", "privy": "₹1L+/month", "privy_plus": "₹3L+/month", "solitaire": "₹5L+/month"}
        ]
    },
    {
        "name": "Accounts & Convenience",
        "items": [
            {"benefit": "Privileged Savings Account", "privy": "✓", "privy_plus": "✓", "solitaire": "✓"},
            {"benefit": "4-in-1 Account", "privy": "✓", "privy_plus": "✓", "solitaire": "✓"},
            {"benefit": "ActiveMoney", "privy": "✓", "privy_plus": "✓", "solitaire": "✓"},
            {"benefit": "Demat & Trading", "privy": "✓", "privy_plus": "✓", "solitaire": "✓"},
            {"benefit": "Family Banking", "privy": "✓", "privy_plus": "✓", "solitaire": "✓"}
        ]
    },
    {
        "name": "Credit Cards",
        "items": [
            {"benefit": "Card", "privy": "Air", "privy_plus": "Air+", "solitaire": "Solitaire"},
            {"benefit": "Travel Air Miles", "privy": "3/₹100", "privy_plus": "5/₹100", "solitaire": "10/₹100 via Unbox"},
            {"benefit": "Other Eligible Spends", "privy": "1/₹100", "privy_plus": "2/₹100", "solitaire": "3/₹100"},
            {"benefit": "Domestic Lounge", "privy": "4/year*", "privy_plus": "4/year*", "solitaire": "Unlimited"},
            {"benefit": "International Lounge", "privy": "—", "privy_plus": "2/year*", "solitaire": "Unlimited"},
            {"benefit": "Forex Mark-up", "privy": "Standard", "privy_plus": "2%", "solitaire": "0%"},
            {"benefit": "Welcome Air Miles", "privy": "1,000", "privy_plus": "2,500", "solitaire": "—"},
            {"benefit": "Renewal Air Miles", "privy": "1,000", "privy_plus": "2,500", "solitaire": "—"},
            {"benefit": "Annual Fee", "privy": "₹999 + GST", "privy_plus": "₹3,000 + GST", "solitaire": "₹0 while eligible"}
        ]
    },
    {
        "name": "Loans & Credit",
        "items": [
            {"benefit": "Home Loan", "privy": "Up to ₹85L", "privy_plus": "Up to ₹1Cr", "solitaire": "Up to ₹7.5Cr"},
            {"benefit": "Auto Loan", "privy": "Up to ₹25L", "privy_plus": "Up to ₹40L", "solitaire": "Available as per eligibility"},
            {"benefit": "Personal Loan", "privy": "Up to ₹10L", "privy_plus": "Up to ₹15L", "solitaire": "Available as per eligibility"},
            {"benefit": "Credit Line", "privy": "—", "privy_plus": "Mid-Month Advance", "solitaire": "Up to ₹25L"},
            {"benefit": "LAP", "privy": "—", "privy_plus": "—", "solitaire": "Special Rates"}
        ]
    }
]

def generate_accordion_html(categories):
    # CSS and JS are already in the file, we just need to generate the HTML
    html = ''
    html += '<div class="compare-global-header"><div class="cg-benefit">Benefit / Feature</div><div class="cg-privy">PRIVY</div><div class="cg-privyplus">PRIVY+</div><div class="cg-solitaire">SOLITAIRE</div></div>\n'
    
    for cat in categories:
        html += '<div class="compare-category">\n'
        html += '<button class="compare-cat-header" onclick="toggleCompareCategory(this)">\n'
        html += f'    {cat["name"]}\n'
        html += '    <span class="compare-cat-icon">▼</span>\n'
        html += '</button>\n'
        html += '<div class="compare-cat-content">\n'
        html += '<table class="compare-inner-table">\n'
        html += '<tbody>\n'
        for item in cat["items"]:
            html += '<tr>\n'
            html += f'<td class="col-benefit">{item["benefit"]}</td>\n'
            html += f'<td class="col-privy">{item["privy"]}</td>\n'
            html += f'<td class="col-privyplus">{item["privy_plus"]}</td>\n'
            html += f'<td class="col-solitaire">{item["solitaire"]}</td>\n'
            html += '</tr>\n'
        html += '</tbody>\n'
        html += '</table>\n'
        html += '</div>\n'
        html += '</div>\n'
        
    return html

new_html = generate_accordion_html(categories)

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find <div class="compare-global-header">...</div> up to the end of the categories
    # The categories end right before </div> </div> <!-- close modal-body --> (or similar)
    # Let's use a simpler regex that looks for the global header and all the compare-categories
    pattern = r'<div class="compare-global-header">.*?(?=</div>\s*</div>\s*</div>\s*<script>)'
    
    # Actually, let's just find the first <div class="compare-global-header"> and replace until the last <div class="compare-category">...</div>
    # Better yet, let's find the start of the compare-global-header, and the end of the accordion.
    
    # In customer_overview_solitaire.html:
    # <div class="compare-global-header">...</div>
    # <div class="compare-category">...</div>
    # <div class="compare-category">...</div>
    # ...
    # </div> <!-- close compare-accordion --> (if exists) or just before <script>
    
    pattern2 = r'<div class="compare-global-header">.*?(?=\s*</div>\s*</div>\s*<script>)'
    if re.search(pattern2, content, flags=re.DOTALL):
        updated = re.sub(pattern2, new_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated {file}")
    else:
        # Fallback if the regex doesn't match exactly
        pattern3 = r'<div class="compare-global-header">.*?(?=\s*</div>\s*</div>\s*</div>)'
        if re.search(pattern3, content, flags=re.DOTALL):
            updated = re.sub(pattern3, new_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Updated {file} (fallback)")
