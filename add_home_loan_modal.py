import re, codecs

modal_html_and_js = '''
<!-- Home Loan Savings Modal -->
<div id="homeLoanModal" style="display:none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(6px); z-index: 9999; align-items: center; justify-content: center; padding: 20px; box-sizing: border-box;">
    <div style="background: white; border-radius: 20px; max-width: 650px; width: 100%; max-height: 90vh; overflow-y: auto; padding: 32px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.3); position: relative; border: 1px solid #e2e8f0; animation: modalFadeIn 0.25s ease;">
        
        <!-- Modal Header -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #f1f5f9; padding-bottom: 16px;">
            <div>
                <span style="font-size: 0.75rem; font-weight: 800; color: #1e3a8a; background: #eff6ff; padding: 4px 12px; border-radius: 20px; letter-spacing: 0.5px;">SOLITAIRE EXCLUSIVE PRICING</span>
                <h2 style="font-size: 1.4rem; font-weight: 800; color: #0f172a; margin: 8px 0 0 0;">Home Loan Savings Calculator</h2>
            </div>
            <button onclick="closeHomeLoanModal()" style="background: #f1f5f9; border: none; width: 36px; height: 36px; border-radius: 50%; font-size: 1.2rem; cursor: pointer; color: #64748b; font-weight: 700;">&times;</button>
        </div>

        <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 24px;">Compare your savings with Solitaire preferential rate (7.50% p.a.) versus standard market rate (7.80% p.a.).</p>

        <!-- Inputs Section -->
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 20px; margin-bottom: 24px;">
            <!-- Loan Amount Slider -->
            <div style="margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <label style="font-size: 0.85rem; font-weight: 700; color: #1e3a8a;">Loan Amount</label>
                    <span id="modal-hl-amount-disp" style="font-size: 1rem; font-weight: 800; color: #0f172a;">? 1,00,00,000</span>
                </div>
                <input id="modal-hl-amount" type="range" min="1000000" max="50000000" step="500000" value="10000000" oninput="calcHomeLoanModal()" style="width: 100%; accent-color: #1e3a8a; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #94a3b8; margin-top: 4px;">
                    <span>?10 Lakh</span>
                    <span>?5 Crore</span>
                </div>
            </div>

            <!-- Tenure Slider -->
            <div style="margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <label style="font-size: 0.85rem; font-weight: 700; color: #1e3a8a;">Tenure (Years)</label>
                    <span id="modal-hl-tenure-disp" style="font-size: 1rem; font-weight: 800; color: #0f172a;">20 Years</span>
                </div>
                <input id="modal-hl-tenure" type="range" min="5" max="30" step="1" value="20" oninput="calcHomeLoanModal()" style="width: 100%; accent-color: #1e3a8a; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #94a3b8; margin-top: 4px;">
                    <span>5 Years</span>
                    <span>30 Years</span>
                </div>
            </div>

            <!-- Rate comparison pill -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 16px;">
                <div style="background: white; border: 1px solid #cbd5e1; border-radius: 10px; padding: 10px 14px; text-align: center;">
                    <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Standard Market Rate</div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: #dc2626;">7.80% p.a.</div>
                </div>
                <div style="background: #ecfdf5; border: 1.5px solid #a7f3d0; border-radius: 10px; padding: 10px 14px; text-align: center;">
                    <div style="font-size: 0.72rem; color: #047857; font-weight: 700;">Solitaire Preferential Rate</div>
                    <div style="font-size: 1.1rem; font-weight: 900; color: #059669;">7.50% p.a. ??</div>
                </div>
            </div>
        </div>

        <!-- Savings Results Section -->
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); border-radius: 16px; padding: 24px; color: white; margin-bottom: 20px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 16px;">
                <div>
                    <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 600; margin-bottom: 2px;">Standard Rate Monthly EMI (7.80%)</div>
                    <div id="modal-emi-normal" style="font-size: 1.25rem; font-weight: 800; color: #fca5a5;">? 82,404</div>
                </div>
                <div>
                    <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 600; margin-bottom: 2px;">Solitaire Monthly EMI (7.50%)</div>
                    <div id="modal-emi-solitaire" style="font-size: 1.25rem; font-weight: 800; color: #34d399;">? 80,559</div>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: center;">
                <div>
                    <div style="font-size: 0.78rem; color: #cbd5e1; font-weight: 600;">Monthly EMI Savings</div>
                    <div id="modal-monthly-savings" style="font-size: 1.4rem; font-weight: 900; color: #34d399;">? 1,845 / mo</div>
                </div>
                <div style="background: rgba(255,255,255,0.12); border-radius: 12px; padding: 12px; text-align: right;">
                    <div style="font-size: 0.75rem; color: #a7f3d0; font-weight: 700; text-transform: uppercase;">Total Interest Saved</div>
                    <div id="modal-total-interest-saved" style="font-size: 1.6rem; font-weight: 900; color: #ffffff;">? 4,42,800</div>
                </div>
            </div>
        </div>

        <!-- Bonus Zero Processing Fee Callout -->
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 14px; font-size: 0.85rem; color: #166534; display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
            <span>?? <strong>Zero Processing Fee Savings:</strong> Waived (Save up to ?50,000)</span>
            <span style="font-weight: 800; color: #15803d;">+ ? 50,000</span>
        </div>

        <button onclick="closeHomeLoanModal()" style="width: 100%; padding: 14px; background: #1e3a8a; color: white; border: none; border-radius: 10px; font-size: 1rem; font-weight: 800; cursor: pointer; transition: background 0.2s;">
            CLOSE CALCULATOR
        </button>
    </div>
</div>

<script>
    function openHomeLoanModal() {
        const modal = document.getElementById('homeLoanModal');
        if(modal) {
            modal.style.display = 'flex';
            calcHomeLoanModal();
        }
    }

    function closeHomeLoanModal() {
        const modal = document.getElementById('homeLoanModal');
        if(modal) modal.style.display = 'none';
    }

    function calcHomeLoanModal() {
        const p = parseFloat(document.getElementById('modal-hl-amount').value) || 10000000;
        const yrs = parseInt(document.getElementById('modal-hl-tenure').value) || 20;
        const n = yrs * 12;

        const rNormal = 7.80 / 100 / 12;
        const rSolitaire = 7.50 / 100 / 12;

        // EMI Formula: P * r * (1+r)^n / ((1+r)^n - 1)
        const emiNormal = p * rNormal * Math.pow(1 + rNormal, n) / (Math.pow(1 + rNormal, n) - 1);
        const emiSolitaire = p * rSolitaire * Math.pow(1 + rSolitaire, n) / (Math.pow(1 + rSolitaire, n) - 1);

        const monthlySave = emiNormal - emiSolitaire;
        const totalInterestNormal = (emiNormal * n) - p;
        const totalInterestSolitaire = (emiSolitaire * n) - p;
        const totalInterestSaved = totalInterestNormal - totalInterestSolitaire;

        document.getElementById('modal-hl-amount-disp').textContent = '? ' + (p >= 10000000 ? (p/10000000).toFixed(2) + ' Cr' : (p/100000).toFixed(1) + ' Lakh');
        document.getElementById('modal-hl-tenure-disp').textContent = yrs + ' Years';

        document.getElementById('modal-emi-normal').textContent = '? ' + Math.round(emiNormal).toLocaleString('en-IN');
        document.getElementById('modal-emi-solitaire').textContent = '? ' + Math.round(emiSolitaire).toLocaleString('en-IN');
        document.getElementById('modal-monthly-savings').textContent = '? ' + Math.round(monthlySave).toLocaleString('en-IN') + ' / mo';
        document.getElementById('modal-total-interest-saved').textContent = '? ' + Math.round(totalInterestSaved).toLocaleString('en-IN');
    }
</script>
'''

