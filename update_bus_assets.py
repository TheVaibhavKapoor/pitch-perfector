# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the panel-business-assets inside the business wrapper
b_start = html.find('id="segment-business-content"')
assets_start = html.find('id="panel-business-assets"', b_start)
assets_end = html.find('id="panel-business-investments"', assets_start)

new_assets_content = '''id="panel-business-assets" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 16px;">Lending Solutions to Business</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Comprehensive credit and lending solutions designed for Solitaire Business clients.</p>
                    
                    <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">🏢</span><h3>Working Capital</h3></div>
                            <ul class="feat-list">
                                <li>Up to <strong style="color: #10b981;">120%</strong> Working Capital against Property collateral</li>
                                <li>Up to <strong style="color: #10b981;">20% Ad-hoc</strong> Working Capital limit (upto 120 Days p.a., max 2 Cr)</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">💳</span><h3>Business Credit Limit</h3></div>
                            <ul class="feat-list">
                                <li><strong>Free Business Credit Card</strong></li>
                                <li>Limit up to <strong style="color: #10b981;">30 Lacs</strong></li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">🏦</span><h3>LAP & LRD</h3></div>
                            <ul class="feat-list">
                                <li><strong>LAP:</strong> Term loans up to 15 years or flexible overdraft with drop line</li>
                                <li><strong>LRD:</strong> Step up EMI available (Lessee should be CAT A Tenant)</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">📈</span><h3>Forward Contracts</h3></div>
                            <ul class="feat-list">
                                <li>Notional limits up to <strong style="color: #10b981;">INR 3 Cr</strong></li>
                                <li>Loan Equivalent Risk of <strong>INR 45 lakhs</strong></li>
                                <li>MTM up to 8.33% (max 6 months USP)</li>
                            </ul>
                        </div>
                    </div>
                </div>
                '''

html = html[:assets_start] + new_assets_content + html[assets_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Business Assets updated")
