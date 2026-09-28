# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\solitaire_dc.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update basic text
content = content.replace('<title>Solitaire Credit Card - Cloud Bank</title>', '<title>Solitaire Debit Card - Cloud Bank</title>')
content = content.replace('<h2>Kotak Solitaire Credit Card</h2>', '<h2>Kotak Solitaire Debit Card</h2>')
content = content.replace('alt="Kotak Solitaire Credit Card"', 'alt="Kotak Solitaire Debit Card"')
content = content.replace('<span class="badge-pill">Premium Metal Card</span>', '<span class="badge-pill">Visa Infinite Debit Card</span>')
content = content.replace('<span class="badge-pill">Nil Joining Fee with Solitaire Program</span>', '<span class="badge-pill">Zero Issuance &amp; Annual Charges</span>')
content = content.replace('<span class="badge-pill">0% Forex Charge</span>', '<span class="badge-pill">1.5% Forex Markup</span>')

# Update breadcrumb
content = content.replace('<span>‹</span> Solitaire Credit Card', '<span>‹</span> Solitaire Debit Card')

# Define new grid
new_grid = '''<div class="product-features-grid">
    <!-- 1. Daily Limits -->
    <div class="feature-card">
        <div class="feat-card-header">
            <span class="feat-icon">💰</span>
            <h3>Daily Usage Limit</h3>
        </div>
        <ul class="feat-list">
            <li><strong>₹2.5 Lakh</strong> ATM withdrawals</li>
            <li><strong>₹15 Lakh</strong> Purchase limit</li>
        </ul>
    </div>

    <!-- 2. Offers & Benefits -->
    <div class="feature-card">
        <div class="feat-card-header">
            <span class="feat-icon">🍽️</span>
            <h3>Offer and Benefits</h3>
        </div>
        <ul class="feat-list">
            <li><strong>20% off</strong> when you dine with Zomato</li>
            <li>Spend ₹2500 or more and save up to ₹1500 every month</li>
        </ul>
    </div>

    <!-- 3. Fuel & Forex -->
    <div class="feature-card">
        <div class="feat-card-header">
            <span class="feat-icon">⛽</span>
            <h3>Fuel Surcharge &amp; Forex</h3>
        </div>
        <ul class="feat-list">
            <li><strong>2.5% Fuel surcharge waiver</strong> on fuel spends up to ₹30,000 per month</li>
            <li><strong>1.5% Forex Markup</strong> on all International Spends</li>
        </ul>
    </div>

    <!-- 4. Important Notes -->
    <div class="feature-card">
        <div class="feat-card-header">
            <span class="feat-icon">⚠️</span>
            <h3>Important Note</h3>
        </div>
        <ul class="feat-list">
            <li><strong>No complimentary lounge access</strong></li>
            <li><strong>No reward points</strong> on Solitaire Debit Card</li>
        </ul>
    </div>

    <!-- 5. Insurance Cover (Span 2 Cols) -->
    <div class="feature-card full-width-card">
        <div class="feat-card-header">
            <span class="feat-icon">🛡️</span>
            <h3>Insurance Cover (Visa Infinite)</h3>
        </div>
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
</div>'''

# Replace the old grid
content = re.sub(
    r'<div class="product-features-grid">.*?</script>', 
    new_grid + '\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </main>\n    </div>\n    <script src="app.js"></script>', 
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated solitaire_dc.html')
