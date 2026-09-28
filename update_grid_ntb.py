import re

with open("experience_solitaire_dashboard_new.html", "r", encoding="utf-8") as f:
    html = f.read()

new_grid = """<div class="product-grid">
<div class="product-card active" onclick="showPanel('intro', this)">
<div class="product-content">
<span class="product-subtitle">Overview</span>
<h3 class="product-title">Introduction to RM and Program</h3>
<span class="product-timestamp">Program pitch and benefits</span>
</div>
<div class="product-icon">👋</div>
</div>
<div class="product-card" onclick="showPanel('lifestyle', this)">
<div class="product-content">
<span class="product-subtitle">Exclusive Experiences</span>
<h3 class="product-title">Lifestyle benefits</h3>
<span class="product-timestamp">Travel, dining, &amp; concierge</span>
</div>
<div class="product-icon">✈️</div>
</div>
<div class="product-card" onclick="showPanel('cc', this)">
<div class="product-content">
<span class="product-subtitle">Premium Access</span>
<h3 class="product-title">Credit Card</h3>
<span class="product-timestamp">Premium lifestyle &amp; travel benefits</span>
</div>
<div class="product-icon">💎</div>
</div>
<div class="product-card" onclick="showPanel('assets', this)">
<div class="product-content">
<span class="product-subtitle">Asset-Backed Lending</span>
<h3 class="product-title">Loans</h3>
<span class="product-timestamp">Bespoke borrowing &amp; credit solutions</span>
</div>
<div class="product-icon">🏦</div>
</div>
<div class="product-card" onclick="showPanel('investments', this)">
<div class="product-content">
<span class="product-subtitle">Portfolio Growth</span>
<h3 class="product-title">Investment</h3>
<span class="product-timestamp">Track your mutual funds &amp; stocks</span>
</div>
<div class="product-icon">📈</div>
</div>
<div class="product-card" onclick="showPanel('summary', this)">
<div class="product-content">
<span class="product-subtitle">Overview</span>
<h3 class="product-title">Summary</h3>
<span class="product-timestamp">Overall program recap</span>
</div>
<div class="product-icon">📋</div>
</div>
</div>"""

# Replace the grid in Individual tab
grid_pattern = re.compile(r'<div class="product-grid">.*?</div>\s*<!-- Info Panels -->', re.DOTALL)
html = grid_pattern.sub(new_grid + '\n<!-- Info Panels -->', html)

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

# Insert new panels before panel-cc. Make sure to match the exact string for panel-cc
html = html.replace('<div class="info-panel active" id="panel-cc">', new_panels + '\n<div class="info-panel" id="panel-cc">')
html = html.replace('<div class="info-panel" id="panel-cc">', new_panels + '\n<div class="info-panel" id="panel-cc">')
html = html.replace(new_panels + '\n' + new_panels, new_panels)

# Hide panel-dc if it exists
html = html.replace('<div class="info-panel" id="panel-dc">', '<div class="info-panel" id="panel-dc" style="display: none;">')
html = html.replace('<div class="info-panel active" id="panel-dc">', '<div class="info-panel" id="panel-dc" style="display: none;">')

with open("experience_solitaire_dashboard_new.html", "w", encoding="utf-8") as f:
    f.write(html)
