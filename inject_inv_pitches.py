import os
from bs4 import BeautifulSoup

def update_inv_pitch(filename, new_content):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    panel_inv = soup.find(id='panel-investments')
    if panel_inv:
        pitch_tab = panel_inv.find(class_='inner-tab-content-pitches')
        if pitch_tab:
            pitch_tab.clear()
            wrapper = soup.new_tag('div', style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); height: 600px; overflow-y: auto;")
            wrapper.append(BeautifulSoup(new_content, 'html.parser'))
            pitch_tab.append(wrapper)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filename}")

def pitch_box(title, text_html):
    return f"""
    <div style="margin-bottom: 24px;">
        <h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600;">{title}</h4>
        <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px; text-align: left; border-radius: 0 8px 8px 0; font-style: italic; color: #334155; font-size: 0.95rem;">
            {text_html}
        </div>
    </div>
    """

def question_box(title, questions_html):
    return f"""
    <div style="margin-bottom: 24px; text-align: left;">
        <h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600;">{title}</h4>
        <div style="background: #eef2ff; padding: 16px; border-radius: 8px; color: #1e40af; font-weight: 600; border-left: 4px solid #3b82f6; font-size: 0.95rem;">
            {questions_html}
        </div>
    </div>
    """

def section_header(number, title):
    return f'<h3 style="color: #0f172a; margin-top: 32px; margin-bottom: 16px; font-size: 1.15rem; text-align: left; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;"><span style="color: #3b82f6; margin-right: 8px;">{number}.</span>{title}</h3>'

def bullet_list(items):
    html = '<ul style="text-align: left; line-height: 1.6; padding-left: 20px; color: #475569; font-size: 0.95rem; margin-bottom: 24px;">'
    for item in items:
        html += f'<li style="margin-bottom: 4px;">{item}</li>'
    html += '</ul>'
    return html

def comparison_table():
    rows = [
        ("What is it?", "3-in-1 account", "Digital investment/trading platform"),
        ("Bank Account", "✓", "Through linked ecosystem"),
        ("Demat", "✓", "✓"),
        ("Trading", "✓", "✓"),
        ("Stocks", "✓", "✓"),
        ("Mutual Funds", "✓", "✓"),
        ("IPO", "✓", "✓"),
        ("Main proposition", "Integration", "Digital investing/trading"),
        ("Best for", "Customers wanting one integrated setup", "Active/self-directed investors"),
        ("RM pitch", "“Connect your banking & investments”", "“Manage your investments digitally”")
    ]
    html = '<table style="width: 100%; text-align: left; border-collapse: collapse; margin-bottom: 24px; font-size: 0.9rem;">'
    html += '<thead style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;"><tr>'
    html += '<th style="padding: 12px; font-weight: 600; color: #475569; width: 30%;">Feature</th>'
    html += '<th style="padding: 12px; font-weight: 600; color: #1e3a8a; width: 35%;">Trinity</th>'
    html += '<th style="padding: 12px; font-weight: 600; color: #b91c1c; width: 35%;">NEO</th>'
    html += '</tr></thead><tbody>'
    for i, (feat, trin, neo) in enumerate(rows):
        bg = "#ffffff" if i % 2 == 0 else "#f8fafc"
        html += f'<tr style="background: {bg}; border-bottom: 1px solid #e2e8f0;">'
        html += f'<td style="padding: 12px; font-weight: 500; color: #0f172a;">{feat}</td>'
        html += f'<td style="padding: 12px; color: #475569;">{trin}</td>'
        html += f'<td style="padding: 12px; color: #475569;">{neo}</td>'
        html += '</tr>'
    html += '</tbody></table>'
    return html


