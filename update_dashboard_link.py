# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = '''                        <div>
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 12px; font-size: 0.95rem;">Key Benefits</h3>
                            <ul class="benefit-list">
                                <li><strong>Daily Usage Limit:</strong> ATM withdrawals up to ₹2.5 lakh &amp; Purchase limit of ₹15 lakh.</li>
                                <li><strong>Offers &amp; Benefits:</strong> 20% off when you dine with Zomato using Solitaire debit card.</li>
                                <li><strong>Fuel &amp; Forex:</strong> 2.5% Fuel surcharge waiver &amp; 1.5% Forex Markup on International Spends.</li>
                                <li><strong>Insurance Cover:</strong> Comprehensive insurance including ₹5 Cr Air Accident &amp; ₹15 Lakh Personal Accident cover.</li>
                            </ul>
                        </div>
                        <div style="background: #f9fafb; padding: 24px; border-radius: 12px; text-align: center;">
                            <img src="solitaire_infinity_logo.png" alt="Solitaire" style="height: 60px; margin-bottom: 24px;">
                            <a href="solitaire_dc.html" style="display: block; padding: 12px 20px; background: #111827; color: white; text-decoration: none; border-radius: 8px; font-weight: 700; font-size: 0.95rem;">View Detailed Benefits</a>
                        </div>'''

content = re.sub(
    r'<div>\s*<h3[^>]*>Key Benefits</h3>\s*<ul class=\"benefit-list\">\s*<li><strong>Daily Usage.*?</ul>\s*</div>',
    new_content,
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated experience_solitaire_dashboard.html')
