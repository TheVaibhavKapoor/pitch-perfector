# -*- coding: utf-8 -*-
import re
import os

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = '''<div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Key Benefits</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <!-- 1. Daily Limits -->
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💰</span><h3>Daily Usage Limit</h3></div>
                                    <ul class="feat-list">
                                        <li>ATM withdrawals up to <strong>₹2.5 lakh</strong></li>
                                        <li>Purchase limit of <strong>₹15 lakh</strong></li>
                                    </ul>
                                </div>
                                <!-- 2. Offers & Benefits -->
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🍽️</span><h3>Offers &amp; Benefits</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>20% off</strong> when you dine with Zomato using Solitaire debit card</li>
                                        <li>Spend ₹2500 or more and save up to ₹1500 every month</li>
                                    </ul>
                                </div>
                                <!-- 3. Fuel & Forex -->
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">⛽</span><h3>Fuel &amp; Forex</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>2.5% Fuel surcharge waiver</strong> on fuel spends up to ₹30,000</li>
                                        <li><strong>1.5% Forex Markup</strong> on International Spends</li>
                                    </ul>
                                </div>
                                <!-- 4. Important Notes -->
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">⚠️</span><h3>Important Note</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>No complimentary lounge access</strong></li>
                                        <li><strong>No reward points</strong> on Solitaire Debit Card</li>
                                    </ul>
                                </div>
                                <!-- 5. Insurance Cover -->
                                <div class="feature-card full-width-card" style="grid-column: 1 / -1;">
                                    <div class="feat-card-header"><span class="feat-icon">🛡️</span><h3>Insurance Cover (Visa Infinite)</h3></div>
                                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 16px;">
                                        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
                                            <div style="color: #64748b; margin-bottom: 4px; font-size: 0.85rem;">Lost Card Liability</div>
                                            <div style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">₹ 6,00,000</div>
                                        </div>
                                        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
                                            <div style="color: #64748b; margin-bottom: 4px; font-size: 0.85rem;">Purchase Protection</div>
                                            <div style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">₹ 1,50,000</div>
                                        </div>
                                        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
                                            <div style="color: #64748b; margin-bottom: 4px; font-size: 0.85rem;">Lost Baggage</div>
                                            <div style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">₹ 1,00,000</div>
                                        </div>
                                        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
                                            <div style="color: #64748b; margin-bottom: 4px; font-size: 0.85rem;">Air Accident</div>
                                            <div style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">₹ 5,00,00,000</div>
                                        </div>
                                        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
                                            <div style="color: #64748b; margin-bottom: 4px; font-size: 0.85rem;">Personal Accident Base Cover*</div>
                                            <div style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">₹ 5,00,000</div>
                                        </div>
                                        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
                                            <div style="color: #64748b; margin-bottom: 4px; font-size: 0.85rem;">Personal Accident Enhance Cover**</div>
                                            <div style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">₹ 15,00,000</div>
                                        </div>
                                    </div>
                                    <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 16px;">
                                        * Minimum 2 POS/ECOM transactions of ₹500 each in last 30 days.<br>
                                        ** Minimum 6 POS/ECOM transactions of ₹500 each in last 60 days.
                                    </div>
                                </div>
                            </div>
                        </div>'''

# Replace from <div style="grid-column: 1 / -1;"> until the end of the <div style="background: #f9fafb..."> button div
content = re.sub(
    r'<div style=\"grid-column: 1 / -1;\">\s*<h3[^>]*>Key Benefits</h3>.*?<div style=\"background: #f9fafb; padding: 24px; border-radius: 12px; text-align: center; grid-column: 1 / -1;\">\s*<img src=\"solitaire_infinity_logo\.png\"[^>]*>\s*<a href=\"solitaire_dc\.html\"[^>]*>View Detailed Benefits</a>\s*</div>',
    new_grid,
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Remove solitaire_dc.html
dc_file = r'c:\Users\vaibh\Desktop\Pitch Perfector\solitaire_dc.html'
if os.path.exists(dc_file):
    os.remove(dc_file)
    print("Deleted solitaire_dc.html")

print('Updated experience_solitaire_dashboard.html')
