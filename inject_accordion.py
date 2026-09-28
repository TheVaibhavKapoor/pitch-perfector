import os
import glob
import re

raw_data = """CATEGORY	BENEFIT	PRIVY	PRIVY+	SOLITAIRE
Eligibility	Relationship Value	₹10L	₹30L	₹75L+
Eligibility	Salary Route	₹1L+/month	₹3L+/month	₹5L+/month
Accounts & Convenience	Privileged Savings Account	✓	✓	✓
Accounts & Convenience	4-in-1 Account	✓	✓	✓
Accounts & Convenience	ActiveMoney	✓	✓	✓
Accounts & Convenience	Demat & Trading	✓	✓	✓
Accounts & Convenience	Family Banking	✓	✓	✓
Credit Cards	Card	Air	Air+	Solitaire
Credit Cards	Travel Air Miles	3/₹100	5/₹100	10/₹100 via Unbox
Credit Cards	Other Eligible Spends	1/₹100	2/₹100	3/₹100
Credit Cards	Domestic Lounge	4/year*	4/year*	Unlimited
Credit Cards	International Lounge	—	2/year*	Unlimited
Credit Cards	Forex Mark-up	Standard	2%	0%
Credit Cards	Welcome Air Miles	1,000	2,500	—
Credit Cards	Renewal Air Miles	1,000	2,500	—
Credit Cards	Annual Fee	₹999 + GST	₹3,000 + GST	₹0 while eligible
Loans & Credit	Home Loan	Up to ₹85L	Up to ₹1Cr	Up to ₹7.5Cr
Loans & Credit	Auto Loan	Up to ₹25L	Up to ₹40L	Available as per eligibility
Loans & Credit	Personal Loan	Up to ₹10L	Up to ₹15L	Available as per eligibility
Loans & Credit	Credit Line	—	Mid-Month Advance	Up to ₹25L
Loans & Credit	LAP / OD / Working Capital	✓	✓	✓
Investments	Mutual Funds	✓	✓	✓
Investments	SIP / STP / SWP	✓	✓	✓
Investments	Equity & Demat	✓	✓	✓
Investments	Trading	✓	✓	✓
Investments	Wealth Solutions	✓	✓	✓ Enhanced
Investments	Alternate Investments	—	—	✓
Investments	Overseas Investment	Standard limits	Standard limits	Up to USD 250K/year
Insurance	Health Insurance	✓	✓	✓
Insurance	Health Assure Prime	Up to ₹1Cr	Up to ₹1Cr	✓
Insurance	Unlimited Reset	—	✓	Product dependent
Insurance	Inflation Protection	—	✓	Product dependent
Insurance	Wellness Benefit	—	Up to 30%	Product dependent
Dining & Lifestyle	Zomato Dining	10% up to ₹600/month	10% up to ₹1,000/month	Premium benefits
Dining & Lifestyle	District Benefits	—	—	20% up to ₹5,000 × 2/month
Dining & Lifestyle	Maximum District Benefit	—	—	₹10,000/month
Dining & Lifestyle	Curated Experiences	—	✓	✓ Exclusive / early access
Dining & Lifestyle	Hotel Benefits	✓	✓	Premium hotel privileges
Travel	Airport Lounge	4 domestic*	4 domestic + 2 international*	Unlimited domestic + international
Travel	Travel Rewards	✓	✓	Enhanced
Travel	Concierge	—	—	✓
Travel	Visa Assistance	—	—	✓
Travel	Airport Assistance	—	—	✓
Global Banking	Forex	Standard	2%	0%
Global Banking	Overseas Investment	Standard	Standard	Up to USD 250K/year
Global Banking	Outward Remittance	Standard	Standard	Up to USD 50K
Service	Relationship Manager	✓	✓	Dedicated RM
Service	Priority Service	✓	✓	✓
Service	Family Support	✓	✓	✓"""

lines = raw_data.strip().split('\n')
headers = lines[0].split('\t')

