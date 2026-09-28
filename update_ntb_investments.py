import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard_new.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_panel = '''                <div id="panel-investments" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 8px;">Competitive Pricing</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">(without subscription fees)</p>
                    
                    <div style="grid-column: 1 / -1;">
                        <div class="product-features-grid">
                            <!-- 1. Support -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">?????</span><h3>Dealer Support</h3></div>
                                <ul class="feat-list">
                                    <li><strong>Dedicated</strong> Dealer Support</li>
                                </ul>
                            </div>
                            
                            <!-- 2. Delivery & Intraday -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Equity & Futures</h3></div>
                                <ul class="feat-list">
                                    <li>Delivery @ <strong>0.10%</strong></li>
                                    <li>Intraday & Futures @ <strong>0.01%</strong></li>
                                </ul>
                            </div>
                            
                            <!-- 3. MTF -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Margin Trading (MTF)</h3></div>
                                <ul class="feat-list">
                                    <li>MTF @ <strong>9.69%</strong> (For NTB customers)</li>
                                </ul>
                            </div>
                            
                            <!-- 4. Options -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Options Trading</h3></div>
                                <ul class="feat-list">
                                    <li><strong>?20</strong> per lot (with dealer)</li>
                                    <li><strong>?10</strong> per lot (without dealer)</li>
                                </ul>
                            </div>
                            
                            <!-- 5. AMC -->
                            <div class="feature-card" style="grid-column: 1 / -1;">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Demat Account</h3></div>
                                <ul class="feat-list">
                                    <li><strong>No AMC</strong> on Demat</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>'''

new_business_panel = new_panel.replace('id="panel-investments"', 'id="panel-business-investments"')

content = re.sub(r'<div id="panel-investments" class="info-panel">.*?(?=<div id="panel-forex" class="info-panel">)', new_panel + '\n\n', content, flags=re.DOTALL)
content = re.sub(r'<div\s+id="panel-business-investments"[^>]*>.*?(?=<div id="panel-business-forex" class="info-panel">)', new_business_panel + '\n\n', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated NTB Investments write-ups!')
