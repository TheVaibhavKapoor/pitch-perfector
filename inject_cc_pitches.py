import os
from bs4 import BeautifulSoup

def update_cc_pitch(filename, new_content):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    panel_cc = soup.find(id='panel-cc')
    if panel_cc:
        pitch_tab = panel_cc.find(class_='inner-tab-content-pitches')
        if pitch_tab:
            pitch_tab.clear()
            wrapper = soup.new_tag('div', style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);")
            wrapper.append(BeautifulSoup(new_content, 'html.parser'))
            pitch_tab.append(wrapper)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filename}")

killer_question = """
<h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">The Killer RM Question</h3>
<div style="text-align: left; margin-bottom: 24px; color: #475569; font-size: 0.95rem;">
    <p style="margin-bottom: 12px;">After explaining the relevant card, don't immediately ask: <em>“Sir, shall I apply for the card?”</em></p>
    <p style="margin-bottom: 12px;">Instead:</p>
    <div style="background: #eef2ff; padding: 16px; border-radius: 8px; margin-bottom: 12px; color: #1e40af; font-weight: 600; border-left: 4px solid #3b82f6;">
        “Sir, roughly how much would you say you spend on your credit cards every month, and how much of that would be travel, international and regular lifestyle spends?”
    </div>
    <p style="margin-bottom: 0;">Then you can calculate the customer's potential annual value and make the recommendation based on their spending rather than pushing a product.</p>
</div>
"""

def generate_table(rows):
    html = '<table style="width: 100%; text-align: left; border-collapse: collapse; margin-bottom: 16px; font-size: 0.9rem;">'
    html += '<thead style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;"><tr>'
    html += '<th style="padding: 12px; font-weight: 600; color: #475569;">Feature</th>'
    html += '<th style="padding: 12px; font-weight: 600; color: #475569;">Details</th>'
    html += '</tr></thead><tbody>'
    for i, (k, v) in enumerate(rows):
        bg = "#ffffff" if i % 2 == 0 else "#f8fafc"
        html += f'<tr style="background: {bg}; border-bottom: 1px solid #e2e8f0;">'
        html += f'<td style="padding: 12px; font-weight: 500; color: #0f172a; width: 35%;">{k}</td>'
        html += f'<td style="padding: 12px; color: #475569;">{v}</td>'
        html += '</tr>'
    html += '</tbody></table>'
    return html


# --- SOLITAIRE ---
solitaire_pitch = f"""
<div style="margin-bottom: 32px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Customer Pitch: Solitaire Credit Card</h3>
    <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px; text-align: left; margin-bottom: 24px; border-radius: 0 8px 8px 0; font-style: italic; color: #334155; font-size: 0.95rem;">
        <p style="margin-bottom: 12px;">“Sir/Ma’am, since you are part of the Solitaire relationship, I’d specifically like to highlight the Solitaire Credit Card.</p>
        <p style="margin-bottom: 12px;">This is designed more as a premium lifestyle and travel card, rather than just a regular rewards credit card.</p>
        <p style="margin-bottom: 12px;">The biggest advantage is that your travel spends can earn 10 Air Miles for every ₹100 when you book flights and hotels through Kotak Unbox, while your other eligible spends earn 3 Air Miles per ₹100.</p>
        <p style="margin-bottom: 12px;">What makes the card particularly valuable for a frequent traveller is the unlimited domestic and international lounge access, including for your add-on cardholders. You also get zero forex markup, which can be quite meaningful if you spend internationally.</p>
        <p style="margin-bottom: 12px;">And because the card is part of the Solitaire proposition, there is no joining or annual fee as long as you continue to remain eligible for Solitaire.</p>
        <p style="margin-bottom: 12px;">So rather than looking at this simply as another credit card, I would look at it as a card that can consolidate your travel, lifestyle and international spends while giving you premium privileges.</p>
        <p style="margin-bottom: 0;">Based on your spending pattern, I can also help you understand whether you would actually benefit from moving your spends to this card.”</p>
    </div>
</div>

<div style="margin-bottom: 32px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Card Positioning</h3>
    <div style="text-align: left; color: #475569; font-size: 0.95rem;">
        <p style="margin-bottom: 12px; font-weight: 600; color: #7e22ce;">🟣 Solitaire → SOLITAIRE</p>
        <p style="margin-bottom: 12px; font-style: italic;">“A premium lifestyle + travel card where the privileges matter as much as the rewards.”</p>
        <p style="font-weight: 600; margin-bottom: 8px;">Best for:</p>
        <ul style="padding-left: 20px; line-height: 1.6;">
            <li>HNI / affluent customer</li>
            <li>High card spends</li>
            <li>Frequent international travel</li>
            <li>Family/add-on usage</li>
            <li>International spends (Wants zero forex)</li>
            <li>Wants unlimited lounge</li>
            <li>Values concierge & premium lifestyle privileges</li>
        </ul>
        <div style="margin-top: 16px; background: #f8fafc; padding: 12px; border-radius: 8px; font-size: 0.85rem;">
            <strong>Example scenario:</strong> ₹3–5 lakh/month spends + frequent international travel + family travel → Solitaire becomes a much stronger proposition.
        </div>
    </div>
</div>

{killer_question}

<div style="margin-bottom: 16px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Key Features: Solitaire</h3>
    {generate_table([
        ("Card type", "Metal card"),
        ("Travel spends", "10 Air Miles / ₹100 via Kotak Unbox"),
        ("Other eligible spends", "3 Air Miles / ₹100"),
        ("Air Mile travel value", "1 Air Mile = ₹1 on eligible travel bookings"),
        ("Domestic lounge", "Unlimited"),
        ("International lounge", "Unlimited"),
        ("Add-on lounge", "Unlimited for add-on cardholders"),
        ("Guest lounge", "2 domestic + 2 international/year"),
        ("Forex markup", "0%"),
        ("ATM cash withdrawal", "1%, with no interest/APR till payment due date"),
        ("Fuel surcharge waiver", "1%, up to ₹10,000/year"),
        ("Add-ons", "Up to 3, for eligible immediate family"),
        ("Joining fee", "Nil"),
        ("Annual fee", "Nil while Solitaire eligible"),
        ("Concierge", "Travel, lifestyle, reservations, visa assistance, airport concierge etc."),
        ("Lifestyle", "Solitaire Table / District by Zomato privileges")
    ])}
    <p style="font-size: 0.8rem; color: #64748b; text-align: left; line-height: 1.5;">*The Air Miles earned on travel through Kotak Unbox are capped at 1 lakh accelerated miles per statement cycle, after which the base 3 miles/₹100 continues; several categories are excluded from earning.</p>
</div>
"""
update_cc_pitch('experience_solitaire_dashboard_new.html', solitaire_pitch)


