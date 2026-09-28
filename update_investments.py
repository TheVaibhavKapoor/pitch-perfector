# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_investments = '''<div id="panel-investments" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 16px;">Investment Suite</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Access institutional-grade investment strategies and competitive pricing without subscription fees.</p>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px;">
                        <div style="grid-column: 1 / -1;">
                            <h3 style="font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;">Competitive Pricing & Support</h3>
                            <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">💰</span><h3>Pricing & AMC</h3></div>
                                    <ul class="feat-list">
                                        <li>Competitive pricing <strong>without subscription fees</strong></li>
                                        <li><strong style="color: #10b981;">No AMC</strong> on Demat</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📈</span><h3>Equity & Futures</h3></div>
                                    <ul class="feat-list">
                                        <li>Delivery @ <strong style="color: #10b981;">0.10%</strong></li>
                                        <li>Intraday & Futures @ <strong style="color: #10b981;">0.01%</strong></li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📊</span><h3>Margin Trading (MTF)</h3></div>
                                    <ul class="feat-list">
                                        <li><strong style="color: #10b981;">9.69%</strong> (For NTB customers)</li>
                                        <li><strong style="color: #10b981;">9.75%</strong> (For ETB customers)</li>
                                    </ul>
                                </div>
                                <div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">📞</span><h3>Options & Dealer</h3></div>
                                    <ul class="feat-list">
                                        <li><strong>Dedicated Dealer Support</strong> included</li>
                                        <li><strong style="color: #10b981;">₹20 per lot</strong> (with dealer)</li>
                                        <li><strong style="color: #10b981;">₹10 per lot</strong> (without dealer)</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = re.sub(
    r'<div id="panel-investments" class="info-panel">.*?</div>\s*</div>\s*</div>\s*</div>',
    new_investments,
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated experience_solitaire_dashboard.html')
