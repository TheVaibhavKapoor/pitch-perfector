# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the panel-business-cc inside the business wrapper
b_start = html.find('id="segment-business-content"')
cc_start = html.find('id="panel-business-cc"', b_start)
cc_end = html.find('id="panel-business-assets"', cc_start)

new_cc_content = '''id="panel-business-cc" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 16px;">Kotak Solitaire Business Credit Card</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Highlights: Low interest rates, Low Forex Markup, Accelerated Rewards, and Lounge Access.</p>
                    
                    <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">💎</span><h3>Core Features</h3></div>
                            <ul class="feat-list">
                                <li>Interest Free Period: <strong style="color: #10b981;">Up to 48 Days</strong></li>
                                <li>Interest Rate: <strong style="color: #10b981;">1.99% / month</strong></li>
                                <li>Forex Mark-up: <strong style="color: #10b981;">1.99%</strong></li>
                                <li>No cash withdrawal allowed</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">⭐</span><h3>Reward Points (RP)</h3></div>
                            <ul class="feat-list">
                                <li><strong style="color: #10b981;">7X (14 RP)</strong> per ₹150 on Kotak UnBox</li>
                                <li><strong>2 RP</strong> per ₹150 on normal categories</li>
                                <li><strong>1 RP</strong> per ₹150 on Utilities/Tax</li>
                                <li>Unlock up to <strong style="color: #10b981;">INR 500</strong> in RP on tax</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">✈️</span><h3>Travel & Lifestyle</h3></div>
                            <ul class="feat-list">
                                <li><strong style="color: #10b981;">4 Domestic</strong> Lounge Access / year</li>
                                <li><strong style="color: #10b981;">1 International</strong> Lounge Access / year</li>
                                <li>Redemption: <strong>1 RP = ₹0.5</strong> on UnBox</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">⛽</span><h3>Fuel & Insurance</h3></div>
                            <ul class="feat-list">
                                <li><strong style="color: #10b981;">1% Fuel Surcharge Waiver</strong> (capped at ₹5k)</li>
                                <li>Complimentary general insurance</li>
                            </ul>
                        </div>
                    </div>
                </div>
                '''

html = html[:cc_start] + new_cc_content + html[cc_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Business CC updated")
