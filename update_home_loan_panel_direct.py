import re, codecs

panel_assets_replacement = '''<div class="info-panel" id="panel-assets">
                    <!-- Home Loan Benefit Calculator -->
                    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%); border-radius: 20px; padding: 28px; color: white; margin-bottom: 24px; box-shadow: 0 10px 30px rgba(30, 58, 138, 0.2);">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 20px;">
                            <div>
                                <span style="background: rgba(255,255,255,0.18); border-radius: 20px; padding: 4px 14px; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;">?? SOLITAIRE EXCLUSIVE RATE SAVINGS</span>
                                <h2 style="font-size: 1.65rem; font-weight: 900; margin: 10px 0 6px 0; color: white;">Home Loan Benefit Calculator</h2>
                                <p style="opacity: 0.85; font-size: 0.92rem; margin: 0;">Calculate your massive EMI &amp; interest savings with Solitaire rate (7.50% p.a.) vs standard market rate (7.80% p.a.).</p>
                            </div>
                            <div style="background: rgba(255,255,255,0.12); border: 1.5px solid rgba(255,255,255,0.25); border-radius: 16px; padding: 12px 20px; text-align: right;">
                                <div style="font-size: 0.72rem; opacity: 0.8; font-weight: 600; text-transform: uppercase;">Solitaire Rate Advantage</div>
                                <div style="font-size: 1.7rem; font-weight: 900; color: #34d399;">7.50% <span style="font-size: 0.85rem; opacity: 0.8; color: #94a3b8;">vs 7.80%</span></div>
                            </div>
                        </div>

                        <!-- Live Inputs Grid -->
                        <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 16px; padding: 20px; margin-bottom: 20px;">
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                                <!-- Loan Amount Slider -->
                                <div>
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                        <label style="font-size: 0.85rem; font-weight: 700; opacity: 0.9;">Loan Amount (?)</label>
                                        <span id="hl-panel-amount-disp" style="font-size: 1.15rem; font-weight: 900; color: #34d399;">? 1,00,00,000</span>
                                    </div>
                                    <input id="hl-panel-amount" type="range" min="1000000" max="50000000" step="500000" value="10000000" oninput="calcPanelHomeLoan()" style="width: 100%; accent-color: #34d399; cursor: pointer;">
                                    <div style="display: flex; justify-content: space-between; font-size: 0.72rem; opacity: 0.7; margin-top: 4px;">
                                        <span>?10 Lakh</span>
                                        <span>?5 Crore</span>
                                    </div>
                                </div>

                                <!-- Tenure Slider -->
                                <div>
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                        <label style="font-size: 0.85rem; font-weight: 700; opacity: 0.9;">Tenure (Years)</label>
                                        <span id="hl-panel-tenure-disp" style="font-size: 1.15rem; font-weight: 900; color: #34d399;">20 Years</span>
                                    </div>
                                    <input id="hl-panel-tenure" type="range" min="5" max="30" step="1" value="20" oninput="calcPanelHomeLoan()" style="width: 100%; accent-color: #34d399; cursor: pointer;">
                                    <div style="display: flex; justify-content: space-between; font-size: 0.72rem; opacity: 0.7; margin-top: 4px;">
                                        <span>5 Years</span>
                                        <span>30 Years</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Savings Results Cards Grid -->
                        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 18px;">
                            <div style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 14px; text-align: center;">
                                <div style="font-size: 0.72rem; opacity: 0.8; font-weight: 600; margin-bottom: 4px;">Standard Rate (7.80%) EMI</div>
                                <div id="hl-panel-emi-normal" style="font-size: 1.2rem; font-weight: 800; color: #fca5a5;">? 82,404</div>
                            </div>
                            <div style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 14px; text-align: center;">
                                <div style="font-size: 0.72rem; opacity: 0.8; font-weight: 600; margin-bottom: 4px;">Solitaire Rate (7.50%) EMI</div>
                                <div id="hl-panel-emi-solitaire" style="font-size: 1.2rem; font-weight: 900; color: #34d399;">? 80,559</div>
                            </div>
                            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); border-radius: 12px; padding: 14px; text-align: center; box-shadow: 0 4px 14px rgba(16,185,129,0.3);">
                                <div style="font-size: 0.72rem; color: #d1fae5; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">Monthly EMI Savings</div>
                                <div id="hl-panel-monthly-savings" style="font-size: 1.2rem; font-weight: 900; color: white;">? 1,845 / mo</div>
                            </div>
                        </div>

                        <!-- Big Total Interest Savings Card -->
                        <div style="background: rgba(255,255,255,0.12); border: 1.5px solid rgba(52,211,153,0.4); border-radius: 14px; padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                            <div>
                                <div style="font-size: 0.8rem; color: #a7f3d0; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">?? Total Interest Saved Over Tenure</div>
                                <div style="font-size: 0.82rem; opacity: 0.8; margin-top: 2px;">Interest at 7.80%: <span id="hl-panel-int-normal">?97.77 L</span> vs 7.50%: <span id="hl-panel-int-solitaire">?93.34 L</span></div>
                            </div>
                            <div id="hl-panel-total-savings" style="font-size: 2rem; font-weight: 900; color: #34d399; letter-spacing: -1px;">? 4,42,800</div>
                        </div>

                        <!-- Bonus Processing Fee Advantage -->
                        <div style="margin-top: 14px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; padding: 12px 18px; font-size: 0.85rem; color: #a7f3d0; display: flex; justify-content: space-between; align-items: center;">
                            <span>? <strong>Zero Processing Fee Advantage:</strong> Solitaire clients pay <strong>?0 processing fee</strong> (Save up to ?50,000).</span>
                            <span style="font-weight: 800; color: #34d399; background: rgba(0,0,0,0.2); padding: 3px 10px; border-radius: 20px;">+ ?50,000 SAVED</span>
                        </div>
                    </div>

                    <!-- All Loan Products Cards Grid -->
                    <h3 style="font-weight: 700; color: #111827; margin-bottom: 14px; font-size: 0.95rem;">All Solitaire Loan Products</h3>
                    <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">??</span><h3>Home Loan (Preferential)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #10b981;">7.50% p.a.</strong> (vs 7.80% market rate)</li>
                                <li>Max: <strong>?5 Crore+</strong> | Tenure: up to 30 years</li>
                                <li><strong style="color: #10b981;">Zero</strong> processing fee</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">??</span><h3>Loan Against Property (LAP)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #1e3a8a;">9.50% &ndash; 11.00% p.a.</strong></li>
                                <li>Max: <strong>?15 Crore</strong> | Tenure: 15 years</li>
                                <li><strong style="color: #10b981;">Zero</strong> processing fee</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">??</span><h3>Personal Loan (Solitaire)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #1e3a8a;">10.25% p.a.</strong></li>
                                <li>Up to <strong>?50 Lakh</strong> | Tenure: 5 years</li>
                                <li><strong style="color: #10b981;">Instant</strong> disbursal</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">??</span><h3>Loan Against Securities (LASP)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #1e3a8a;">9.00% &ndash; 10.50% p.a.</strong></li>
                                <li>Up to <strong>80% of portfolio value</strong></li>
                                <li>Pledge stocks, MFs &amp; bonds</li>
                            </ul>
                        </div>
                    </div>
                </div>'''

