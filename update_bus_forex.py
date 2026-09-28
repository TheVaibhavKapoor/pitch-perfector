# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

b_start = html.find('id="segment-business-content"')
forex_start = html.find('id="panel-business-forex"', b_start)
forex_end = html.find('id="panel-business-other"', forex_start)

new_forex_content = '''id="panel-business-forex" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 16px;">Trade & Forex</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Exclusive global trade pricing and digital execution platforms for Solitaire Business clients.</p>
                    
                    <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">🌐</span><h3>Trade Pricing & GTA</h3></div>
                            <ul class="feat-list">
                                <li>Eligible for <strong>GTA variant</strong> linked to Solitaire CA variant (Ace Variant)</li>
                                <li><strong style="color: #10b981;">NIL Inward Remittance, FICR and Export LC advising charges</strong></li>
                                <li>Waived off Throughput requirement & priority execution</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">💻</span><h3>Digital Platforms</h3></div>
                            <ul class="feat-list">
                                <li><strong>Kotak fyn - Trade:</strong> Single interface for Remittances, LC, BG & real-time insights</li>
                                <li><strong style="color: #10b981;">Fx Live Platform:</strong> Book Fx easily, live rates (Cash/TOM/Spot), market alerts</li>
                                <li><strong>Kotak Remit:</strong> Instant individual outward remittance (upto Rs.50,000/txn)</li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">🛡️</span><h3>Hedging & Advisory</h3></div>
                            <ul class="feat-list">
                                <li>Pre-approved forward hedging limits (LER) for import/export risk</li>
                                <li>Exclusive advisory by FX specialists for hedging strategies</li>
                                <li><strong>Dedicated Trade & Treasury Relationship Manager</strong></li>
                            </ul>
                        </div>
                        <div class="feature-card">
                            <div class="feat-card-header"><span class="feat-icon">💳</span><h3>Travel Forex</h3></div>
                            <ul class="feat-list">
                                <li>Exclusive FX pricing for Solitaire-linked corporate salary relationships</li>
                                <li>Doorstep delivery of <strong>Kotak World travel forex card</strong></li>
                                <li>Preferential loading rates & multi-currency convenience</li>
                            </ul>
                        </div>
                    </div>
                </div>
                '''

html = html[:forex_start] + new_forex_content + html[forex_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Business Forex updated")