inv_html = f"""
{section_header('🔥', 'THE BEST INVESTMENT PITCH FOR YOU AS RM (Recommended)')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">For your Privy / Privy+ / Solitaire customers, don't randomly pitch MF, Trinity and NEO. Do an Investment Health Check.</p>

<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Investment Health Check</h4>
<div style="background: #f1f5f9; padding: 16px; border-radius: 8px; text-align: left; margin-bottom: 24px;">
    <p style="color: #334155; margin-bottom: 12px;"><strong>Opening:</strong> <em>“Sir/Ma’am, apart from your banking requirements, I'd also like to understand how you currently manage your investments.”</em></p>
    <p style="color: #0f172a; font-weight: 600; margin-bottom: 8px;">Then ask:</p>
    <ol style="padding-left: 20px; color: #475569; font-size: 0.95rem; margin-bottom: 16px; line-height: 1.6;">
        <li>“Do you invest directly in equities?”</li>
        <li>“Do you have mutual funds?”</li>
        <li>“Are your investments primarily with Kotak or spread across different platforms?”</li>
        <li>“Do you manage your portfolio yourself or work with an advisor?”</li>
        <li>“What would you say is your primary objective—wealth creation, regular income, capital preservation or a specific future goal?”</li>
    </ol>
    
    <p style="color: #0f172a; font-weight: 600; margin-bottom: 8px;">Then map:</p>
    <ul style="padding-left: 20px; color: #475569; font-size: 0.95rem; margin-bottom: 0; line-height: 1.6; list-style-type: none;">
        <li>Customer has no market investments → <strong style="color: #3b82f6;">MF / SIP</strong></li>
        <li>Customer has MF but scattered across platforms → <strong style="color: #3b82f6;">Portfolio consolidation / Kotak Investment Account</strong></li>
        <li>Customer invests in stocks through another broker → <strong style="color: #3b82f6;">Trinity + NEO</strong></li>
        <li>Customer actively trades → <strong style="color: #3b82f6;">Trinity + NEO</strong></li>
        <li>Customer has large idle savings → <strong style="color: #3b82f6;">Asset allocation discussion → MF / debt / equity</strong> based on suitability</li>
        <li>HNI with ₹50L+ investments → Don't stop at MF. Move the conversation toward: <strong style="color: #3b82f6;">MF → Equity → Bonds → PMS → AIF → structured/alternate investments</strong></li>
    </ul>
</div>

<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Your One-Line Positioning</h4>
<div style="text-align: left; margin-bottom: 24px; color: #475569; font-size: 0.95rem;">
    <p style="margin-bottom: 8px;"><strong>Trinity:</strong> “One ecosystem to Save, Trade & Invest.”</p>
    <p style="margin-bottom: 8px;"><strong>Mutual Funds:</strong> “Professionally managed diversification for long-term wealth creation.”</p>
    <p style="margin-bottom: 16px;"><strong>NEO:</strong> “A digital platform for customers who want to actively manage their investments and trades.”</p>
</div>

{pitch_box("Your RM Role", '''
<p style="margin-bottom: 0;">“I don't want to sell you an investment product. I want to understand your existing portfolio and identify where your money can be better structured according to your goals, liquidity needs and risk profile.”</p>
<p style="font-size: 0.85rem; color: #475569; font-weight: 400; font-style: italic; margin-top: 8px;">(That last line is the premium-RM positioning I'd use with Solitaire/Privy+ clients.)</p>
''')}


<hr style="border: 0; border-top: 2px dashed #cbd5e1; margin: 32px 0;">

{section_header('1', 'KOTAK TRINITY — 3-in-1 ACCOUNT')}
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, I also noticed that we can make your investment experience much more seamless through Kotak Trinity.</p>
<p style="margin-bottom: 12px;">Trinity essentially brings your Savings Account, Demat Account and Trading Account together.</p>
<p style="margin-bottom: 12px;">So instead of maintaining separate banking and investment setups, your Kotak savings account is directly linked to your trading and demat account.</p>
<p style="margin-bottom: 12px;">The biggest convenience is the seamless movement of funds from your savings account to your trading account, along with the ability to invest in stocks, bonds and IPOs through the same ecosystem.</p>
<p style="margin-bottom: 0;">So if you actively invest in the markets, I would recommend having Trinity because it gives you one integrated relationship for saving, investing and trading.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Key Features / Benefits</h4>
{bullet_list([
    "<strong>3-in-1 structure:</strong> Savings Account (KMB) + Demat Account (KS) + Trading Account (KS)",
    "<strong>Investment access:</strong> Equity/stocks, Bonds, IPOs, ASBA, Mutual Funds",
    "<strong>Convenience:</strong> Seamless transfer between Savings → Trading, Single integrated ecosystem, Easier settlement of trades",
    "Digital account opening/upgrade",
    "<strong>Pricing:</strong> Current Kotak information advertises ₹0 account-opening fee, varying pricing plans, flat ₹10/order for Intraday and F&O under applicable plans"
])}
{question_box("Strong RM Question", '''
<p style="margin-bottom: 8px;">“Sir, do you currently maintain your Demat and trading account with another broker?”</p>
<p style="margin-bottom: 8px; color: #475569; font-weight: 400;">If yes:</p>
<p style="margin-bottom: 8px;">“And do you usually transfer money from your bank account to the broker before investing?”</p>
<p style="margin-bottom: 8px; color: #475569; font-weight: 400;">Then:</p>
<p style="margin-bottom: 0;">“That's exactly where Trinity can simplify the experience for you.”</p>
''')}

{section_header('2', 'MUTUAL FUNDS')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">Don't start with <em>“Sir, we have mutual funds.”</em> Start with the customer's idle money / goals / existing portfolio.</p>
{pitch_box("Recommended Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, one area I would like to review with you is your investment portfolio.</p>
<p style="margin-bottom: 12px;">A lot of customers have money sitting in savings accounts or FDs, while their long-term wealth creation happens separately through mutual funds.</p>
<p style="margin-bottom: 12px;">What I would like to do is understand your goals, investment horizon and risk appetite and then see whether a portion of your surplus can be allocated towards market-linked investments.</p>
<p style="margin-bottom: 12px;">The advantage of mutual funds is that you don't have to individually research and manage every stock. The portfolio is managed by professional fund managers and can give you diversification across companies and sectors.</p>
<p style="margin-bottom: 12px;">We can structure it through SIP, lump-sum investment or STP, depending on your cash flow and objective.</p>
<p style="margin-bottom: 0;">More importantly, I don't want to simply recommend a fund. I'd first like to look at what you already hold and identify whether there is any concentration, duplication or asset-allocation gap.”</p>
<p style="font-size: 0.85rem; color: #475569; font-weight: 400; font-style: italic; margin-top: 8px;">(That last line is excellent for affluent clients.)</p>
''')}

<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">MF Features / Benefits</h4>
{bullet_list([
    "<strong>Investment Options:</strong> SIP, Lump-sum, STP, Systematic instructions",
    "<strong>Categories:</strong> Equity funds, Debt funds, Hybrid funds based on risk profile",
    "Kotak's investment account currently allows customers to transact in mutual funds from 25+ fund houses."
])}

<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Portfolio Management (Kotak Investment Account)</h4>
{bullet_list([
    "Consolidated MF portfolio view",
    "Daily NAV tracking & Portfolio-performance tracking",
    "Recommended funds",
    "Transaction reports & Capital-gain/loss reports",
    "Nomination facility",
    "Online purchase/redemption, SIP/STP/standing instructions"
])}

{question_box("Why SIP?", '''
<p style="margin-bottom: 12px; font-weight: 400; color: #475569;">Pitch it like this:</p>
<p style="margin-bottom: 12px;">“Instead of trying to identify the perfect time to enter the market, SIP allows you to invest a fixed amount regularly across different market conditions. It creates discipline and helps average your purchase cost over time.”</p>
<p style="margin-bottom: 0; font-weight: 400; color: #475569;">Kotak highlights discipline, rupee-cost averaging and avoiding the need to time the market as key SIP benefits.</p>
''')}

{section_header('3', 'KOTAK NEO')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">This one should be positioned very differently from Trinity. Trinity = account architecture. NEO = investment/trading platform.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, if you are someone who actively follows the market or manages your own investments, I'd also recommend looking at Kotak NEO.</p>
<p style="margin-bottom: 12px;">NEO is Kotak Securities' digital investment and trading platform where you can manage your market investments digitally.</p>
<p style="margin-bottom: 12px;">You get access to stocks, mutual funds, IPOs and trading capabilities, along with research and tools designed for more active investors.</p>
<p style="margin-bottom: 12px;">So if you prefer taking your own investment decisions rather than having everything managed for you, NEO gives you the digital platform to research, execute and monitor your investments in one place.</p>
<p style="margin-bottom: 0;">And because your banking relationship is already with Kotak, we can also look at integrating the overall banking and investment experience through Trinity.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">NEO — Key Features</h4>
{bullet_list([
    "<strong>📈 Equity:</strong> Buy/sell stocks, Market monitoring, Research and insights, Portfolio tracking",
    "<strong>📊 Trading:</strong> Intraday, Futures & Options, Advanced basket orders, MTF (with dedicated research section), Charts, Option-chain tools",
    "<strong>📈 Mutual Funds:</strong> Native MF investment journey, MF discovery, Digital execution, UPI Autopay support",
    "<strong>🏦 IPO:</strong> IPO applications, ASBA, UPI-based payment journey, Digital application process",
    "<strong>📱 Digital:</strong> Mobile investment platform, Personalised market/investment views, Integrated investment experience"
])}

{section_header('4', 'TRINITY vs NEO — VERY IMPORTANT FOR YOUR PITCH')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">Don't confuse these two with the customer.</p>
{comparison_table()}

<div style="background: #f1f5f9; padding: 16px; border-radius: 8px; text-align: left; margin-bottom: 24px;">
    <h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600;">The easiest explanation to a client:</h4>
    <p style="color: #1e40af; font-weight: 600; margin-bottom: 0; font-style: italic;">“Sir, Trinity is the relationship structure—your Bank + Demat + Trading together. NEO is the digital platform through which you can actually manage your investments and trades.”</p>
</div>

"""

update_inv_pitch('experience_solitaire_dashboard_new.html', inv_html)
update_inv_pitch('experience_privy_dashboard_new.html', inv_html)
update_inv_pitch('experience_privy_plus_dashboard_new.html', inv_html)
