import os
import re

files_to_update = [
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard_new.html'
]

new_lead_content = """<h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 12px; margin-top: 8px; color: #0f172a;">Target Program</h4>
        <select class="ntb-modal-input" style="appearance: auto;">
            <option>Kotak Solitaire</option>
            <option>Kotak Privy+</option>
            <option>Kotak Privy</option>
        </select>

        <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 12px; margin-top: 8px; color: #0f172a;">Cross-Sell Interests</h4>
        <div class="lead-checkbox-group">
            <label class="lead-checkbox-label">
                <input type="checkbox" onchange="document.getElementById('asset-products').style.display = this.checked ? 'flex' : 'none'"> Asset / Lending
            </label>
            <div id="asset-products" style="display:none; margin-left: 28px; flex-direction:column; gap:8px; margin-bottom: 8px;">
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Home Loan</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Loan Against Property (LAP)</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Auto Loan</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Working Capital / OD</label>
            </div>

            <label class="lead-checkbox-label">
                <input type="checkbox" onchange="document.getElementById('investment-products').style.display = this.checked ? 'flex' : 'none'"> Investment & Wealth
            </label>
            <div id="investment-products" style="display:none; margin-left: 28px; flex-direction:column; gap:8px; margin-bottom: 8px;">
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Kotak Trinity (3-in-1)</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Mutual Funds / SIP</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Portfolio Management Service (PMS)</label>
            </div>

            <label class="lead-checkbox-label">
                <input type="checkbox" onchange="document.getElementById('cc-products').style.display = this.checked ? 'flex' : 'none'"> Credit Cards
            </label>
            <div id="cc-products" style="display:none; margin-left: 28px; flex-direction:column; gap:8px; margin-bottom: 8px;">
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Solitaire Metal Card</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Privy+ Signature Card</label>
                <label style="font-size: 0.85rem; color: #475569; display: flex; align-items: center; gap: 8px;"><input type="checkbox"> Privy Signature Card</label>
            </div>
        </div>"""

old_pattern = r'<h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 12px; margin-top: 8px; color: #0f172a;">Interested In</h4>\s*<div class="lead-checkbox-group">[\s\S]*?</div>'

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_lead_content, content)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated lead modal in {filename}")
        else:
            print(f"Could not find exact pattern in {filename}")
