import os
from bs4 import BeautifulSoup

def make_intro_expandable(filename, program_name, intro_text, eligibility_text, benefits_list):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    panel_intro = soup.find(id='panel-intro')
    if panel_intro:
        # Find the h3 containing the program introduction
        prog_header = None
        for h3 in panel_intro.find_all('h3'):
            if "Program Introduction" in h3.text:
                prog_header = h3
                break
                
        if prog_header:
            # The div following the header has the text. We will clear both and replace.
            prog_div = prog_header.find_next_sibling('div')
            prog_header.decompose()
            if prog_div:
                prog_div.decompose()
                
            # Create expandable section
            details = soup.new_tag('details', style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);")
            
            summary = soup.new_tag('summary', style="padding: 16px; font-weight: 700; color: #0f172a; font-size: 1.15rem; cursor: pointer; outline: none; list-style: none; display: flex; justify-content: space-between; align-items: center;")
            # Inner HTML for summary to include a custom arrow icon if desired, but native is fine. We will use native for simplicity but hide default marker and add a custom one.
            summary_html = f'''
                <span style="display: flex; align-items: center; gap: 8px;">
                    <svg fill="none" height="20" stroke="#3b82f6" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path><path d="M12 8v8"></path><path d="M8 12h8"></path></svg>
                    {program_name} Program Introduction
                </span>
            '''
            summary.append(BeautifulSoup(summary_html, 'html.parser'))
            
            content_div = soup.new_tag('div', style="padding: 0 16px 16px 16px; color: #475569; line-height: 1.6; font-size: 0.95rem; border-top: 1px solid #f1f5f9; margin-top: 8px; padding-top: 16px;")
            
            intro_p = soup.new_tag('p', style="margin-bottom: 12px;")
            intro_p.string = intro_text
            content_div.append(intro_p)
            
            # List-wise all benefits
            benefits_title = soup.new_tag('p', style="font-weight: 600; color: #0f172a; margin-bottom: 8px;")
            benefits_title.string = "Key Benefits:"
            content_div.append(benefits_title)
            
            ul = soup.new_tag('ul', style="padding-left: 20px; margin-bottom: 16px; line-height: 1.8;")
            for benefit in benefits_list:
                li = soup.new_tag('li', style="margin-bottom: 4px;")
                # Bold the first word or just use a nice icon bullet
                li_html = f'<span style="color: #3b82f6; margin-right: 6px;">✓</span> {benefit}'
                li.append(BeautifulSoup(li_html, 'html.parser'))
                ul.append(li)
            content_div.append(ul)
            
            elig_p = soup.new_tag('p', style="margin-bottom: 0; background: #f8fafc; padding: 12px; border-radius: 6px; border-left: 3px solid #64748b;")
            elig_p.append(BeautifulSoup(f'<strong>Eligibility:</strong> {eligibility_text}', 'html.parser'))
            content_div.append(elig_p)
            
            details.append(summary)
            details.append(content_div)
            
            # Add a style to hide the default summary marker
            style = soup.new_tag('style')
            style.string = "details > summary::-webkit-details-marker { display: none; }"
            if not soup.find('style', string="details > summary::-webkit-details-marker { display: none; }"):
                soup.head.append(style)
            
            panel_intro.append(details)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filename}")


solitaire_intro = "Kotak Solitaire is Kotak Mahindra Bank’s invite-only premium/private banking proposition designed for affluent and HNI customers and their families."
solitaire_elig = "Generally, salaried customers require ₹75 lakh+ Relationship Value (RV), while self-employed customers require ₹1 crore+ RV across family relationships."
solitaire_benefits = [
    "Wealth Management",
    "Premium Banking",
    "Exclusive Credit Cards",
    "Preferential Lending",
    "Lifestyle Privileges",
    "Dedicated Relationship Support"
]
make_intro_expandable('experience_solitaire_dashboard_new.html', 'Kotak Solitaire', solitaire_intro, solitaire_elig, solitaire_benefits)

privy_plus_intro = "Kotak Privy+ is the higher tier of the Privy proposition, targeted at customers with a stronger relationship with Kotak."
privy_plus_elig = "Current Kotak information indicates ₹30 lakh Relationship Value or ₹3 lakh+ monthly salary credit for the Privy+ proposition."
privy_plus_benefits = [
    "Premium Banking",
    "Wealth/Investment Access",
    "Premium Cards",
    "Insurance",
    "Significantly Higher Pre-Qualified Lending Limits"
]
make_intro_expandable('experience_privy_plus_dashboard_new.html', 'Kotak Privy+', privy_plus_intro, privy_plus_elig, privy_plus_benefits)

privy_intro = "Kotak Privy is a premium banking programme for affluent customers, built around an integrated proposition."
privy_elig = "The current Privy proposition starts at approximately ₹10 lakh Relationship Value or ₹1–3 lakh monthly salary credit, depending on the eligibility route."
privy_benefits = [
    "Integrated Banking",
    "Investment",
    "Insurance",
    "Lending Proposition"
]
make_intro_expandable('experience_privy_dashboard_new.html', 'Kotak Privy', privy_intro, privy_elig, privy_benefits)