def update_file(filepath):
    print(f'=== Updating Home Loan hero card & adding Modal in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update Home Loan Hero Card rates from 8.75% / 9.25% to 7.50% / 7.80%
    text = re.sub(r'<span style="font-size: 2\.8rem; font-weight: 900; letter-spacing: -2px; line-height: 1;">8\.75%</span>', '<span style="font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; line-height: 1;">7.50%</span>', text)
    text = re.sub(r'Standard rate starts at 9\.25% &mdash; You save <strong style="color: #6ee7b7;">0\.50%</strong>', 'Standard rate starts at 7.80% &mdash; You save <strong style="color: #6ee7b7;">0.30%</strong>', text)

    # 2. Add onclick="openHomeLoanModal()" to Home Loan Hero Card container and add a Calculate Button inside
    hero_search = r'(<!-- FEATURED: Home Loan Hero Card -->\s*<div style="background: linear-gradient\(135deg, #1e3a8a 0%, #1e40af 50%, #1d4ed8 100%\);[^">]*)"'
    
    # Check if click handler exists
    if 'openHomeLoanModal()' not in text:
        # Add button inside Home Loan hero card
        old_hero_end = '<!-- All Solitaire Loan Products -->'
        new_hero_btn = '''
                        <div style="margin-top: 18px; text-align: right; position: relative; z-index: 2;">
                            <button onclick="openHomeLoanModal()" style="background: #ffffff; color: #1e3a8a; border: none; padding: 10px 22px; border-radius: 8px; font-weight: 800; font-size: 0.88rem; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.15); transition: transform 0.2s;">
                                ?? CALCULATE INTEREST SAVINGS &rarr;
                            </button>
                        </div>
                    </div>

                    <!-- All Solitaire Loan Products -->'''
        text = text.replace('</div>\n\n                    <!-- All Solitaire Loan Products -->', new_hero_btn)
        text = text.replace('</div>\r\n\r\n                    <!-- All Solitaire Loan Products -->', new_hero_btn)

    # 3. Append modal before </body>
    if 'id="homeLoanModal"' not in text:
        text = text.replace('</body>', modal_html_and_js + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done updating {filepath}')

update_file('experience_solitaire_dashboard_new.html')
update_file('experience_solitaire_dashboard.html')
