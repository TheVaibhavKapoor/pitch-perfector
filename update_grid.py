import re

with open("experience_solitaire_dashboard.html", "r", encoding="utf-8") as f:
    html = f.read()

new_panels = """
<div class="info-panel active" id="panel-intro">
    <h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 8px;">Introduction to RM and Program</h2>
    
    <h3 style="font-weight: 700; color: #0f172a; margin-bottom: 16px; font-size: 1.05rem;">Program Pitch &amp; Benefits</h3>
    <ul style="color: #475569; line-height: 1.8; margin-left: 20px; font-size: 0.95rem;">
        <li><strong>Intro of RM:</strong> Dedicated Relationship Manager assigned for personalized advisory and service.</li>
        <li><strong>Program Pitch:</strong> Crafted exclusively for the select few, providing priority access and tailored solutions.</li>
        <li><strong>Product-wise Benefits:</strong> Specialized rates and dedicated processing for loans, investments, and cards.</li>
    </ul>
</div>

<div class="info-panel" id="panel-lifestyle">
    <h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 8px;">Lifestyle Benefits</h2>
    <p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">Elevate your everyday experiences with unmatched lifestyle privileges.</p>
    <ul style="color: #475569; line-height: 1.8; margin-left: 20px; font-size: 0.95rem;">
        <li>24/7 Global Concierge services for dining and travel.</li>
        <li>Complimentary airport lounge access worldwide.</li>
        <li>Curated experiences and invites to premium events.</li>
    </ul>
</div>

<div class="info-panel" id="panel-summary">
    <h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 8px;">Summary</h2>
    <p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">A holistic view of your premium banking benefits.</p>
    <ul style="color: #475569; line-height: 1.8; margin-left: 20px; font-size: 0.95rem;">
        <li>Comprehensive suite of cards, loans, and investment solutions.</li>
        <li>Dedicated support and priority processing across all touchpoints.</li>
        <li>Unrivaled lifestyle privileges tailored for you.</li>
    </ul>
</div>
"""

html = html.replace('<div class="info-panel active" id="panel-cc">', new_panels + '\n<div class="info-panel" id="panel-cc">')

with open("experience_solitaire_dashboard.html", "w", encoding="utf-8") as f:
    f.write(html)
