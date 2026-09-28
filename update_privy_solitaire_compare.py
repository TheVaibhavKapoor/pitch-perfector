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
# NEW INLINE PROGRAM COMPARISON PANEL (PRIVY vs PRIVY+ vs SOLITAIRE)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PANEL_COMPARE_PRIVY_HTML = """<div class="info-panel" id="panel-compare">
    <h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 4px;">Program Comparison</h2>
    <p style="color: #64748b; line-height: 1.6; margin-bottom: 20px; font-size: 0.92rem;">Compare Privy, Privy+ and Solitaire across eligibility, products and rewards.</p>

    <!-- Header Row Table Style -->
    <div style="background: #e9ecef; border-radius: 10px 10px 0 0; padding: 12px 20px; font-weight: 800; font-size: 0.82rem; color: #334155; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; letter-spacing: 0.05em; text-transform: uppercase;">
        <div>BENEFIT / FEATURE</div>
        <div>PRIVY</div>
        <div>PRIVY+</div>
        <div style="color: #1e3a8a;">SOLITAIRE</div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">

        <!-- 1. Eligibility Accordion -->
        <details open style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 0 0 10px 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 20px; font-weight: 800; color: #0f172a; font-size: 0.95rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span>Eligibility</span>
                <span style="font-size: 0.75rem; color: #64748b;">▲</span>
            </summary>
            <div style="padding: 0 20px 14px 20px;">
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Relationship Value</div>
                    <div style="color: #64748b;">₹10L</div>
                    <div style="color: #64748b;">₹30L</div>
                    <div style="color: #1e3a8a; font-weight: 800;">₹75L+</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Salary Route</div>
                    <div style="color: #64748b;">₹1L+/month</div>
                    <div style="color: #64748b;">₹3L+/month</div>
                    <div style="color: #1e3a8a; font-weight: 800;">₹5L+/month</div>
                </div>
            </div>
        </details>

        <!-- 2. Accounts & Convenience Accordion -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 20px; font-weight: 800; color: #0f172a; font-size: 0.95rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span>Accounts & Convenience</span>
                <span style="font-size: 0.75rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 0 20px 14px 20px;">
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Relationship Support</div>
                    <div style="color: #64748b;">Priority Service</div>
                    <div style="color: #64748b;">Dedicated RM</div>
                    <div style="color: #1e3a8a; font-weight: 800;">Dedicated Private RM + Family Banking</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Debit Card</div>
                    <div style="color: #64748b;">Privy Platinum</div>
                    <div style="color: #64748b;">Privy Signature</div>
                    <div style="color: #1e3a8a; font-weight: 800;">Solitaire Metal / Visa Infinite</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">ActivMoney Returns</div>
                    <div style="color: #64748b;">Auto-sweep FD</div>
                    <div style="color: #64748b;">Auto-sweep FD</div>
                    <div style="color: #1e3a8a; font-weight: 800;">Auto-sweep + Preferential Rates</div>
                </div>
            </div>
        </details>

        <!-- 3. Credit Cards Accordion -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 20px; font-weight: 800; color: #0f172a; font-size: 0.95rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span>Credit Cards</span>
                <span style="font-size: 0.75rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 0 20px 14px 20px;">
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Card Variant</div>
                    <div style="color: #64748b;">Select Credit Card</div>
                    <div style="color: #64748b;">Privy League Metal</div>
                    <div style="color: #1e3a8a; font-weight: 800;">Kotak Solitaire Metal Card</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Reward Rate / Air Miles</div>
                    <div style="color: #64748b;">Standard Rewards</div>
                    <div style="color: #64748b;">2x Reward Points</div>
                    <div style="color: #1e3a8a; font-weight: 800;">10 Air Miles / ₹100 via Unbox</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Forex Markup</div>
                    <div style="color: #64748b;">3.5% Markup</div>
                    <div style="color: #64748b;">2.0% Markup</div>
                    <div style="color: #1e3a8a; font-weight: 800;">0% Forex Markup</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Lounge Access</div>
                    <div style="color: #64748b;">4 visits / year</div>
                    <div style="color: #64748b;">8 visits / year</div>
                    <div style="color: #1e3a8a; font-weight: 800;">UNLIMITED Domestic & Intl + Guest</div>
                </div>
            </div>
        </details>

        <!-- 4. Loans & Credit Accordion -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 20px; font-weight: 800; color: #0f172a; font-size: 0.95rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span>Loans & Credit</span>
                <span style="font-size: 0.75rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 0 20px 14px 20px;">
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Home Loan Discount</div>
                    <div style="color: #64748b;">Standard Rates</div>
                    <div style="color: #64748b;">0.10% Discount</div>
                    <div style="color: #1e3a8a; font-weight: 800;">~0.25% Discount + Zero Fees</div>
                </div>
                <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 0; font-size: 0.88rem; align-items: center;">
                    <div style="color: #334155; font-weight: 600;">Pre-Approved Credit</div>
                    <div style="color: #64748b;">₹5 Lakh</div>
                    <div style="color: #64748b;">₹10 Lakh</div>
                    <div style="color: #1e3a8a; font-weight: 800;">₹25L Overdraft Line + ₹7.5Cr HL</div>
                </div>
            </div>
        </details>

    </div>
</div>"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Updating panel-compare in {fname} ====================")

# 1. Ensure top right header Compare Program button is completely removed
c = re.sub(r'<button[^>]*onclick="openCompareModal\(\)"[^>]*>Compare Program</button>\s*', '', c)
c = re.sub(r'<button[^>]*>Compare Program</button>\s*', '', c)

# 2. Replace panel-compare with new Privy vs Privy+ vs Solitaire table
p_compare_start = c.find('id="panel-compare"')
if p_compare_start != -1:
    div_start = c.rfind('<div', 0, p_compare_start)
    next_panel = c.find('<div class="info-panel"', p_compare_start)
    if next_panel == -1: next_panel = c.find('</div>\n\n</div>', p_compare_start)
    
    c = c[:div_start] + NEW_PANEL_COMPARE_PRIVY_HTML + "\n\n" + c[next_panel:]
    print("Replaced panel-compare with Privy vs Privy+ vs Solitaire program comparison table!")

save(fname, c)
print("Successfully saved updated experience_solitaire_dashboard_new.html!")
