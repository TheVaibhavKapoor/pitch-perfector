# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacement HTMLs

dc_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💰</span><h3>Daily Usage Limit</h3></div>
                                    <ul class="feat-list">
                                        <li>ATM withdrawals up to <strong>₹2.5 lakh</strong></li>
                                        <li>Purchase limit of <strong>₹15 lakh</strong></li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🍽️</span><h3>Offers &amp; Benefits</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>20% off</strong> when you dine with Zomato using Solitaire debit card</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">⛽</span><h3>Fuel &amp; Forex</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>2.5% Fuel surcharge waiver</strong> on fuel spends up to ₹30,000</li>
                                        <li><strong>1.5% Forex Markup</strong> on International Spends</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🛡️</span><h3>Insurance Cover</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>₹5 Cr</strong> Air Accident cover</li>
                                        <li><strong>₹15 Lakh</strong> Personal Accident cover</li>
                                    </ul>
                                </div>
                            </div>
                        </div>'''

cc_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">✈️</span><h3>Lounge Access</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Unlimited</strong> domestic &amp; international airport lounge access</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🚀</span><h3>Reward Points</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>5X Reward Points</strong> on travel and luxury dining expenditures</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🌐</span><h3>Forex</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Zero foreign currency markup fees</strong> on international transactions</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">⛳</span><h3>Lifestyle</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Complimentary golf rounds</strong> and exclusive lifestyle concierge</li>
                                    </ul>
                                </div>
                            </div>
                        </div>'''

assets_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📉</span><h3>Interest Rates</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Preferential interest rates</strong> on Home Loans and Loan Against Property</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💳</span><h3>Fees</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Zero processing fees</strong> for asset-backed credit facilities</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">👨‍💼</span><h3>Relationship Manager</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Dedicated relationship manager</strong> for personalized loan structuring</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">⚡</span><h3>Approvals</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Express approvals</strong> and seamless digital documentation</li>
                                    </ul>
                                </div>
                            </div>
                        </div>'''

investments_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🤵</span><h3>Wealth Advisor</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Dedicated wealth advisor</strong> for portfolio structuring</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💎</span><h3>Exclusive Access</h3></div>
                                    <ul class="feat-list">
                                        <li>Access to <strong>exclusive Alternative Investment Funds (AIFs)</strong> and PMS</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📈</span><h3>Brokerage</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Zero brokerage</strong> on equity delivery trades</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📊</span><h3>Analytics</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Comprehensive digital wealth dashboard</strong> and analytics</li>
                                    </ul>
                                </div>
                            </div>
                        </div>'''

forex_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💱</span><h3>Forex Rates</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Preferential Forex markup</strong> and conversion rates</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💸</span><h3>Remittances</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Free international</strong> inward and outward remittances</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🌍</span><h3>Multi-Currency</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Multi-currency accounts</strong> for seamless global transactions</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📞</span><h3>Dealing Desk</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Dedicated Forex dealing desk</strong> for real-time rates</li>
                                    </ul>
                                </div>
                            </div>
                        </div>'''

other_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🛎️</span><h3>Concierge</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>24x7 premium lifestyle</strong> and travel concierge desk</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">⭐</span><h3>Priority Service</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Priority processing</strong> across all bank service touchpoints</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🎟️</span><h3>Events</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Invitations</strong> to exclusive networking and lifestyle events</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🔐</span><h3>Lockers</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Complimentary</strong> safety deposit lockers</li>
                                    </ul>
                                </div>
                            </div>
                        </div>'''

# We also need to change the grid-template-columns of the parent div if they contain a button (DC and CC). 
# Actually, the grid-template-columns: 1fr 1fr; is set on the container that wraps the "Key Benefits" and the "View Benefits Button".
# It makes more sense to have the grid be full width and then have the button below it, or keep it inside.
# If we set grid-column: 1 / -1 on the new blocks, it will take the full width of the parent grid.

# DC Replace
content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li><strong>Daily Usage.*?</ul>\s*</div>',
    dc_grid,
    content,
    flags=re.DOTALL
)

# CC Replace
content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li>Unlimited domestic.*?</ul>\s*</div>',
    cc_grid,
    content,
    flags=re.DOTALL
)

# Assets Replace
content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li>Preferential interest.*?</ul>\s*</div>',
    assets_grid,
    content,
    flags=re.DOTALL
)

# Investments Replace
content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li>Dedicated wealth advisor.*?</ul>\s*</div>',
    investments_grid,
    content,
    flags=re.DOTALL
)

# Forex Replace
content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li>Preferential Forex.*?</ul>\s*</div>',
    forex_grid,
    content,
    flags=re.DOTALL
)

# Other Replace
content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li>24x7 premium lifestyle.*?</ul>\s*</div>',
    other_grid,
    content,
    flags=re.DOTALL
)

# Update buttons to span full width
content = content.replace('<div style="background: #f9fafb; padding: 24px; border-radius: 12px; text-align: center;">', '<div style="background: #f9fafb; padding: 24px; border-radius: 12px; text-align: center; grid-column: 1 / -1;">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated experience_solitaire_dashboard.html')
