import os
from bs4 import BeautifulSoup

def fix_expandable_intro(filename, program_name, intro_text, eligibility_text, categories):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    panel_intro = soup.find(id='panel-intro')
    if panel_intro:
        # Clear out existing content except the top RM Intro stuff
        rm_box = panel_intro.find('div', style=lambda s: s and 'border-left: 4px solid #1e3a8a' in s)
        rm_header = panel_intro.find('h2')
        
        panel_intro.clear()
        
        if rm_header:
            panel_intro.append(rm_header)
        if rm_box:
            panel_intro.append(rm_box)
            
        # 1. ALWAYS SHOW: Program Intro Header, Text, and Eligibility
        prog_intro_h = soup.new_tag('h3', style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-top: 24px; margin-bottom: 8px;")
        prog_intro_h.string = f"{program_name} Program Introduction"
        panel_intro.append(prog_intro_h)
        
        intro_p = soup.new_tag('p', style="color: #475569; line-height: 1.6; margin-bottom: 12px; font-size: 0.95rem;")
        intro_p.string = intro_text
        panel_intro.append(intro_p)
        
        elig_p = soup.new_tag('p', style="margin-bottom: 24px; background: #f8fafc; padding: 12px; border-radius: 6px; border-left: 3px solid #64748b; font-size: 0.95rem; color: #475569;")
        elig_p.append(BeautifulSoup(f'<strong>Eligibility:</strong> {eligibility_text}', 'html.parser'))
        panel_intro.append(elig_p)
            
        # 2. EXPANDABLE: Key Features
        details = soup.new_tag('details', style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);")
        
        summary = soup.new_tag('summary', style="padding: 16px; font-weight: 700; color: #0f172a; font-size: 1.05rem; cursor: pointer; outline: none; list-style: none; display: flex; justify-content: space-between; align-items: center;")
        summary_html = f'''
            <span style="display: flex; align-items: center; gap: 8px;">
                <svg fill="none" height="20" stroke="#3b82f6" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path><path d="M12 8v8"></path><path d="M8 12h8"></path></svg>
                Key Features
            </span>
        '''
        summary.append(BeautifulSoup(summary_html, 'html.parser'))
        
        content_div = soup.new_tag('div', style="padding: 0 16px 16px 16px; border-top: 1px solid #f1f5f9; margin-top: 8px; padding-top: 16px;")
        
        # Add categories
        for cat_icon, cat_title, items in categories:
            cat_div = soup.new_tag('div', style="margin-bottom: 16px;")
            cat_h = soup.new_tag('h4', style="font-weight: 600; color: #0f172a; margin-bottom: 8px; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;")
            cat_h.append(BeautifulSoup(f'<span>{cat_icon}</span> {cat_title}', 'html.parser'))
            cat_div.append(cat_h)
            
            ul = soup.new_tag('ul', style="padding-left: 28px; margin-bottom: 0; line-height: 1.6; color: #475569; font-size: 0.95rem;")
            for item in items:
                li = soup.new_tag('li', style="margin-bottom: 4px;")
                li.string = item
                ul.append(li)
            cat_div.append(ul)
            content_div.append(cat_div)
        
        details.append(summary)
        details.append(content_div)
        
        style = soup.new_tag('style')
        style.string = "details > summary::-webkit-details-marker { display: none; }"
        if not soup.find('style', string="details > summary::-webkit-details-marker { display: none; }"):
            soup.head.append(style)
        
        panel_intro.append(details)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filename}")


solitaire_intro = "Kotak Solitaire is Kotak Mahindra Bank’s invite-only premium/private banking proposition designed for affluent and HNI customers and their families. It combines wealth management, premium banking, exclusive credit cards, preferential lending and lifestyle privileges with dedicated relationship support."
solitaire_elig = "Generally, salaried customers require ₹75 lakh+ Relationship Value (RV), while self-employed customers require ₹1 crore+ RV across family relationships."
solitaire_cats = [
    ("🏦", "Premium Banking", [
        "Dedicated Relationship Manager",
        "Priority/personalised banking service",
        "Family relationship banking",
        "Preferential rates on select banking products",
        "ActivMoney — FD-like returns on idle savings balance"
    ]),
    ("💳", "Solitaire Credit Card", [
        "Invite-only premium metal credit card",
        "10 Air Miles/₹100 on eligible flight & hotel bookings through Kotak Unbox",
        "3 Air Miles/₹100 on other eligible spends",
        "0% forex markup on international spends",
        "Complimentary airport lounge access for customer/family",
        "1% cash withdrawal charge at ATMs worldwide",
        "Annual fee waived for Solitaire customers while eligibility is maintained"
    ]),
    ("💰", "Lending & Liquidity", [
        "Pre-approved home loan up to ₹7.5 crore",
        "Pre-approved credit line up to ₹25 lakh",
        "Quick loan solutions",
        "Preferential lending propositions"
    ]),
    ("📈", "Wealth Management", [
        "Personalised investment solutions",
        "Access/referrals to alternate investments including AIFs",
        "Mutual funds, equities and other investment solutions",
        "Global investment/remittance opportunities",
        "Overseas investment facility up to USD 2,50,000 annually",
        "Outward remittances up to USD 50,000 through the stated facility"
    ]),
    ("✈️", "Lifestyle", [
        "Premium travel benefits",
        "Hotel & flight privileges",
        "Exclusive events/experiences",
        "Concierge-style relationship support"
    ])
]

fix_expandable_intro('experience_solitaire_dashboard_new.html', 'Kotak Solitaire', solitaire_intro, solitaire_elig, solitaire_cats)
