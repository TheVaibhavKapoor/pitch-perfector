import os
import re

raw_data = """Benefit / Proposition	PRIVY	PRIVY+	SOLITAIRE
Positioning	Premium Banking	Upper Premium Banking	Invite-only Elite / HNI
Relationship Value	₹10 lakh	₹30 lakh	₹75 lakh Salaried / ₹1 Cr Self-employed
Salary eligibility	₹1–3 lakh/month	₹3 lakh+/month	₹5 lakh+/month
Dedicated RM	✓	✓	✓ Premium personalised RM
Family Banking	✓	✓	✓ Family-wide programme
Savings + ActiveMoney	✓	✓	✓
4-in-1 Account	✓	✓	Investment/wealth ecosystem
Demat + Trading	✓	✓	✓
ActivMoney	✓	✓	✓
Credit Card	Kotak Air	Kotak Air+	Solitaire Metal
Air Miles – Travel	3 / ₹100	5 / ₹100	10 / ₹100 via Unbox
Air Miles – Other spends	1 / ₹100	2 / ₹100	3 / ₹100
Travel redemption value	₹1/mile on eligible travel	₹1/mile on eligible travel	₹1/mile on eligible travel
Domestic lounge	4/year	4/year	Unlimited
International lounge	—	2/year	Unlimited
Forex markup – Credit Card	Standard applicable	2%	0%
Welcome Air Miles	1,000	2,500	—
Renewal Air Miles	1,000	2,500	—
Credit Card annual fee	₹999 + GST	₹3,000 + GST	₹0 while Solitaire eligible
Home Loan – Pre-approved	₹85 lakh	₹1 crore	₹7.5 crore
Auto Loan – Pre-approved	₹25 lakh	₹40 lakh	Premium/pre-qualified proposition
Personal Loan – Pre-approved	₹10 lakh	₹15 lakh	Premium/pre-qualified proposition
Credit Line / OD	—	Mid-Month Advance	₹25 lakh credit line
Interest on utilised credit line	—	Applicable	Only amount utilised
Health Insurance	✓	✓	✓
Health Assure Prime	Up to ₹1 crore	Up to ₹1 crore	Insurance solutions available
Health reset benefit	✓	Unlimited reset for unrelated illnesses	—
Pre-existing disease waiting period	Product dependent	30 days for specified proposition	—
Zomato Dining – Debit Card	10% / ₹600 pm	10% / ₹1,000 pm	Premium Solitaire benefits
District / Solitaire Table	—	—	20% up to ₹5,000 × 2/month
Maximum District monthly benefit	—	—	₹10,000/month
District annual potential	—	—	₹1.20 lakh/year
Curated dining access	—	—	✓ Exclusive / early access
Concierge	Premium services	Premium services	Solitaire Concierge
Luxury travel benefits	✓	✓	Enhanced
Global investment	Investment access	Investment access	Up to USD 250,000/year
Outward remittance	Standard applicable	Standard applicable	Up to USD 50,000 facility
AIF / Alternate Investments	—	—	Access/referral through group
Wealth Management	✓	✓	Enhanced / dedicated
Life Insurance	✓	✓	✓
Locker benefits	✓	✓	✓
Debit Card Purchase Limit	—	₹15 lakh/day	₹15 lakh/day
Debit Card ATM Limit	—	₹2 lakh/day	₹2.5 lakh/day
Fuel surcharge waiver	—	2.5% up to ₹30,000 fuel/month	2.5% up to ₹30,000/month
Debit Card Air Accident Cover	—	₹1 crore*	₹5 crore
Personal Accident Cover	Up to ₹15 lakh*	Up to ₹15 lakh*	Up to ₹5 lakh*
Lost Card Liability	Up to ₹4.75 lakh*	Up to ₹4.75 lakh*	Applicable
Purchase Protection	Up to ₹1.5 lakh*	Up to ₹1.5 lakh*	Applicable
Lost Baggage Insurance	₹1 lakh*	₹1 lakh*	Applicable
Family grouping	✓	✓	✓ Entire group upgraded
Best suited for	Affluent	Upper Affluent	HNI / UHNI"""

lines = raw_data.strip().split('\n')
headers = lines[0].split('\t')
rows = [line.split('\t') for line in lines[1:]]

# Build the new table HTML
new_table_html = '<table class="program-compare-table">\n'
new_table_html += '    <thead style="position: sticky; top: 0; z-index: 10;">\n        <tr>\n'
for h in headers:
    new_table_html += f'            <th>{h}</th>\n'
new_table_html += '        </tr>\n    </thead>\n    <tbody>\n'

for r in rows:
    new_table_html += '        <tr>\n'
    new_table_html += f'            <td><strong>{r[0]}</strong></td>\n'
    for cell in r[1:]:
        new_table_html += f'            <td>{cell}</td>\n'
    new_table_html += '        </tr>\n'
new_table_html += '    </tbody>\n</table>'

target_files = [
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard_new.html'
]

for filename in target_files:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update max-width of compare-modal
    # Match <div id="compare-modal" ...> followed by <div class="ntb-modal">
    # We want to change the <div class="ntb-modal"> to <div class="ntb-modal" style="max-width: 1100px;">
    pattern_modal = r'(<div id="compare-modal"[^>]*>)\s*<div class="ntb-modal">'
    replacement_modal = r'\1\n    <div class="ntb-modal" style="max-width: 1100px;">'
    content = re.sub(pattern_modal, replacement_modal, content)

    # 2. Replace the whole table
    pattern_table = r'<table class="program-compare-table">.*?</table>'
    content = re.sub(pattern_table, new_table_html, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")
