import os
from bs4 import BeautifulSoup

def update_pitches(filename, program_name, intro_pitch, cc_pitch, loans_pitch, inv_pitch):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # RM Intro (common) + Program Intro
    panel_intro = soup.find(id='panel-intro')
    if panel_intro:
        # Clear existing content and rewrite it cleanly
        panel_intro.clear()
        
        header = soup.new_tag('h2', style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 16px;")
        header.string = "Introduction to RM and Program"
        panel_intro.append(header)
        
        # RM Intro Box
        rm_box = soup.new_tag('div', style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px; margin-bottom: 24px; border-radius: 0 8px 8px 0;")
        rm_text = """
        <p style="color: #334155; margin-bottom: 12px;"><strong>Good morning, Sir/Ma’am. I’m Vaibhav Kapoor, your dedicated Relationship Manager at Kotak Mahindra Bank.</strong></p>
        <p style="color: #475569; margin-bottom: 8px;">I’ll be your single point of contact for all your banking and wealth requirements going forward.</p>
        <p style="color: #475569; margin-bottom: 8px;">My role is not just to assist you whenever you need something, but to understand your overall financial requirements and proactively help you with the right solutions—whether it’s investments, lending, insurance, cards, or any other banking requirement.</p>
        <p style="color: #475569; margin-bottom: 8px;">I’d also like to understand how you currently use your Kotak relationship, what’s working well for you, and where you feel there is scope for improvement.</p>
        <p style="color: #475569; margin-bottom: 8px;">My objective is very simple—to make your banking relationship with Kotak more seamless, personalised and valuable.</p>
        <p style="color: #475569; margin-bottom: 0;">Going forward, please feel free to reach out to me directly for anything you need. I’ll be happy to take ownership and coordinate it for you.</p>
        """
        rm_box.append(BeautifulSoup(rm_text, 'html.parser'))
        panel_intro.append(rm_box)
        
        # Program Pitch
        prog_header = soup.new_tag('h3', style="font-weight: 700; color: #0f172a; margin-bottom: 12px; font-size: 1.15rem;")
        prog_header.string = f"{program_name} Program Introduction"
        panel_intro.append(prog_header)
        
        prog_box = soup.new_tag('div', style="color: #475569; line-height: 1.6; font-size: 0.95rem;")
        prog_box.append(BeautifulSoup(intro_pitch, 'html.parser'))
        panel_intro.append(prog_box)
        
    def set_pitch_content(panel_id, content_html):
        panel = soup.find(id=panel_id)
        if panel:
            pitch_tab = panel.find(class_='inner-tab-content-pitches')
            if pitch_tab:
                pitch_tab.clear()
                wrapper = soup.new_tag('div', style="background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 12px; padding: 24px; color: #334155;")
                wrapper.append(BeautifulSoup(content_html, 'html.parser'))
                pitch_tab.append(wrapper)

    set_pitch_content('panel-cc', cc_pitch)
    set_pitch_content('panel-assets', loans_pitch)
    set_pitch_content('panel-investments', inv_pitch)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filename}")


# --- SOLITAIRE ---
solitaire_intro = """
<p style="margin-bottom: 12px;">Kotak Solitaire is Kotak Mahindra Bank’s invite-only premium/private banking proposition designed for affluent and HNI customers and their families. It combines wealth management, premium banking, exclusive credit cards, preferential lending and lifestyle privileges with dedicated relationship support.</p>
<p><strong>Eligibility:</strong> Generally, salaried customers require ₹75 lakh+ Relationship Value (RV), while self-employed customers require ₹1 crore+ RV across family relationships.</p>
"""

solitaire_cc = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Solitaire Credit Card Features</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Invite-only premium metal credit card</li>
    <li>10 Air Miles/₹100 on eligible flight & hotel bookings through Kotak Unbox</li>
    <li>3 Air Miles/₹100 on other eligible spends</li>
    <li>0% forex markup on international spends</li>
    <li>Complimentary airport lounge access for customer/family</li>
    <li>1% cash withdrawal charge at ATMs worldwide</li>
    <li>Annual fee waived for Solitaire customers while eligibility is maintained</li>
</ul>
"""

solitaire_loans = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Lending & Liquidity Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Pre-approved home loan up to ₹7.5 crore</li>
    <li>Pre-approved credit line up to ₹25 lakh</li>
    <li>Quick loan solutions</li>
    <li>Preferential lending propositions</li>
</ul>
"""

solitaire_inv = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Wealth Management Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Personalised investment solutions</li>
    <li>Access/referrals to alternate investments including AIFs</li>
    <li>Mutual funds, equities and other investment solutions</li>
    <li>Global investment/remittance opportunities</li>
    <li>Overseas investment facility up to USD 2,50,000 annually</li>
    <li>Outward remittances up to USD 50,000 through the stated facility</li>
</ul>
"""

update_pitches('experience_solitaire_dashboard_new.html', 'Kotak Solitaire', solitaire_intro, solitaire_cc, solitaire_loans, solitaire_inv)


# --- PRIVY ---
privy_intro = """
<p style="margin-bottom: 12px;">Kotak Privy is a premium banking programme for affluent customers, built around an integrated banking + investment + insurance + lending proposition.</p>
<p><strong>Eligibility:</strong> The current Privy proposition starts at approximately ₹10 lakh Relationship Value or ₹1–3 lakh monthly salary credit, depending on the eligibility route.</p>
"""

privy_cc = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Kotak Air Credit Card Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Up to 3 Air Miles/₹100</li>
    <li>Up to 4 complimentary domestic lounge visits, subject to applicable conditions</li>
</ul>
"""

privy_loans = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Privy Loans Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Pre-approved home loan up to ₹85 lakh</li>
    <li>Home-loan protection plan option</li>
    <li>Pre-approved auto loan up to ₹25 lakh</li>
    <li>Other pre-qualified lending solutions</li>
</ul>
"""

privy_inv = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Privy Banking & Investments</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Premium Privy savings account</li>
    <li>4-in-1 account combining: Savings, ActiveMoney, Investments, and Trading</li>
    <li>ActivMoney for FD-like returns on idle funds</li>
    <li>Priority banking service</li>
</ul>
"""

update_pitches('experience_privy_dashboard_new.html', 'Kotak Privy', privy_intro, privy_cc, privy_loans, privy_inv)


# --- PRIVY+ ---
privy_plus_intro = """
<p style="margin-bottom: 12px;">Kotak Privy+ is the higher tier of the Privy proposition, targeted at customers with a stronger relationship with Kotak. It combines premium banking, wealth/investment access, premium cards, insurance and significantly higher pre-qualified lending limits.</p>
<p><strong>Eligibility:</strong> Current Kotak information indicates ₹30 lakh Relationship Value or ₹3 lakh+ monthly salary credit for the Privy+ proposition.</p>
"""

privy_plus_cc = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Kotak Air+ Credit Card Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Up to 5 Air Miles/₹100</li>
    <li>2% forex markup</li>
    <li>Complimentary global lounge access, subject to applicable conditions</li>
</ul>
"""

privy_plus_loans = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Privy+ Lending Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Pre-approved home loan up to ₹1 crore</li>
    <li>Pre-approved auto loan up to ₹40 lakh</li>
    <li>Pre-approved personal loan up to ₹15 lakh</li>
    <li>Protection-plan options on eligible loans</li>
    <li><strong>Short-Term Liquidity:</strong> Kotak Mid-Month Advance - short-term salary-linked borrowing designed for temporary cash-flow requirements.</li>
</ul>
"""

privy_plus_inv = """
<h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; text-align: left;">Privy+ Banking & Investments Pitch</h3>
<ul style="text-align: left; line-height: 1.8; padding-left: 20px;">
    <li>Integrated 4-in-1 account (Savings + ActiveMoney + Investments + Trading)</li>
    <li>Seamless investment/trading access</li>
    <li>Wealth/investment solutions</li>
    <li>Preferential service</li>
</ul>
"""

update_pitches('experience_privy_plus_dashboard_new.html', 'Kotak Privy+', privy_plus_intro, privy_plus_cc, privy_plus_loans, privy_plus_inv)
