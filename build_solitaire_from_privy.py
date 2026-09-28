"""
Build experience_solitaire_dashboard_new.html based on the Privy template
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('experience_privy_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Simple text replacements
replacements = [
    ('Cloud Bank - Experience Privy', 'Cloud Bank - Experience Solitaire'),
    ('Kotak Privy Program Introduction', 'Kotak Solitaire Program Introduction'),
    ('current Privy proposition starts at approximately \u20b910 lakh Relationship Value or \u20b91\u20133 lakh monthly salary credit, depending on the eligibility route.',
     'Solitaire proposition is for customers with a Relationship Value of \u20b975 lakh or above, or a monthly salary credit of \u20b95 lakh+.'),
    ('Privy Debit Card</h2><p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Your gateway to everyday premium banking. The Privy Debit Card',
     'Solitaire Debit Card</h2><p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Your gateway to everyday premium banking. The Solitaire Debit Card'),
    ('Privy Credit Card</h2><p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Experience unparalleled luxury and rewards with our premium metallic Privy Credit Card, designed exclusively for our most esteemed clients.',
     'Solitaire Infinite Credit Card</h2><p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Experience unparalleled luxury with the exclusive Solitaire Infinite Credit Card, designed for Solitaire members only.'),
    ('Kotak Privy <span class="cap-note">(Accelerated RP capped at 1,00,000 per St. cycle)</span>',
     'Kotak Solitaire <span class="cap-note">(Accelerated Air Miles capped at 10,00,000 per St. cycle)</span>'),
    ('value="experience_privy_dashboard_v1.html" selected', 'value="experience_solitaire_dashboard_v1.html" selected'),
    ('value="experience_privy_dashboard_v2.html"', 'value="experience_solitaire_dashboard_v2.html"'),
    ('value="experience_privy_dashboard_v3.html"', 'value="experience_solitaire_dashboard_v3.html"'),
    ('href="privy.html"', 'href="solitaire.html"'),
    ('Privy debit card', 'Solitaire debit card'),
    ('Nil charges</strong> with Privy Program</li><li><strong>\u20b925,000 + GST</strong> in case RV is not met',
     'Nil charges</strong> with Solitaire Program</li><li><strong>\u20b950,000 + GST</strong> in case RV is not met'),
    ('Calculate Rewards Points', 'Calculate Air Miles & Benefits'),
    ('experience_privy_dashboard_new.html', 'experience_solitaire_dashboard_new.html'),
]

for old, new in replacements:
    count = html.count(old)
    if count > 0:
        html = html.replace(old, new)
        print(f'Replaced {count}x: {old[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

# Write the result
with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone! Written {len(html)} bytes to experience_solitaire_dashboard_new.html')
