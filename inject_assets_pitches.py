import os
from bs4 import BeautifulSoup

def update_assets_pitch(filename, new_content):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    panel_assets = soup.find(id='panel-assets')
    if panel_assets:
        pitch_tab = panel_assets.find(class_='inner-tab-content-pitches')
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

def cheat_sheet_table():
    rows = [
        ("Buying property", "HL", "“Planning a property purchase?”"),
        ("Existing HL elsewhere", "HL BT + Top-up", "“What rate are you currently paying?”"),
        ("Owns debt-free property", "LAP", "“Do you have any debt-free property?”"),
        ("Irregular liquidity", "OD", "“Do you need the entire amount or only periodically?”"),
        ("Business owner", "WC", "“How long is your receivable cycle?”"),
        ("Business expansion", "Business Loan / WC", "“How are you funding the expansion?”"),
        ("POS-heavy business", "Receivables Loan", "“What % of turnover is through cards?”"),
        ("Buying car", "Auto Loan", "“Planning an upgrade?”"),
        ("Existing business loan", "Takeover + enhancement", "“What is your current rate/outstanding?”"),
        ("Large investment opportunity", "LAP / OD", "“Would you prefer to liquidate investments or leverage an asset?”")
    ]
    html = '<table style="width: 100%; text-align: left; border-collapse: collapse; margin-bottom: 24px; font-size: 0.9rem;">'
    html += '<thead style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;"><tr>'
    html += '<th style="padding: 12px; font-weight: 600; color: #475569;">Customer Situation</th>'
    html += '<th style="padding: 12px; font-weight: 600; color: #475569;">First Product to Explore</th>'
    html += '<th style="padding: 12px; font-weight: 600; color: #475569;">RM Question</th>'
    html += '</tr></thead><tbody>'
    for i, (sit, prod, q) in enumerate(rows):
        bg = "#ffffff" if i % 2 == 0 else "#f8fafc"
        html += f'<tr style="background: {bg}; border-bottom: 1px solid #e2e8f0;">'
        html += f'<td style="padding: 12px; font-weight: 500; color: #0f172a;">{sit}</td>'
        html += f'<td style="padding: 12px; color: #3b82f6; font-weight: 500;">{prod}</td>'
        html += f'<td style="padding: 12px; font-style: italic; color: #475569;">{q}</td>'
        html += '</tr>'
    html += '</tbody></table>'
    return html

