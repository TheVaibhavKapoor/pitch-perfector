import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard_new.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_panel = '''                <div id="panel-assets" class="info-panel">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 8px;">Kotak Solitaire Program</h2>
                    <h3 style="font-size: 1.1rem; font-weight: 700; color: #d61f26; margin-bottom: 16px;">Pre-Approved Asset Offer</h3>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Enjoy exclusive access to a range of bespoke pre-approved lending solutions based on your Relationship Value (RV).</p>
                    
                    <div style="grid-column: 1 / -1;">
                        <div class="product-features-grid">
                            <!-- 1. Home Loan -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Home Loan</h3></div>
                                <ul class="feat-list">
                                    <li>Pre-approved Home loan of <strong>3X RV</strong></li>
                                    <li>Up to <strong>? 7.5 Crore</strong></li>
                                    <li><strong>Nil</strong> Processing Fee</li>
                                </ul>
                            </div>
                            
                            <!-- 2. Car Loan -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Car Loan</h3></div>
                                <ul class="feat-list">
                                    <li>Pre-approved car loan of <strong>40% of RV</strong></li>
                                    <li>Up to <strong>? 1 Crore</strong> (whichever is lower)</li>
                                </ul>
                            </div>
                            
                            <!-- 3. Pre-approved Credit Line -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Pre-approved Credit Line</h3></div>
                                <ul class="feat-list">
                                    <li>Withdrawal <strong>15% of RV</strong></li>
                                    <li>Up to <strong>? 25 lakhs</strong></li>
                                </ul>
                            </div>
                            
                            <!-- 4. Working Capital -->
                            <div class="feature-card">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Working Capital</h3></div>
                                <ul class="feat-list">
                                    <li>Up to <strong>120% of collateral value</strong></li>
                                    <li>Plus up to <strong>20% of additional limit</strong></li>
                                    <li>Ad hoc cumulative period of <strong>120 days</strong></li>
                                </ul>
                            </div>
                            
                            <!-- 5. Loan Against Property -->
                            <div class="feature-card" style="grid-column: 1 / -1;">
                                <div class="feat-card-header"><span class="feat-icon">??</span><h3>Loan Against Property (LAP)</h3></div>
                                <ul class="feat-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                                    <li>Avail LAP of up to <strong>3X RV</strong>, up to <strong>? 7.5 Crore</strong> (fungible against HL offer)</li>
                                    <li><strong>Combination of properties</strong> acceptable for availing LAP loan</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div style="margin-top: 24px; padding: 16px; background: #f8fafc; border-radius: 8px; border-left: 4px solid #94a3b8; font-size: 0.85rem; color: #64748b;">
                            <strong>Note:</strong> Credit at the sole discretion of the bank and subject to guidelines issued by RBI from time to time.<br>
                            This is a confidential document.
                        </div>
                    </div>
                </div>'''

new_business_panel = new_panel.replace('id="panel-assets"', 'id="panel-business-assets"')

content = re.sub(r'<div id="panel-assets" class="info-panel">.*?(?=<div id="panel-investments" class="info-panel">)', new_panel + '\n\n', content, flags=re.DOTALL)
content = re.sub(r'<div\s+id="panel-business-assets"[^>]*>.*?(?=<div id="panel-business-investments" class="info-panel">|<div id="panel-business-forex" class="info-panel">)', new_business_panel + '\n\n', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated NTB Loans write-ups!')
