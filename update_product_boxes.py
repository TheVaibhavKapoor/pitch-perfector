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
# 1. NEW LOANS PANEL CONTENT (NO TABS, PRODUCT BOXES FOR HL, LAP, LAS, ETC.)
# ─────────────────────────────────────────────────────────────────────────────
NEW_LOANS_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">Bespoke Lending & Liquidity Solutions</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">Pre-approved limits, preferential interest rates, zero processing fees, and priority underwriting across all loan products.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 24px;">

    <!-- Product Box 1: Home Loan (HL) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#3b82f6';this.style.boxShadow='0 10px 15px -3px rgba(59,130,246,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #eff6ff; padding: 8px; border-radius: 10px;">🏠</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Home Loan (HL)</h3>
                    <span style="font-size: 0.78rem; color: #3b82f6; font-weight: 700;">Pre-Approved up to ₹7.5 Cr</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Preferential Rate Advantage:</strong> ~0.25% rate discount for Solitaire members</li>
            <li><strong>Zero Processing Fees</strong> & priority credit underwriting</li>
            <li>Balance Transfer with attractive top-up facilities</li>
            <li>Doorstep Relationship Manager assistance</li>
        </ul>
    </div>

    <!-- Product Box 2: Loan Against Property (LAP) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#3b82f6';this.style.boxShadow='0 10px 15px -3px rgba(59,130,246,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #f0fdf4; padding: 8px; border-radius: 10px;">🏢</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Loan Against Property (LAP)</h3>
                    <span style="font-size: 0.78rem; color: #16a34a; font-weight: 700;">High-Value Liquidity Pool</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>High quantum credit against residential or commercial property</li>
            <li>Flexible repayment tenures up to <strong>15 years</strong></li>
            <li>Special Solitaire commercial property rate structures</li>
            <li>Multi-property collateral pooling option</li>
        </ul>
    </div>

    <!-- Product Box 3: Loan Against Securities (LAS) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#3b82f6';this.style.boxShadow='0 10px 15px -3px rgba(59,130,246,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #fff7ed; padding: 8px; border-radius: 10px;">📈</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Loan Against Securities (LAS)</h3>
                    <span style="font-size: 0.78rem; color: #ea580c; font-weight: 700;">Instant Overdraft Line</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Instant OD line against Mutual Funds, Shares, Bonds & Insurance</li>
            <li><strong>Pay interest ONLY on utilized amount</strong></li>
            <li>Digital pledge / unpledge with zero foreclosure charges</li>
            <li>Retain ownership & dividend/growth benefits on pledged assets</li>
        </ul>
    </div>

    <!-- Product Box 4: Credit Line / Overdraft (Mid-Month Advance) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#3b82f6';this.style.boxShadow='0 10px 15px -3px rgba(59,130,246,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #f3e8ff; padding: 8px; border-radius: 10px;">💳</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Credit Line / Overdraft</h3>
                    <span style="font-size: 0.78rem; color: #9333ea; font-weight: 700;">Pre-Approved up to ₹25 Lakh</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Instant liquidity pool directly linked to primary Solitaire account</li>
            <li>Mid-Month Advance option for short-term working capital</li>
            <li>Solitaire preferential OD interest rates with zero annual fees</li>
        </ul>
    </div>

    <!-- Product Box 5: Auto Loan (Solitaire) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#3b82f6';this.style.boxShadow='0 10px 15px -3px rgba(59,130,246,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #fef2f2; padding: 8px; border-radius: 10px;">🚗</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Auto Loan (Solitaire)</h3>
                    <span style="font-size: 0.78rem; color: #dc2626; font-weight: 700;">Luxury Vehicle Funding</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Up to <strong>100% On-Road Funding</strong> for super-premium & luxury cars</li>
            <li>Bespoke step-up or balloon EMI repayment structures</li>
            <li>Nil foreclosure penalty post lock-in period</li>
        </ul>
    </div>

    <!-- Product Box 6: Personal Loan (Solitaire) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#3b82f6';this.style.boxShadow='0 10px 15px -3px rgba(59,130,246,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #ecfdf5; padding: 8px; border-radius: 10px;">💼</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Personal Loan</h3>
                    <span style="font-size: 0.78rem; color: #059669; font-weight: 700;">Pre-Approved Unsecured Credit</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Pre-approved unsecured loan up to <strong>₹25 Lakh</strong></li>
            <li>Instant 1-click disbursement with zero documentation</li>
            <li>Special fixed interest rates exclusive for Solitaire customers</li>
        </ul>
    </div>

