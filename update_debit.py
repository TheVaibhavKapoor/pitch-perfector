# -*- coding: utf-8 -*-
import re

# Update debit_card_details.html
filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\debit_card_details.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Limits
content = content.replace('₹ 1,00,000', '₹ 2,50,000')
content = content.replace('₹ 3,00,000', '₹ 15,00,000')

# Create Benefits Section
benefits_html = '''
                <!-- Card Benefits & Insurance -->
                <section style="margin-bottom: 32px;">
                    <div class="card-section-title" style="margin-bottom: 16px;">
                        <div class="section-indicator"></div>
                        <h2>Solitaire Debit Card Benefits &amp; Insurance</h2>
                    </div>

                    <div style="background: #ffffff; border: 1px solid #e5e7eb; border-radius: 16px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
                        
                        <h3 style="font-size: 1rem; font-weight: 700; color: #111827; margin-bottom: 12px; border-bottom: 1px solid #f3f4f6; padding-bottom: 8px;">Key Features &amp; Offers</h3>
                        <ul style="list-style: none; padding: 0; margin: 0 0 24px 0;">
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;">
                                <span style="color: #0284c7;">✓</span>
                                <div>
                                    <strong style="color: #111827; display: block; font-size: 0.9rem;">Daily Usage Limit</strong>
                                    <span style="color: #4b5563; font-size: 0.85rem;">ATM withdrawals up to ₹2.5 lakh. Purchase limit of ₹15 lakh.</span>
                                </div>
                            </li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;">
                                <span style="color: #0284c7;">✓</span>
                                <div>
                                    <strong style="color: #111827; display: block; font-size: 0.9rem;">Offer and Benefits</strong>
                                    <span style="color: #4b5563; font-size: 0.85rem;">20% off when you dine with Zomato using Solitaire debit card - Spend ₹2500 or more and save up to ₹1500 every month.</span>
                                </div>
                            </li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;">
                                <span style="color: #0284c7;">✓</span>
                                <div>
                                    <strong style="color: #111827; display: block; font-size: 0.9rem;">Fuel Surcharge &amp; Forex</strong>
                                    <span style="color: #4b5563; font-size: 0.85rem;">2.5% Fuel surcharge waiver on fuel spends up to ₹30,000 per month. 1.5% Forex Markup on all International Spends.</span>
                                </div>
                            </li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;">
                                <span style="color: #d61f26;">!</span>
                                <div>
                                    <span style="color: #6b7280; font-size: 0.85rem;"><strong>Note:</strong> No complimentary lounge access and no reward points on Solitaire Debit Card.</span>
                                </div>
                            </li>
                        </ul>

                        <h3 style="font-size: 1rem; font-weight: 700; color: #111827; margin-bottom: 12px; border-bottom: 1px solid #f3f4f6; padding-bottom: 8px;">Insurance Cover (Visa Infinite)</h3>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 0.85rem;">
                            <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                                <div style="color: #64748b; margin-bottom: 4px;">Lost Card Liability</div>
                                <div style="font-weight: 700; color: #0f172a;">₹ 6,00,000</div>
                            </div>
                            <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                                <div style="color: #64748b; margin-bottom: 4px;">Purchase Protection (Fire/Burglary)</div>
                                <div style="font-weight: 700; color: #0f172a;">₹ 1,50,000</div>
                            </div>
                            <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                                <div style="color: #64748b; margin-bottom: 4px;">Lost Baggage</div>
                                <div style="font-weight: 700; color: #0f172a;">₹ 1,00,000</div>
                            </div>
                            <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                                <div style="color: #64748b; margin-bottom: 4px;">Air Accident</div>
                                <div style="font-weight: 700; color: #0f172a;">₹ 5,00,00,000</div>
                            </div>
                            <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                                <div style="color: #64748b; margin-bottom: 4px;">Personal Accident Base Cover*</div>
                                <div style="font-weight: 700; color: #0f172a;">₹ 5,00,000</div>
                            </div>
                            <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                                <div style="color: #64748b; margin-bottom: 4px;">Personal Accident Enhance Cover**</div>
                                <div style="font-weight: 700; color: #0f172a;">₹ 15,00,000</div>
                            </div>
                        </div>
                        <div style="font-size: 0.7rem; color: #94a3b8; margin-top: 16px;">
                            * Minimum 2 POS/ECOM transactions of ₹500 each in last 30 days.<br>
                            ** Minimum 6 POS/ECOM transactions of ₹500 each in last 60 days.
                        </div>
                    </div>
                </section>
'''

if 'Solitaire Debit Card Benefits' not in content:
    content = content.replace('<!-- Recent Debit Card Transactions -->', benefits_html + '\n                <!-- Recent Debit Card Transactions -->')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated debit_card_details.html')

# Update experience_solitaire_dashboard.html
dashboard_filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(dashboard_filepath, 'r', encoding='utf-8') as f:
    dash_content = f.read()

new_benefits = '''<ul class="benefit-list">
                                <li><strong>Daily Usage Limit:</strong> ATM withdrawals up to ₹2.5 lakh &amp; Purchase limit of ₹15 lakh.</li>
                                <li><strong>Offers &amp; Benefits:</strong> 20% off when you dine with Zomato using Solitaire debit card.</li>
                                <li><strong>Fuel &amp; Forex:</strong> 2.5% Fuel surcharge waiver &amp; 1.5% Forex Markup on International Spends.</li>
                                <li><strong>Insurance Cover:</strong> Comprehensive insurance including ₹5 Cr Air Accident &amp; ₹15 Lakh Personal Accident cover.</li>
                            </ul>'''
                            
dash_content = re.sub(
    r'<ul class=\"benefit-list\">\s*<li>Enhanced daily ATM withdrawal.*?</ul\s*>', 
    new_benefits, 
    dash_content,
    flags=re.DOTALL
)

with open(dashboard_filepath, 'w', encoding='utf-8') as f:
    f.write(dash_content)
print('Updated experience_solitaire_dashboard.html')
