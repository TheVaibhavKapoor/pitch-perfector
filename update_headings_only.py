import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def save(f, c):
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

# ─────────────────────────────────────────────────────────────────────────────
# NEW LOANS SELECTOR GRID (HEADINGS & ICONS ONLY)
# ─────────────────────────────────────────────────────────────────────────────
NEW_LOAN_BOXES_GRID = """<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: 20px;" id="loan-product-selector-grid">

    <div class="loan-prod-box active" onclick="selectLoanProduct('hl', this)" style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">🏠</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #1e3a8a;">Home Loan</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('lap', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">🏢</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">LAP</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('las', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">📈</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">LAS</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('od', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">💳</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">Credit Line / OD</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('auto', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">🚗</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">Auto Loan</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('personal', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">💼</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">Personal Loan</div>
    </div>

</div>"""


# ─────────────────────────────────────────────────────────────────────────────
# NEW INVESTMENTS SELECTOR GRID (HEADINGS & ICONS ONLY)
# ─────────────────────────────────────────────────────────────────────────────
NEW_INV_BOXES_GRID = """<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: 20px;" id="inv-product-selector-grid">

    <div class="inv-prod-box active" onclick="selectInvProduct('demat', this)" style="background: #ecfdf5; border: 2px solid #10b981; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">📊</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #065f46;">Demat & Equity</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('mf', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">📈</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">Mutual Funds</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('ipo', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">🚀</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">IPO (ASBA)</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('mtf', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">⚡</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">MTF Leverage</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('aif', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">💎</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">AIF & PMS</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('lrs', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 14px 10px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.6rem; margin-bottom: 4px;">🌐</div>
        <div style="font-weight: 800; font-size: 0.9rem; color: #0f172a;">Global LRS</div>
    </div>

</div>"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)
print(f"\n==================== Updating Headings Only in {fname} ====================")

# Replace loan grid
pattern_loan_grid = re.compile(r'<div[^>]*id="loan-product-selector-grid"[^>]*>.*?</div>\s*</div>', re.DOTALL)
c = pattern_loan_grid.sub(NEW_LOAN_BOXES_GRID, c)
print("Replaced Loan selector grid with headings-only boxes!")

# Replace inv grid
pattern_inv_grid = re.compile(r'<div[^>]*id="inv-product-selector-grid"[^>]*>.*?</div>\s*</div>', re.DOTALL)
c = pattern_inv_grid.sub(NEW_INV_BOXES_GRID, c)
print("Replaced Investment selector grid with headings-only boxes!")

save(fname, c)
print("Successfully saved headings-only selector boxes!")