</div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# 2. NEW INVESTMENTS PANEL CONTENT (NO TABS, PRODUCT BOXES FOR DEMAT, MF, IPO, ETC.)
# ─────────────────────────────────────────────────────────────────────────────
NEW_INVESTMENTS_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">Investment Products Suite</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">Institutional-grade investment products, zero AMC Demat, dedicated dealer support, and global wealth solutions.</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 24px;">

    <!-- Product Box 1: Demat & Equity Trading -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.boxShadow='0 10px 15px -3px rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #ecfdf5; padding: 8px; border-radius: 10px;">📊</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Demat & Equity Trading</h3>
                    <span style="font-size: 0.78rem; color: #059669; font-weight: 700;">Zero AMC Demat</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Zero Annual Maintenance Charge (AMC)</strong> on Demat Account</li>
            <li>Delivery @ <strong style="color: #059669;">0.10%</strong> | Intraday & Futures @ <strong style="color: #059669;">0.01%</strong></li>
            <li>Options @ <strong style="color: #059669;">₹20/lot</strong> (with dealer) | <strong style="color: #059669;">₹10/lot</strong> (without dealer)</li>
            <li><strong>Dedicated Dealer Phone Support</strong> included</li>
        </ul>
    </div>

    <!-- Product Box 2: Mutual Funds & SIP / SWP -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.boxShadow='0 10px 15px -3px rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #eff6ff; padding: 8px; border-radius: 10px;">📈</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Mutual Funds & SIP / SWP</h3>
                    <span style="font-size: 0.78rem; color: #2563eb; font-weight: 700;">Curated MF Solutions</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Access to top-rated mutual fund baskets across Equity, Debt & Hybrid</li>
            <li>Automated <strong>SIP & SWP cash-flow planning tools</strong></li>
            <li>Personalised portfolio health check & rebalancing advisory</li>
            <li>Zero subscription & platform transaction fees</li>
        </ul>
    </div>

    <!-- Product Box 3: IPO & Primary Market (ASBA) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.boxShadow='0 10px 15px -3px rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #fff7ed; padding: 8px; border-radius: 10px;">🚀</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">IPO & Primary Market (ASBA)</h3>
                    <span style="font-size: 0.78rem; color: #ea580c; font-weight: 700;">Priority HNI ASBA</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Priority ASBA bidding support for Mainboard & SME IPOs</li>
            <li>HNI category bidding with instant fund block/unblock</li>
            <li>Research reports, valuation notes & anchor allocation insights</li>
        </ul>
    </div>

    <!-- Product Box 4: Margin Trading Facility (MTF) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.boxShadow='0 10px 15px -3px rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #fef2f2; padding: 8px; border-radius: 10px;">⚡</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Margin Trading Facility (MTF)</h3>
                    <span style="font-size: 0.78rem; color: #dc2626; font-weight: 700;">Rate @ 9.69% p.a.</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Preferential MTF rates: <strong style="color: #059669;">9.69% p.a.</strong> (NTB) | <strong style="color: #059669;">9.75% p.a.</strong> (ETB)</li>
            <li>Leverage up to <strong>4x</strong> on 1,000+ approved stocks</li>
            <li>Hold positions against cash margin or pledged stocks</li>
        </ul>
    </div>

    <!-- Product Box 5: Alternate Investments (AIF & PMS) -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.boxShadow='0 10px 15px -3px rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #f3e8ff; padding: 8px; border-radius: 10px;">💎</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Alternate Investments (AIF & PMS)</h3>
                    <span style="font-size: 0.78rem; color: #9333ea; font-weight: 700;">HNI Wealth Strategies</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>Curated referrals to <strong>Category I, II & III AIFs</strong> (Private Equity, VC, Hedge Funds)</li>
            <li>Bespoke Portfolio Management Services (PMS) with institutional managers</li>
            <li>Structured debt & high-yield private placement deals</li>
        </ul>
    </div>

    <!-- Product Box 6: Global Investments & Remittances -->
    <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 22px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.boxShadow='0 10px 15px -3px rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='#e2e8f0';this.style.boxShadow='0 4px 6px -1px rgba(0,0,0,0.03)'">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.5rem; background: #e0f2fe; padding: 8px; border-radius: 10px;">🌐</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: #0f172a;">Global Investments & LRS</h3>
                    <span style="font-size: 0.78rem; color: #0284c7; font-weight: 700;">Overseas Remittance</span>
                </div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li>LRS Overseas Investment facility up to <strong>USD 2,50,000</strong> annually</li>
            <li>Outward remittances up to <strong>USD 50,000</strong> through dedicated desk</li>
            <li>Preferential FX rates for overseas education, property, or foreign equities</li>
        </ul>
    </div>

</div>
"""

def update_file(fname):
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
        print("Updated panel-assets with product boxes (No tabs)!")

    # 2. Update Investments Panel (panel-investments)
    p_inv_start = c.find('id="panel-investments"')
    if p_inv_start != -1:
        div_start = c.rfind('<div', 0, p_inv_start)
        p_forex_start = c.find('id="panel-forex"')
        div_forex_start = c.rfind('<div', 0, p_forex_start)
        
        new_inv_panel = f'<div class="info-panel" id="panel-investments">\n{NEW_INVESTMENTS_HTML}\n</div>\n'
        c = c[:div_start] + new_inv_panel + c[div_forex_start:]
        print("Updated panel-investments with product boxes (No tabs)!")

    save(fname, c)
    print(f"Successfully saved {fname}!")

update_file("experience_solitaire_dashboard_new.html")
