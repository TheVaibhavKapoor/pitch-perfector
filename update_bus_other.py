# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

b_start = html.find('id="segment-business-content"')
other_start = html.find('id="panel-business-other"', b_start)
# The end of this panel is tricky, let's find the CALCULATE OVERALL BENEFIT button
other_end = html.find('<div style="text-align: center; margin-top: 48px;">', other_start)

new_other_content = '''id="panel-business-other" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 16px;">Exclusive Offerings & Banking</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Elevate your business operations with premium banking, payment solutions, and tax benefits.</p>
                    
                    <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">🏦</span><h3>Current Account</h3></div>
                            <ul class="feat-list">
                                <li><strong>NIL AQB requirement</strong> (also offered to all Family accounts CA, SA). Preferred account number.</li>
                                <li><strong style="color: #10b981;">Cheque pick-up and delivery at no extra charges</strong></li>
                                <li>Multi-city cash deposit up to 10X of prev. month's Avg. Credit Balance (up to <strong style="color: #10b981;">Rs. 20 cr. at zero charges</strong>)</li>
                                <li>Connected Banking: Tally Prime 6.0 benefits</li>
                                <li>Free debit card with zero withdrawal charges across all ATMs</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">💰</span><h3>Activ Money</h3></div>
                            <ul class="feat-list">
                                <li>Existing clients with Activ Money enabled will continue as per <strong style="color: #10b981;">existing threshold</strong></li>
                                <li>New clients will have a threshold of <strong>INR 45 lakhs</strong> if they activate Activ money in CA</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">🧾</span><h3>Kotax</h3></div>
                            <ul class="feat-list">
                                <li><strong>10% cash back</strong> up to ₹1500 p.m for tax paid via Kotax payment gateway with Solitaire Business DC</li>
                                <li>Cash back credited within 60 days of txn</li>
                                <li>Direct tax, indirect tax and GST payments supported</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">💻</span><h3>CMS (Fyn - CMS)</h3></div>
                            <ul class="feat-list">
                                <li><strong style="color: #10b981;">Available at no extra set up charges</strong></li>
                                <li><strong style="color: #10b981;">Free bulk NEFT/RTGS</strong> up to 500 monthly transactions p.m.</li>
                                <li>Seamless bulk payments and collections with secure maker checker facility</li>
                                <li>Mobile app convenience & smart tools to manage beneficiaries in real time</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="grid-column: span 1;">
                            <div class="feat-card-header"><span class="feat-icon">💳</span><h3>POS</h3></div>
                            <ul class="feat-list">
                                <li><strong style="color: #10b981;">Preferential MDR</strong> (Merchant Discount rate)</li>
                                <li><strong style="color: #10b981;">Nil rentals & Zero installation charges</strong> on new POS machines and sound boxes (No Cap on the number)</li>
                            </ul>
                        </div>
                    </div>
                </div>
                '''

html = html[:other_start] + new_other_content + html[other_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Business Other updated")
