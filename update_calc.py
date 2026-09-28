import os
import re

file_path = 'home_loan_calculator.html'

if not os.path.exists(file_path):
    print("File not found")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for loan-type-btn
css_to_add = """
        .loan-type-btn {
            flex: 1;
            background: #f1f5f9;
            border: 1px solid #e2e8f0;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #475569;
            cursor: pointer;
            transition: all 0.2s;
        }
        .loan-type-btn.active {
            background: #1e3a8a;
            color: white;
            border-color: #1e3a8a;
        }
"""
content = content.replace('.slider-control {', css_to_add + '\n        .slider-control {')


# 2. Add Loan Type selector HTML
loan_type_html = """
                <!-- Loan Type Selector -->
                <div style="display: flex; gap: 8px; margin-bottom: 24px;">
                    <button class="loan-type-btn active" onclick="setLoanType(this, 'New')">New</button>
                    <button class="loan-type-btn" onclick="setLoanType(this, 'BT')">BT</button>
                    <button class="loan-type-btn" onclick="setLoanType(this, 'Top up')">Top up</button>
                    <button class="loan-type-btn" onclick="setLoanType(this, 'BT + Top up')">BT + Top up</button>
                </div>
"""
content = content.replace('<!-- 1. Property Value Input -->', loan_type_html + '\n                <!-- 1. Property Value Input -->')


# 3. Replace the Rate Cards HTML
old_rates_html = """<div class="rate-comparison-grid">
                    <div class="rate-card-box rate-card-normal">
                        <div style="font-size: 0.72rem; color: #dc2626; font-weight: 700; text-transform: uppercase;">Standard Market Rate</div>
                        <div style="font-size: 1.25rem; font-weight: 900; color: #991b1b; margin-top: 2px;">7.80% p.a.</div>
                    </div>
                    <div class="rate-card-box rate-card-solitaire">
                        <div style="font-size: 0.72rem; color: #047857; font-weight: 800; text-transform: uppercase;">Solitaire Rate</div>
                        <div style="font-size: 1.25rem; font-weight: 900; color: #065f46; margin-top: 2px;">7.50% p.a. 🔥</div>
                    </div>
                </div>"""

new_rates_html = """<div class="rate-comparison-grid">
                    <div class="rate-card-box rate-card-normal">
                        <div style="font-size: 0.72rem; color: #dc2626; font-weight: 700; text-transform: uppercase; margin-bottom: 6px;">Standard Market Rate</div>
                        <div style="display: flex; align-items: center; justify-content: center; gap: 4px;">
                            <input type="number" id="market-rate-input" step="0.05" value="7.80" style="width: 70px; font-size: 1.25rem; font-weight: 900; color: #991b1b; background: transparent; border: 1.5px dashed #f87171; text-align: center; border-radius: 4px; outline: none; padding: 2px;" oninput="updatePageHLCalc()">
                            <span style="font-size: 1.1rem; font-weight: 800; color: #991b1b;">% p.a.</span>
                        </div>
                    </div>
                    <div class="rate-card-box rate-card-solitaire">
                        <div style="font-size: 0.72rem; color: #047857; font-weight: 800; text-transform: uppercase; margin-bottom: 6px;">Solitaire Rate</div>
                        <div style="display: flex; align-items: center; justify-content: center; gap: 4px;">
                            <input type="number" id="solitaire-rate-input" step="0.05" value="7.50" style="width: 70px; font-size: 1.25rem; font-weight: 900; color: #065f46; background: transparent; border: 1.5px dashed #34d399; text-align: center; border-radius: 4px; outline: none; padding: 2px;" oninput="updatePageHLCalc()">
                            <span style="font-size: 1.1rem; font-weight: 800; color: #065f46;">% p.a. 🔥</span>
                        </div>
                    </div>
                </div>"""

# Replace by regex to be safe about spacing
content = re.sub(r'<div class="rate-comparison-grid">[\s\S]*?</div>\s*</div>', new_rates_html, content)


# 4. Replace results labels to have spans for dynamic values
content = content.replace('Standard Rate EMI (7.80%)', 'Standard Rate EMI (<span id="disp-normal-rate">7.80</span>%)')
content = content.replace('Solitaire Rate EMI (7.50%)', 'Solitaire Rate EMI (<span id="disp-sol-rate">7.50</span>%)')
content = content.replace('Interest (7.80%):', 'Interest (<span id="disp-int-normal-rate">7.80</span>%):')
content = content.replace('Solitaire (7.50%):', 'Solitaire (<span id="disp-int-sol-rate">7.50</span>%):')


# 5. Update Javascript
js_old = """const rNormal = 7.80 / 100 / 12;
            const rSolitaire = 7.50 / 100 / 12;"""

js_new = """const normalRateVal = parseFloat(document.getElementById('market-rate-input').value) || 7.80;
            const solRateVal = parseFloat(document.getElementById('solitaire-rate-input').value) || 7.50;

            const rNormal = normalRateVal / 100 / 12;
            const rSolitaire = solRateVal / 100 / 12;
            
            // Update the display labels
            document.getElementById('disp-normal-rate').textContent = normalRateVal.toFixed(2);
            document.getElementById('disp-sol-rate').textContent = solRateVal.toFixed(2);
            document.getElementById('disp-int-normal-rate').textContent = normalRateVal.toFixed(2);
            document.getElementById('disp-int-sol-rate').textContent = solRateVal.toFixed(2);"""

content = content.replace(js_old, js_new)

# Add setLoanType function
js_function = """
        let currentLoanType = 'New';
        function setLoanType(btn, type) {
            document.querySelectorAll('.loan-type-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentLoanType = type;
            // Additional logic can be added here if BT/Topup needs to change input labels
        }
        
        function updatePageHLCalc() {"""
        
content = content.replace('function updatePageHLCalc() {', js_function)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated home_loan_calculator.html successfully!")