# --- PRIVY PLUS ---
privy_plus_pitch = f"""
<div style="margin-bottom: 32px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Customer Pitch: Kotak Air+ Credit Card</h3>
    <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px; text-align: left; margin-bottom: 24px; border-radius: 0 8px 8px 0; font-style: italic; color: #334155; font-size: 0.95rem;">
        <p style="margin-bottom: 12px;">“Sir/Ma’am, for Privy+ customers, another card I would recommend looking at is the Kotak Air+ Credit Card, particularly if you travel regularly.</p>
        <p style="margin-bottom: 12px;">The proposition is quite straightforward — you earn more when you travel and continue earning on your everyday spends.</p>
        <p style="margin-bottom: 12px;">You earn 5 Air Miles for every ₹100 on flight and hotel bookings through Kotak Unbox, and 2 Air Miles per ₹100 on other eligible purchases.</p>
        <p style="margin-bottom: 12px;">You also get 4 domestic and 2 international lounge visits every year, along with a 2% forex markup, which makes it a fairly well-rounded travel card.</p>
        <p style="margin-bottom: 12px;">There is also a 2,500 Air Miles welcome benefit and another 2,500 on renewal, subject to the applicable conditions.</p>
        <p style="margin-bottom: 0;">So if you already have meaningful monthly spends and travel expenditure, instead of simply using a standard credit card, we can route the relevant spends through Air+ and convert those spends into travel value.”</p>
    </div>
</div>

<div style="margin-bottom: 32px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Card Positioning</h3>
    <div style="text-align: left; color: #475569; font-size: 0.95rem;">
        <p style="margin-bottom: 12px; font-weight: 600; color: #2563eb;">🔵 Privy+ → AIR+</p>
        <p style="margin-bottom: 12px; font-style: italic;">“A stronger travel card for customers with higher spends and more frequent travel.”</p>
        <p style="font-weight: 600; margin-bottom: 8px;">Best for:</p>
        <ul style="padding-left: 20px; line-height: 1.6;">
            <li>Higher monthly spends</li>
            <li>Frequent domestic/international travel</li>
            <li>Wants higher Air Mile accumulation</li>
            <li>Wants international lounge access</li>
            <li>Will actually utilise travel benefits</li>
        </ul>
        <div style="margin-top: 16px; background: #f8fafc; padding: 12px; border-radius: 8px; font-size: 0.85rem;">
            <strong>Example scenario:</strong> ₹1 lakh/month spends + ₹3 lakh annual travel spend → Air+ may make more sense.
        </div>
    </div>
</div>

{killer_question}

<div style="margin-bottom: 16px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Key Features: Air+</h3>
    {generate_table([
        ("Travel spends", "5 Air Miles / ₹100 via Kotak Unbox"),
        ("Other eligible spends", "2 Air Miles / ₹100"),
        ("Welcome benefit", "2,500 Air Miles"),
        ("Renewal benefit", "2,500 Air Miles"),
        ("Travel redemption", "1 Air Mile = ₹1"),
        ("Domestic lounge", "4/year"),
        ("International lounge", "2/year"),
        ("Forex markup", "2%"),
        ("Fuel surcharge", "1% waiver"),
        ("Fuel waiver cap", "₹4,500/year"),
        ("Joining fee", "₹3,000 + GST"),
        ("Annual fee", "₹3,000 + GST"),
        ("Air Miles transfer", "Airline & hotel partners"),
        ("Air Miles expiry", "3 years")
    ])}
    <p style="font-size: 0.8rem; color: #64748b; text-align: left; line-height: 1.5;">*Air+ travel acceleration is capped at 15,000 Air Miles per statement cycle; base earning continues thereafter. Certain categories, including fuel, rent, utilities/telecom, insurance, education, government, EMI and international transactions, don't earn Air Miles.</p>
</div>
"""
update_cc_pitch('experience_privy_plus_dashboard_new.html', privy_plus_pitch)