assets_html = f"""
{section_header('🔥', 'THE "ASSET REVIEW" PITCH (Recommended Approach)')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">This is the strongest approach to use with Premium (Solitaire / Privy / Privy+) clients. Do not individually pitch 7 loans.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, as your Relationship Manager, one exercise I'd like to do once every year is a quick liability and asset review.</p>
<p style="margin-bottom: 12px;">I'll understand what assets you own, what loans you currently have, what rates you're paying and where your future funding requirements may come up.</p>
<p style="margin-bottom: 12px;">For example, if you have a home loan elsewhere, we can evaluate a balance transfer. If you have a debt-free property, we can assess the liquidity available against it. If you run a business, we can look at working-capital requirements or an OD instead of you liquidating investments whenever there is a cash-flow gap.</p>
<p style="margin-bottom: 12px;">The idea is not to increase your borrowing. It's to make sure that whenever you need financing, you're using the most appropriate source of capital.</p>
<p style="margin-bottom: 0;">I'll do the evaluation and only recommend something if I genuinely see a benefit for you.”</p>
''')}

<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Your RM Lending Cheat Sheet</h4>
{cheat_sheet_table()}

<div style="background: #f1f5f9; padding: 16px; border-radius: 8px; text-align: left; margin-bottom: 32px;">
    <h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600;">The Key RM Mindset</h4>
    <p style="color: #475569; margin-bottom: 8px;"><strong>Don't ask:</strong> <em>“Sir, do you need a loan?”</em></p>
    <p style="color: #475569; margin-bottom: 12px;"><strong>Ask:</strong> <em>“What major financial requirement do you see coming up over the next 6–12 months?”</em></p>
    <p style="color: #0f172a; font-weight: 600; margin-bottom: 8px;">Then diagnose:</p>
    <p style="color: #3b82f6; font-weight: 600;">Requirement → Cash-flow → Existing liability → Available collateral → Appropriate structure → Kotak solution.</p>
    <p style="color: #475569; font-size: 0.85rem; margin-top: 8px;">That is the difference between selling an asset product and doing a relationship-led lending conversation.</p>
</div>

<hr style="border: 0; border-top: 2px dashed #cbd5e1; margin: 32px 0;">

{section_header('1', 'HOME LOAN — HL')}
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, whenever you are planning a property purchase, I would request you to involve me before finalising the financing.</p>
<p style="margin-bottom: 12px;">At Kotak, we can look at the complete requirement—property value, funding requirement, EMI comfort, tenure and your existing liabilities—and structure the home loan accordingly.</p>
<p style="margin-bottom: 12px;">We can also look at pre-approved funding, balance transfer and top-up options, so you don't necessarily have to wait until the property transaction is finalised to understand your borrowing capacity.</p>
<p style="margin-bottom: 0;">My role would be to make the financing part as seamless as possible and help you structure it in the most efficient way.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Key Features / Benefits</h4>
{bullet_list([
    "Loan amount up to ₹40 crore, subject to eligibility",
    "Funding of up to 90% of property value, subject to applicable norms",
    "Tenure up to 25 years",
    "Competitive rates currently advertised from 7.60% p.a.",
    "Minimal documentation & Digital-first application",
    "Doorstep service",
    "Pre-approved home-loan options for eligible existing customers",
    "Balance transfer & Top-up facility",
    "Home purchase, construction, extension/renovation options",
    "Fixed/floating options for applicable customer segments",
    "Flexible prepayment/foreclosure options, subject to applicable terms"
])}
{question_box("RM Trigger Questions", '''
<p style="margin-bottom: 8px;">“Do you have any property purchase planned in the next 6–12 months?”</p>
<p style="margin-bottom: 0;">“Do you currently have a home loan with another bank?”</p>
<p style="font-size: 0.85rem; color: #475569; font-weight: 400; font-style: italic; margin-top: 8px;">(The second question is particularly important because it opens the door for a Balance Transfer + Top-up conversation.)</p>
''')}

{section_header('2', 'LOAN AGAINST PROPERTY — LAP')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">This is one of the strongest products for HNI / business-owner customers.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, one area I would also like to explore with you is whether any of your existing properties are currently under-utilised from a financial perspective.</p>
<p style="margin-bottom: 12px;">If you own residential, commercial or industrial property, we can potentially unlock part of that property's value without selling the asset.</p>
<p style="margin-bottom: 12px;">Through a Loan Against Property, the funds can be used for business expansion, investment in the business, machinery, debt consolidation or other eligible personal requirements.</p>
<p style="margin-bottom: 12px;">And importantly, we can structure it either as a regular term loan or an overdraft, depending on whether you need the entire amount upfront or want flexibility to draw funds as required.</p>
<p style="margin-bottom: 0;">So if you have a substantial property asset but don't want to liquidate it, this is something I would definitely evaluate for you.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Key Features / Benefits</h4>
{bullet_list([
    "Secured funding against property (Residential, commercial and industrial property)",
    "Loan range advertised from ₹10 lakh to ₹5 crore on the standard LAP proposition",
    "Can be used for eligible personal and business requirements (Business expansion, Machinery purchase, Debt consolidation)",
    "Flexible funding structures: Term Loan or OD facility",
    "Potentially lower-cost financing compared with unsecured borrowing because the facility is secured",
    "Existing Kotak customers can approach their RM for the facility",
    "Kotak states a typical disbursal timeline of up to 25 working days from receipt of documents, subject to conditions and credit approval"
])}
{question_box("Powerful RM Question", '''
<p style="margin-bottom: 12px;">“Sir, do you own any commercial or residential property which is currently debt-free?”</p>
<p style="margin-bottom: 8px; color: #475569; font-weight: 400;">If YES:</p>
<p style="margin-bottom: 0;">“Then I would like to evaluate the available borrowing potential against that property—not necessarily because you need funds today, but so you know what liquidity is available to you if an opportunity comes up.”</p>
<p style="font-size: 0.85rem; color: #475569; font-weight: 400; font-style: italic; margin-top: 8px;">(That's a much better HNI conversation than “Sir, do you need a loan?”)</p>
''')}

{section_header('3', 'OD — OVERDRAFT')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">This needs to be pitched differently from a normal loan.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, if your requirement is not a fixed ₹X crore today, but rather access to liquidity whenever required, I would actually suggest that we evaluate an overdraft structure instead of taking the entire loan upfront.</p>
<p style="margin-bottom: 12px;">The key advantage is flexibility—you have a sanctioned limit available, you draw what you actually need, and repayment can be made as your cash flow comes in.</p>
<p style="margin-bottom: 12px;">This can be particularly useful for business owners or customers with irregular cash flows, seasonal requirements or temporary liquidity gaps.</p>
<p style="margin-bottom: 0;">So instead of borrowing ₹1 crore and paying interest on the entire amount from day one, we can evaluate whether an OD structure is more appropriate for your actual cash-flow pattern.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Key Benefits</h4>
{bullet_list([
    "Sanctioned credit limit available when required",
    "Draw only as required, subject to facility terms",
    "Useful for short-term liquidity gaps",
    "Flexible withdrawal and repayment",
    "Particularly relevant for variable/seasonal cash flows",
    "Can be structured against property for eligible customers",
    "Kotak also offers Digi OD for eligible business customers, with unsecured limits advertised up to ₹15 lakh and paperless processing",
    "LAP can also be structured as an OD facility"
])}
{question_box("Key Question", '''
<p style="margin-bottom: 8px;">“Does your cash requirement come in one large requirement, or do you typically need ₹10–20 lakh here, ₹30 lakh there depending on the month?”</p>
<p style="margin-bottom: 0; color: #475569; font-weight: 400; font-style: italic;">If variable → OD conversation.</p>
''')}

{section_header('4', 'WORKING CAPITAL — WC')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">For business owners, this is a major cross-sell opportunity.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, when you are running a business, profitability and liquidity are two different things.</p>
<p style="margin-bottom: 12px;">You may have healthy sales and profitability, but money can still get stuck in inventory, receivables or payment cycles.</p>
<p style="margin-bottom: 12px;">That's where I would like to understand your working-capital cycle.</p>
<p style="margin-bottom: 12px;">Kotak can look at solutions such as Cash Credit, Overdraft, Working Capital Term Loans, Supply Chain Finance and other structured solutions, depending on the nature of your business.</p>
<p style="margin-bottom: 0;">The objective is not simply to give you a loan—it is to make sure your business has adequate liquidity to purchase inventory, pay vendors and manage receivables without disturbing your personal investments or long-term assets.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Key Features / Benefits</h4>
{bullet_list([
    "Cash Credit & Overdraft",
    "Demand/Short-Term Loans",
    "Working Capital Term Loan",
    "Supply Chain Finance",
    "Customised financing with dedicated RM support",
    "Flexible margin requirements based on business",
    "Facilities designed for incremental working-capital requirements",
    "Exporter/importer solutions including pre- and post-shipment finance",
    "Competitive pricing and processing/turnaround subject to credit assessment"
])}
<div style="background: #fdf4ff; border-left: 4px solid #c026d3; padding: 16px; margin-bottom: 24px; text-align: left;">
    <h5 style="color: #86198f; margin-bottom: 8px; font-size: 1rem; font-weight: 600;">Special Opportunity — GST-Based Funding</h5>
    <p style="color: #701a75; font-size: 0.95rem; margin-bottom: 8px;">For eligible businesses:</p>
    <ul style="padding-left: 20px; color: #701a75; font-size: 0.9rem; margin-bottom: 0; line-height: 1.5;">
        <li>Assessment using GST returns + bank statements</li>
        <li>OD / Bank Guarantee / Term Loan options</li>
        <li>Business funding advertised up to ₹2 crore</li>
        <li>Quick processing & Easier documentation</li>
    </ul>
</div>
{question_box("Powerful RM Questions", '''
<p style="margin-bottom: 8px;">“What is your average receivable period?”</p>
<p style="margin-bottom: 8px;">“How many days of inventory do you normally carry?”</p>
<p style="margin-bottom: 8px;">“Do your customers pay you in 30, 60 or 90 days?”</p>
<p style="margin-bottom: 0;">“Do you currently use CC/OD limits with another bank?”</p>
<p style="font-size: 0.85rem; color: #475569; font-weight: 400; font-style: italic; margin-top: 8px;">(These questions make you sound like a business banker, rather than someone selling a loan.)</p>
''')}

{section_header('5', 'AUTO / CAR LOAN')}
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, if you are planning a new vehicle or even replacing an existing vehicle, please let me know before you finalise the financing at the dealership.</p>
<p style="margin-bottom: 12px;">We can evaluate the financing separately and structure the loan based on your preferred down payment, tenure and cash-flow requirement.</p>
<p style="margin-bottom: 12px;">Kotak's auto-financing proposition covers a wide range of vehicles, including new and used cars, with flexible financing structures.</p>
<p style="margin-bottom: 0;">So rather than deciding the EMI first and then choosing the financing, I can help you work backwards from the amount you actually want to deploy.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Key Features</h4>
{bullet_list([
    "New and used car financing (Wide range of passenger cars/MUVs)",
    "Financing available for eligible imported cars",
    "Financing up to 100% of car value, subject to eligibility",
    "Loan amount from ₹1 lakh",
    "Tenure 12–84 months",
    "Tailor-made financing schemes with attractive/profile-based pricing",
    "Speedy processing (Kotak Mahindra Prime states processing can be completed within 48 hours after satisfactory documentation)",
    "Prepayment possible after 6 months, subject to applicable charges/terms"
])}
{question_box("RM Question", '''
<p style="margin-bottom: 0;">“Sir, are you planning to upgrade or purchase a vehicle in the next 6–12 months?”</p>
''')}

{section_header('6', 'BUSINESS LOAN')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">For a business owner who doesn't want to mortgage property, this is an important conversation.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir/Ma’am, if the requirement is for business expansion but you don't want to create a mortgage on your property, we can also evaluate an unsecured business-financing route.</p>
<p style="margin-bottom: 12px;">Depending on your business profile, turnover, banking and financials, we can look at an appropriate business-loan structure.</p>
<p style="margin-bottom: 0;">This could be useful for expansion, additional inventory, equipment, a new location or managing a temporary cash-flow requirement.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Benefits</h4>
{bullet_list([
    "Unsecured business financing may be available",
    "For business expansion, inventory funding, equipment, working-capital support",
    "OD / term-loan structures",
    "GST-based assessment for eligible programmes",
    "Bank-statement-based assessment for eligible programmes",
    "Kotak's bank-statement-based working-capital proposition advertises OD, Bank Guarantee and term-loan options, with loans up to ₹2 crore for eligible micro-enterprises"
])}

{section_header('7', 'CREDIT-CARD RECEIVABLES → BUSINESS FUNDING')}
<p style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 16px;">This is a very good hidden pitch for merchants.</p>
{pitch_box("Customer Pitch", '''
<p style="margin-bottom: 12px;">“Sir, if your business receives significant payments through card/POS transactions, we can also look at whether those receivables can support your funding requirement.</p>
<p style="margin-bottom: 12px;">Instead of pledging another asset, the business's transaction history can potentially be used to assess funding eligibility.</p>
<p style="margin-bottom: 0;">This can be structured as a business loan or overdraft depending on your requirement.”</p>
''')}
<h4 style="color: #0f172a; margin-bottom: 12px; font-size: 1.05rem; font-weight: 600; text-align: left;">Features</h4>
{bullet_list([
    "Funding against eligible credit-card/POS receivables",
    "Business Loan or OD",
    "Advertised funding up to ₹3 crore",
    "Can potentially be combined with loan + OD",
    "No asset collateral for this specific facility, subject to eligibility and credit assessment"
])}
{question_box("Killer Question", '''
<p style="margin-bottom: 0;">“Sir, approximately how much of your monthly business turnover comes through card/POS transactions?”</p>
''')}

{section_header('8', 'LOAN / LIABILITY TAKEOVER')}
<div style="text-align: left; color: #475569; font-size: 0.95rem; margin-bottom: 24px;">
    <p style="margin-bottom: 12px;">Don't only ask: <em>“Do you need a loan?”</em></p>
    <p style="margin-bottom: 12px;">Ask: <strong>“Sir, do you currently have any major loans with another bank?”</strong></p>
    <p style="margin-bottom: 12px;">If yes: <strong>“What rate are you currently paying and approximately how much is the outstanding?”</strong></p>
    
    <h5 style="color: #0f172a; font-weight: 600; margin-top: 16px; margin-bottom: 8px;">Evaluate Possible Kotak Opportunities:</h5>
    <ul style="padding-left: 20px; line-height: 1.6; margin-bottom: 16px;">
        <li><strong>Home Loan</strong> → Balance Transfer + Top-up</li>
        <li><strong>LAP</strong> → Takeover + enhancement</li>
        <li><strong>Business Loan</strong> → Takeover</li>
        <li><strong>Working Capital</strong> → Takeover / enhancement</li>
        <li><strong>Auto Loan</strong> → refinance/eligible restructuring</li>
    </ul>
    
    <p style="margin-bottom: 12px;">The conversation becomes:</p>
    <div style="background: #eef2ff; padding: 16px; border-radius: 8px; color: #1e40af; font-weight: 600; border-left: 4px solid #3b82f6;">
        “Let's see whether we can reduce your financing cost or increase your available liquidity.”
    </div>
    <p style="margin-top: 12px; font-style: italic;">That's much stronger.</p>
</div>
"""

update_assets_pitch('experience_solitaire_dashboard_new.html', assets_html)
update_assets_pitch('experience_privy_dashboard_new.html', assets_html)
update_assets_pitch('experience_privy_plus_dashboard_new.html', assets_html)