js_calc_panel = '''
<script>
function calcPanelHomeLoan() {
    const amountInput = document.getElementById('hl-panel-amount');
    const tenureInput = document.getElementById('hl-panel-tenure');
    if(!amountInput || !tenureInput) return;

    const p = parseFloat(amountInput.value) || 10000000;
    const yrs = parseInt(tenureInput.value) || 20;
    const n = yrs * 12;

    const rNormal = 7.80 / 100 / 12;
    const rSolitaire = 7.50 / 100 / 12;

    const emiNormal = p * rNormal * Math.pow(1 + rNormal, n) / (Math.pow(1 + rNormal, n) - 1);
    const emiSolitaire = p * rSolitaire * Math.pow(1 + rSolitaire, n) / (Math.pow(1 + rSolitaire, n) - 1);

    const monthlySave = emiNormal - emiSolitaire;
    const totalInterestNormal = (emiNormal * n) - p;
    const totalInterestSolitaire = (emiSolitaire * n) - p;
    const totalInterestSaved = totalInterestNormal - totalInterestSolitaire;

    const amtDisp = document.getElementById('hl-panel-amount-disp');
    if(amtDisp) amtDisp.textContent = '? ' + (p >= 10000000 ? (p/10000000).toFixed(2) + ' Cr' : (p/100000).toFixed(1) + ' Lakh');

    const tenureDisp = document.getElementById('hl-panel-tenure-disp');
    if(tenureDisp) tenureDisp.textContent = yrs + ' Years';

    const emiNormEl = document.getElementById('hl-panel-emi-normal');
    if(emiNormEl) emiNormEl.textContent = '? ' + Math.round(emiNormal).toLocaleString('en-IN');

    const emiSolEl = document.getElementById('hl-panel-emi-solitaire');
    if(emiSolEl) emiSolEl.textContent = '? ' + Math.round(emiSolitaire).toLocaleString('en-IN');

    const mSaveEl = document.getElementById('hl-panel-monthly-savings');
    if(mSaveEl) mSaveEl.textContent = '? ' + Math.round(monthlySave).toLocaleString('en-IN') + ' / mo';

    const intNormEl = document.getElementById('hl-panel-int-normal');
    if(intNormEl) intNormEl.textContent = '? ' + (totalInterestNormal/100000).toFixed(2) + ' L';

    const intSolEl = document.getElementById('hl-panel-int-solitaire');
    if(intSolEl) intSolEl.textContent = '? ' + (totalInterestSolitaire/100000).toFixed(2) + ' L';

    const totSaveEl = document.getElementById('hl-panel-total-savings');
    if(totSaveEl) totSaveEl.textContent = '? ' + Math.round(totalInterestSaved).toLocaleString('en-IN');
}

// Auto init on load
document.addEventListener('DOMContentLoaded', function() {
    calcPanelHomeLoan();
});
</script>
'''

def update_file(filepath):
    print(f'=== Updating Home Loan card title & panel calculator in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update Product Card 3 Title to "Home Loan"
    text = text.replace('<h3 class="product-title">Loans</h3>', '<h3 class="product-title">Home Loan</h3>')
    text = text.replace('<span class="product-timestamp">Bespoke borrowing &amp; credit solutions</span>', '<span class="product-timestamp">7.50% Solitaire vs 7.80% Normal Rate</span>')

    # 2. Replace panel-assets content with direct Home Loan Benefit Calculator
    panel_pattern = r'<div class="info-panel" id="panel-assets">.*?(?=<div class="info-panel" id="panel-investments">)'
    text = re.sub(panel_pattern, panel_assets_replacement + '\n\n', text, flags=re.DOTALL)

    # 3. Add js_calc_panel before </body>
    if 'calcPanelHomeLoan' not in text:
        text = text.replace('</body>', js_calc_panel + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done updating {filepath}')

update_file('experience_solitaire_dashboard_new.html')
update_file('experience_solitaire_dashboard.html')