# Group by category
categories = {}
for line in lines[1:]:
    parts = line.split('\t')
    cat = parts[0]
    if cat not in categories:
        categories[cat] = []
    categories[cat].append({
        'benefit': parts[1],
        'privy': parts[2],
        'privy_plus': parts[3],
        'solitaire': parts[4]
    })

def generate_accordion_html(categories):
    html = '<div class="compare-accordion">\n'
    html += '''
<style>
.compare-accordion {
    width: 100%;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    background: #ffffff;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
.compare-category {
    border-bottom: 1px solid #e2e8f0;
}
.compare-category:last-child {
    border-bottom: none;
}
.compare-cat-header {
    width: 100%;
    padding: 16px 24px;
    background: #f8fafc;
    border: none;
    text-align: left;
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background 0.2s;
}
.compare-cat-header:hover {
    background: #f1f5f9;
}
.compare-cat-icon {
    transition: transform 0.3s ease;
    font-size: 1.2rem;
    color: #64748b;
}
.compare-cat-content {
    display: none;
    padding: 0;
}
.compare-cat-content.active {
    display: block;
    animation: fadeIn 0.3s ease-in-out;
}
.compare-inner-table {
    width: 100%;
    border-collapse: collapse;
}
.compare-inner-table th {
    background: #f1f5f9;
    padding: 12px 24px;
    font-size: 0.85rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
    text-align: left;
}
.compare-inner-table td {
    padding: 16px 24px;
    border-bottom: 1px solid #f1f5f9;
    font-size: 0.95rem;
    color: #334155;
    vertical-align: top;
}
.compare-inner-table tr:last-child td {
    border-bottom: none;
}
.col-benefit { width: 25%; font-weight: 600; color: #0f172a; }
.col-privy { width: 25%; }
.col-privyplus { width: 25%; }
.col-solitaire { width: 25%; font-weight: 700; color: #1e3a8a; }

/* Desktop header row outside accordion so columns align visually */
.compare-global-header {
    display: flex;
    padding: 12px 24px 12px 24px;
    background: #e2e8f0;
    border-radius: 12px 12px 0 0;
    font-weight: 700;
    color: #0f172a;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.compare-global-header > div {
    flex: 1;
}
.cg-benefit { flex: 0 0 25%; }
.cg-privy { flex: 0 0 25%; padding-left: 24px; }
.cg-privyplus { flex: 0 0 25%; padding-left: 24px; }
.cg-solitaire { flex: 0 0 25%; padding-left: 24px; color: #1e40af; }
</style>

<script>
function toggleCompareCategory(btn) {
    const content = btn.nextElementSibling;
    const icon = btn.querySelector('.compare-cat-icon');
    
    if (content.classList.contains('active')) {
        content.classList.remove('active');
        icon.style.transform = 'rotate(0deg)';
    } else {
        // Optional: close all others
        // document.querySelectorAll('.compare-cat-content').forEach(c => c.classList.remove('active'));
        // document.querySelectorAll('.compare-cat-icon').forEach(i => i.style.transform = 'rotate(0deg)');
        
        content.classList.add('active');
        icon.style.transform = 'rotate(180deg)';
    }
}
</script>
'''
    html += '<div class="compare-global-header"><div class="cg-benefit">Benefit / Feature</div><div class="cg-privy">PRIVY</div><div class="cg-privyplus">PRIVY+</div><div class="cg-solitaire">SOLITAIRE</div></div>\n'
    
    for cat_name, items in categories.items():
        html += '<div class="compare-category">\n'
        html += f'''<button class="compare-cat-header" onclick="toggleCompareCategory(this)">
    <span>{cat_name}</span>
    <span class="compare-cat-icon">▼</span>
</button>\n'''
        html += '<div class="compare-cat-content">\n'
        html += '<table class="compare-inner-table">\n'
        html += '<tbody>\n'
        for item in items:
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
        
    html += '</div>'
    return html

new_html = generate_accordion_html(categories)

# Update all html files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace old <table class="program-compare-table">...</table> with new_html
    pattern = r'<table class="program-compare-table">.*?</table>'
    if re.search(pattern, content, flags=re.DOTALL):
        updated = re.sub(pattern, new_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated {file}")
