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
# NEW LOANS PANEL HTML (SMALL BOXES + DYNAMIC BELOW CONTENT WITH FEATURES, PITCH, EXPANDABLE CALCULATOR)
# ─────────────────────────────────────────────────────────────────────────────
NEW_LOANS_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">Bespoke Lending & Liquidity Solutions</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">Select a loan product to view features, RM pitch scripts, and interactive rate calculators.</p>

<!-- Small Product Selector Boxes Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; margin-bottom: 20px;" id="loan-product-selector-grid">

    <div class="loan-prod-box active" onclick="selectLoanProduct('hl', this)" style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">🏠</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #1e3a8a;">Home Loan</div>
        <div style="font-size: 0.72rem; color: #3b82f6; font-weight: 600;">Up to ₹7.5 Cr</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('lap', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">🏢</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">LAP</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Property Credit</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('las', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">📈</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">LAS</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Instant OD Line</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('od', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">💳</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">Credit Line</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">₹25L Overdraft</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('auto', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">🚗</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">Auto Loan</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">100% On-Road</div>
    </div>

    <div class="loan-prod-box" onclick="selectLoanProduct('personal', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; background: #ffffff; margin-bottom: 4px;">💼</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">Personal Loan</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Instant Unsecured</div>
    </div>

</div>

<!-- Dynamic Detail Container Below -->
<div id="loan-product-detail" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">

    <!-- Default: Home Loan (HL) -->
    <div id="loan-content-hl" class="loan-detail-pane" style="display: block;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🏠</span> Home Loan (HL) Details
            </h3>
            <span style="background: #eff6ff; color: #2563eb; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Pre-approved up to ₹7.5 Cr</span>
        </div>

        <!-- 1. Features -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0; display: flex; align-items: center; gap: 6px;">
            <span>📌</span> Key Features & Privileges
        </h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Preferential Rate Advantage:</strong> ~0.25% interest rate discount for Solitaire members</li>
            <li><strong>Zero Processing Fees</strong> & priority credit underwriting with fast-track processing</li>
            <li>Balance Transfer facility with high-quantum top-up loans at preferential rates</li>
            <li>Dedicated Relationship Manager for end-to-end documentation & doorstep assistance</li>
        </ul>

        <!-- 2. Pitches -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0; display: flex; align-items: center; gap: 6px;">
            <span>🗣️</span> Relationship Manager Pitch Script
        </h4>
        <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “As a Kotak Solitaire member, you have access to a pre-approved Home Loan limit up to ₹7.5 Crore at a preferential rate advantage of ~0.25% with zero processing fees. Whether you are purchasing a luxury property or transferring an existing high-cost loan, we can save you lakhs in interest outgo.”
        </div>

        <!-- 3. Expandable Calculator -->
        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span style="display: flex; align-items: center; gap: 8px;">
                    <span>🧮</span> Home Loan Interest Savings Calculator (Expandable)
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                    <div>
                        <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Loan Amount (₹ Crore)</label>
                        <input type="range" id="hl-amt" min="1" max="10" step="0.5" value="3" oninput="calcHLSavings()" style="width: 100%;">
                        <div style="font-weight: 800; color: #1e3a8a; font-size: 1rem; margin-top: 4px;" id="hl-amt-val">₹3.0 Crore</div>
                    </div>
                    <div>
                        <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Solitaire Rate Discount</label>
                        <select id="hl-disc" onchange="calcHLSavings()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1; font-weight: 600;">
                            <option value="0.25" selected>0.25% p.a. Discount</option>
                            <option value="0.35">0.35% p.a. Discount</option>
                            <option value="0.50">0.50% p.a. Discount</option>
                        </select>
                    </div>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 14px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #1e40af; display: block;">Estimated First-Year Interest Savings</span>
                    <strong style="font-size: 1.4rem; color: #1e3a8a;" id="hl-savings-val">₹75,000 / year</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- LAP Content -->
    <div id="loan-content-lap" class="loan-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🏢</span> Loan Against Property (LAP) Details
            </h3>
            <span style="background: #f0fdf4; color: #16a34a; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Tenures up to 15 Years</span>
        </div>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>High quantum long-term liquidity against residential or commercial real estate</li>
            <li>Flexible repayment tenures up to <strong>15 years</strong> with custom EMI options</li>
            <li>Special commercial property rates exclusive for Solitaire business owners</li>
            <li>Multi-property collateral pooling to maximize overall loan eligibility</li>
        </ul>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #16a34a; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “If you wish to unlock substantial liquidity from your real estate holdings without selling assets, LAP offers high-quantum capital at low Solitaire interest rates for business expansion or personal investments.”
        </div>
        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 LAP Monthly Outgo Estimator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For a <strong>₹2 Crore LAP</strong> over 10 years at 8.75% p.a. Solitaire rate:</p>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #166534;">Estimated Monthly EMI</span><br>
                    <strong style="font-size: 1.3rem; color: #15803d;">~₹2,50,600 / month</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- LAS Content -->
    <div id="loan-content-las" class="loan-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>📈</span> Loan Against Securities (LAS) Details
            </h3>
            <span style="background: #fff7ed; color: #c2410c; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Instant OD Line</span>
        </div>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Instant digital overdraft against Mutual Funds, Equities, Bonds & Life Insurance policies</li>
            <li><strong>Pay interest ONLY on the amount utilized</strong> for the exact number of days used</li>
            <li>Digital pledge & unpledge with zero prepayment or foreclosure charges</li>
            <li>Retain full asset ownership, dividends, and compounding growth benefits</li>
        </ul>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #ea580c; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Instead of redeeming your equity portfolio and incurring capital gains tax, LAS allows you to pledge your securities digitally for an instant credit line while your portfolio continues to compound.”
        </div>
        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 LAS Daily Interest Calculator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹50 Lakh utilized</strong> for 15 days at 9.0% p.a.:</p>
                <div style="background: #fff7ed; border: 1px solid #fed7aa; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #9a3412;">Interest Outgo for 15 Days</span><br>
                    <strong style="font-size: 1.3rem; color: #c2410c;">~₹18,493</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- OD Content -->
    <div id="loan-content-od" class="loan-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>💳</span> Credit Line / Overdraft Details
            </h3>
            <span style="background: #f3e8ff; color: #7e22ce; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Pre-approved ₹25L</span>
        </div>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Pre-approved overdraft limit up to <strong>₹25 Lakh</strong> linked directly to primary account</li>
            <li>Mid-Month Advance facility to bridge transient liquidity needs</li>
            <li>Solitaire preferential OD interest rates with zero annual renewal fees</li>
        </ul>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #9333ea; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Your Solitaire account includes a pre-approved ₹25 Lakh overdraft limit that serves as a seamless liquidity cushion for business or personal emergency cash needs.”
        </div>
        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 Overdraft Usage Estimator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹10 Lakh utilized for 7 days</strong> at 9.5% p.a.:</p>
                <div style="background: #f3e8ff; border: 1px solid #e9d5ff; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #6b21a8;">7-Day Interest Cost</span><br>
                    <strong style="font-size: 1.3rem; color: #7e22ce;">~₹1,821</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- Auto Content -->
    <div id="loan-content-auto" class="loan-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🚗</span> Auto Loan Details
            </h3>
            <span style="background: #fef2f2; color: #b91c1c; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">100% On-Road Funding</span>
        </div>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Up to <strong>100% On-Road Funding</strong> for luxury & super-premium vehicles</li>
            <li>Custom step-up or balloon EMI options to optimize monthly cash flow</li>
            <li>Nil foreclosure penalty after initial lock-in period</li>
        </ul>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #dc2626; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Planning your next luxury automobile purchase? Solitaire provides 100% on-road funding with tailored balloon EMIs so your working capital stays untouched.”
        </div>
        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 Luxury Auto EMI Estimator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹75 Lakh Auto Loan</strong> for 5 years @ 8.50% p.a.:</p>
                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #991b1b;">Monthly EMI</span><br>
                    <strong style="font-size: 1.3rem; color: #b91c1c;">~₹1,53,900 / month</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- Personal Content -->
    <div id="loan-content-personal" class="loan-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>💼</span> Personal Loan Details
            </h3>
            <span style="background: #ecfdf5; color: #047857; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Instant 1-Click Disbursement</span>
        </div>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Pre-approved unsecured credit line up to <strong>₹25 Lakh</strong></li>
            <li>Instant 1-click digital disbursement with zero paper documentation</li>
            <li>Special fixed interest rates exclusive to Solitaire banking relationships</li>
        </ul>
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #059669; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Need quick unsecured capital for a short-term requirement? Your pre-approved ₹25 Lakh Solitaire Personal Loan can be credited to your account instantly.”
        </div>
        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 Personal Loan EMI Estimator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹15 Lakh</strong> for 3 years @ 10.5% p.a.:</p>
                <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #065f46;">Monthly EMI</span><br>
                    <strong style="font-size: 1.3rem; color: #047857;">~₹48,750 / month</strong>
                </div>
            </div>
        </details>
    </div>

</div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# NEW INVESTMENTS PANEL HTML (SMALL BOXES + DYNAMIC BELOW CONTENT WITH FEATURES, PITCH, EXPANDABLE CALCULATOR)
# ─────────────────────────────────────────────────────────────────────────────
NEW_INVESTMENTS_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">Investment Products Suite</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">Select an investment product to view features, RM pitch scripts, and interactive return calculators.</p>

<!-- Small Product Selector Boxes Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; margin-bottom: 20px;" id="inv-product-selector-grid">

    <div class="inv-prod-box active" onclick="selectInvProduct('demat', this)" style="background: #ecfdf5; border: 2px solid #10b981; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">📊</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #065f46;">Demat & Equity</div>
        <div style="font-size: 0.72rem; color: #10b981; font-weight: 600;">Zero AMC</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('mf', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">📈</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">Mutual Funds</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">SIP & SWP</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('ipo', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">🚀</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">IPO (ASBA)</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">HNI Priority</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('mtf', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">⚡</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">MTF Leverage</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Rate @ 9.69%</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('aif', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">💎</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">AIF & PMS</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Bespoke Wealth</div>
    </div>

    <div class="inv-prod-box" onclick="selectInvProduct('lrs', this)" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; text-align: center; transition: all 0.2s; user-select: none;">
        <div style="font-size: 1.5rem; margin-bottom: 4px;">🌐</div>
        <div style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">Global LRS</div>
        <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Remittance</div>
    </div>

</div>

<!-- Dynamic Detail Container Below -->
<div id="inv-product-detail" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">

    <!-- Default: Demat -->
    <div id="inv-content-demat" class="inv-detail-pane" style="display: block;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>📊</span> Demat & Equity Trading Details
            </h3>
            <span style="background: #ecfdf5; color: #059669; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Zero AMC for Solitaire</span>
        </div>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Zero Annual Maintenance Charge (AMC)</strong> on Demat Account</li>
            <li>Delivery @ <strong>0.10%</strong> | Intraday & Futures @ <strong>0.01%</strong></li>
            <li>Options @ <strong>₹20/lot</strong> (with dealer) | <strong>₹10/lot</strong> (without dealer)</li>
            <li><strong>Dedicated Phone Dealer</strong> for instant voice trade execution</li>
        </ul>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Solitaire provides a zero-AMC Demat account combined with institutional brokerage rates—0.10% delivery and ₹20 options with a dedicated phone dealer for high-value orders.”
        </div>

        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 Brokerage & AMC Savings Calculator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹1 Crore annual turnover</strong> vs 0.30% standard brokerage:</p>
                <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #065f46;">Annual Brokerage & AMC Savings</span><br>
                    <strong style="font-size: 1.3rem; color: #059669;">~₹20,000 + ₹1,000 AMC = ₹21,000 / year</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- MF Content -->
    <div id="inv-content-mf" class="inv-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>📈</span> Mutual Funds & SIP / SWP Details
            </h3>
            <span style="background: #eff6ff; color: #2563eb; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Direct Plan Access</span>
        </div>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Access to top-rated mutual funds across Equity, Debt & Hybrid asset classes</li>
            <li>Automated <strong>SIP & SWP cash-flow tools</strong> for goal-based wealth planning</li>
            <li>Personalised portfolio health checkup & rebalancing recommendations</li>
        </ul>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Our ASPIRE tool lets you combine long-term SIP wealth accumulation with tax-efficient SWP monthly cash flows tailored to your family's financial goals.”
        </div>

        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 SIP Wealth Growth Calculator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹1,00,000/month SIP</strong> for 10 years @ 12% p.a.:</p>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #1e40af;">Projected Corpus (Investment ₹1.2 Cr)</span><br>
                    <strong style="font-size: 1.3rem; color: #1e3a8a;">~₹2.30 Crore</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- IPO Content -->
    <div id="inv-content-ipo" class="inv-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🚀</span> IPO & Primary Market (ASBA) Details
            </h3>
            <span style="background: #fff7ed; color: #c2410c; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Priority HNI Bidding</span>
        </div>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Priority ASBA bidding support for Mainboard & SME IPO applications</li>
            <li>HNI category bidding with instant fund block & unblock</li>
            <li>Research notes, valuation reports, and anchor investor insights</li>
        </ul>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #ea580c; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Apply for high-demand IPOs under the HNI category with priority ASBA blocking, so your funds stay in your account earning savings interest until allotment.”
        </div>

        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 HNI ASBA Savings Estimator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹10 Lakh HNI application</strong> blocked for 4 days:</p>
                <div style="background: #fff7ed; border: 1px solid #fed7aa; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #9a3412;">Savings Interest Earned During ASBA Block</span><br>
                    <strong style="font-size: 1.3rem; color: #c2410c;">~₹400 per IPO application</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- MTF Content -->
    <div id="inv-content-mtf" class="inv-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>⚡</span> Margin Trading Facility (MTF) Details
            </h3>
            <span style="background: #fef2f2; color: #b91c1c; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Rate @ 9.69% p.a.</span>
        </div>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Preferential MTF interest rates: <strong>9.69% p.a.</strong> (NTB) | <strong>9.75% p.a.</strong> (ETB)</li>
            <li>Leverage up to <strong>4x</strong> on 1,000+ approved stocks</li>
            <li>Hold positions backed by cash or pledged collateral shares</li>
        </ul>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #dc2626; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Capitalize on market opportunities with up to 4x funding on approved stocks at an industry-low 9.69% p.a. interest rate.”
        </div>

        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 MTF Buying Power & Interest Calculator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹10 Lakh Margin</strong> @ 4x Leverage = <strong>₹40 Lakh Buying Power</strong>:</p>
                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #991b1b;">Daily MTF Interest Outgo on ₹30L Borrowed</span><br>
                    <strong style="font-size: 1.3rem; color: #b91c1c;">~₹796 / day @ 9.69% p.a.</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- AIF Content -->
    <div id="inv-content-aif" class="inv-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>💎</span> Alternate Investments (AIF & PMS) Details
            </h3>
            <span style="background: #f3e8ff; color: #7e22ce; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">HNI Wealth Solutions</span>
        </div>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Curated referrals to <strong>Category I, II & III AIFs</strong> (Private Equity, VC, Hedge Funds)</li>
            <li>Custom Portfolio Management Services (PMS) with top fund managers</li>
            <li>High-yield structured debt & private placement opportunities</li>
        </ul>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #9333ea; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “For portfolio diversification beyond traditional markets, Solitaire offers exclusive access to curated AIFs and PMS strategies managed by leading fund houses.”
        </div>

        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 AIF Target IRR Projection (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>₹1 Crore allocation</strong> @ 18% target IRR over 5 years:</p>
                <div style="background: #f3e8ff; border: 1px solid #e9d5ff; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #6b21a8;">Projected Maturity Value</span><br>
                    <strong style="font-size: 1.3rem; color: #7e22ce;">~₹2.28 Crore</strong>
                </div>
            </div>
        </details>
    </div>

    <!-- LRS Content -->
    <div id="inv-content-lrs" class="inv-detail-pane" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🌐</span> Global Investments & LRS Details
            </h3>
            <span style="background: #e0f2fe; color: #0369a1; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Zero Remittance Fee</span>
        </div>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">📌 Key Features & Privileges</h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>LRS Overseas Investment facility up to <strong>USD 250,000</strong> annually</li>
            <li>Outward remittances up to <strong>USD 50,000</strong> with zero processing fee</li>
            <li>Preferential FX rates for overseas education, property, or foreign equities</li>
        </ul>

        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0;">🗣️ RM Pitch Script</h4>
        <div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 12px 16px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.9rem; line-height: 1.6; font-style: italic; margin-bottom: 20px;">
            “Planning overseas investments, university fees, or international property? Execute outward remittances up to USD 50,000 with zero processing fee and preferred FX rates.”
        </div>

        <details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                <span>🧮 FX Remittance Savings Calculator (Expandable)</span>
                <span style="font-size: 0.8rem; color: #64748b;">▼ Click to Calculate</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
                <p style="font-size: 0.88rem; color: #475569; margin-bottom: 10px;">For <strong>USD 50,000 remittance</strong> with zero processing fee & 25 paisa FX edge:</p>
                <div style="background: #e0f2fe; border: 1px solid #bae6fd; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.82rem; color: #075985;">Total Savings Per Remittance</span><br>
                    <strong style="font-size: 1.3rem; color: #0369a1;">~₹12,500 FX Edge + ₹1,500 Fee Waiver = ₹14,000</strong>
                </div>
            </div>
        </details>
    </div>

</div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# JS FUNCTIONS FOR INTERACTIVE PRODUCT BOX SELECTION
# ─────────────────────────────────────────────────────────────────────────────
JS_PRODUCT_BOX_SCRIPTS = """
// Loan Product Box Selection Logic
function selectLoanProduct(type, element) {
    document.querySelectorAll('#loan-product-selector-grid .loan-prod-box').forEach(el => {
        el.style.background = '#ffffff';
        el.style.border = '1.5px solid #e2e8f0';
        el.classList.remove('active');
        const textEl = el.querySelector('div:nth-child(2)');
        if (textEl) textEl.style.color = '#0f172a';
    });
    
    element.style.background = '#eff6ff';
    element.style.border = '2px solid #3b82f6';
    element.classList.add('active');
    const activeText = element.querySelector('div:nth-child(2)');
    if (activeText) activeText.style.color = '#1e3a8a';
    
    document.querySelectorAll('#loan-product-detail .loan-detail-pane').forEach(pane => {
        pane.style.display = 'none';
    });
    const selectedPane = document.getElementById('loan-content-' + type);
    if (selectedPane) selectedPane.style.display = 'block';
}

function calcHLSavings() {
    const amtEl = document.getElementById('hl-amt');
    const discEl = document.getElementById('hl-disc');
    const amtVal = document.getElementById('hl-amt-val');
    const savingsVal = document.getElementById('hl-savings-val');
    
    if (amtEl && discEl && amtVal && savingsVal) {
        const amt = parseFloat(amtEl.value);
        const disc = parseFloat(discEl.value);
        amtVal.innerText = `₹${amt.toFixed(1)} Crore`;
        const savings = Math.round(amt * 10000000 * (disc / 100));
        savingsVal.innerText = `₹${savings.toLocaleString('en-IN')} / year`;
    }
}

// Investment Product Box Selection Logic
function selectInvProduct(type, element) {
    document.querySelectorAll('#inv-product-selector-grid .inv-prod-box').forEach(el => {
        el.style.background = '#ffffff';
        el.style.border = '1.5px solid #e2e8f0';
        el.classList.remove('active');
        const textEl = el.querySelector('div:nth-child(2)');
        if (textEl) textEl.style.color = '#0f172a';
    });
    
    element.style.background = '#ecfdf5';
    element.style.border = '2px solid #10b981';
    element.classList.add('active');
    const activeText = element.querySelector('div:nth-child(2)');
    if (activeText) activeText.style.color = '#065f46';
    
    document.querySelectorAll('#inv-product-detail .inv-detail-pane').forEach(pane => {
        pane.style.display = 'none';
    });
    const selectedPane = document.getElementById('inv-content-' + type);
    if (selectedPane) selectedPane.style.display = 'block';
}
"""

def apply_updates():
    fname = "experience_solitaire_dashboard_new.html"
    c = get(fname)
    print(f"\n==================== Updating {fname} ====================")
    
    # 1. Update Loans Panel (panel-assets)
    p_assets_start = c.find('id="panel-assets"')
    if p_assets_start != -1:
        div_start = c.rfind('<div', 0, p_assets_start)
        p_inv_start = c.find('id="panel-investments"')
        div_inv_start = c.rfind('<div', 0, p_inv_start)
        
        new_loans_panel = f'<div class="info-panel" id="panel-assets">\n{NEW_LOANS_HTML}\n</div>\n'
        c = c[:div_start] + new_loans_panel + c[div_inv_start:]
        print("Updated panel-assets with small product boxes & dynamic detail container below!")

    # 2. Update Investments Panel (panel-investments)
    p_inv_start = c.find('id="panel-investments"')
    if p_inv_start != -1:
        div_start = c.rfind('<div', 0, p_inv_start)
        p_forex_start = c.find('id="panel-forex"')
        div_forex_start = c.rfind('<div', 0, p_forex_start)
        
        new_inv_panel = f'<div class="info-panel" id="panel-investments">\n{NEW_INVESTMENTS_HTML}\n</div>\n'
        c = c[:div_start] + new_inv_panel + c[div_forex_start:]
        print("Updated panel-investments with small product boxes & dynamic detail container below!")

    # 3. Inject JS functions before </body>
    if "function selectLoanProduct" not in c:
        pos_body_end = c.find('</body>')
        if pos_body_end != -1:
            c = c[:pos_body_end] + f'<script>\n{JS_PRODUCT_BOX_SCRIPTS}\n</script>\n' + c[pos_body_end:]
            print("Injected JS product box selection functions before </body>!")

    save(fname, c)
    print(f"Successfully saved {fname}!")

apply_updates()