# --- PRIVY ---
privy_pitch = f"""
<div style="margin-bottom: 32px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Customer Pitch: Kotak Air Credit Card</h3>
    <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px; text-align: left; margin-bottom: 24px; border-radius: 0 8px 8px 0; font-style: italic; color: #334155; font-size: 0.95rem;">
        <p style="margin-bottom: 12px;">“Sir/Ma’am, for your Privy relationship, we also have the Kotak Air Credit Card.</p>
        <p style="margin-bottom: 12px;">This is positioned as a simple travel-rewards card — you don't need to have extremely high spends to start getting value from it.</p>
        <p style="margin-bottom: 12px;">You earn 3 Air Miles for every ₹100 spent on flights and hotels through Kotak Unbox, and 1 Air Mile per ₹100 on other eligible purchases.</p>
        <p style="margin-bottom: 12px;">You also get 4 complimentary domestic lounge visits every year, along with 1,000 Air Miles as a welcome benefit and another 1,000 on renewal.</p>
        <p style="margin-bottom: 12px;">So if your objective is to get a straightforward travel card with lounge access and earn Air Miles on your regular spends, this is a good fit within the Privy proposition.</p>
        <p style="margin-bottom: 0;">I can look at your existing card spends and travel pattern and tell you whether shifting some of those spends to the Kotak Air Card would make financial sense.”</p>
    </div>
</div>

<div style="margin-bottom: 32px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Card Positioning</h3>
    <div style="text-align: left; color: #475569; font-size: 0.95rem;">
        <p style="margin-bottom: 12px; font-weight: 600; color: #16a34a;">🟢 Privy → AIR</p>
        <p style="margin-bottom: 12px; font-style: italic;">“A simple entry-level travel rewards proposition.”</p>
        <p style="font-weight: 600; margin-bottom: 8px;">Best for:</p>
        <ul style="padding-left: 20px; line-height: 1.6;">
            <li>Moderate card spends</li>
            <li>Occasional traveller</li>
            <li>Wants lounge access</li>
            <li>Wants basic Air Miles</li>
            <li>Lower annual fee</li>
        </ul>
    </div>
</div>

{killer_question}

<div style="margin-bottom: 16px;">
    <h3 style="color: #0f172a; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Key Features: Air</h3>
    {generate_table([
        ("Travel spends", "3 Air Miles / ₹100 via Kotak Unbox"),
        ("Other eligible spends", "1 Air Mile / ₹100"),
        ("Welcome benefit", "1,000 Air Miles"),
        ("Renewal benefit", "1,000 Air Miles"),
        ("Travel redemption", "1 Air Mile = ₹1"),
        ("Voucher redemption", "1 Air Mile = ₹0.50"),
        ("Domestic lounge", "4/year"),
        ("Forex", "Applicable standard card markup"),
        ("Fuel surcharge", "1% waiver"),
        ("Joining fee", "₹999 + GST"),
        ("Annual fee", "₹999 + GST"),
        ("Air Miles transfer", "Airline & hotel partners"),
        ("Air Miles expiry", "3 years")
    ])}
    <p style="font-size: 0.8rem; color: #64748b; text-align: left; line-height: 1.5;">*Current Kotak information states that Air Miles can be redeemed through Kotak Unbox for flights/hotels, vouchers or transferred to partner programmes.</p>
</div>
"""
update_cc_pitch('experience_privy_dashboard_new.html', privy_pitch)
