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
# NEW INLINE COMPARE PANEL HTML (#panel-compare) WITH 7 EXPANDABLE CATEGORIES
# ─────────────────────────────────────────────────────────────────────────────
NEW_PANEL_COMPARE_HTML = """<div class="info-panel" id="panel-compare">
    <h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">Solitaire Competitive Edge & Program Comparison</h2>
    <p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">Benchmark Kotak Solitaire against premier banking propositions (HDFC Imperial/Infinia, ICICI Emerelde, Axis Burgundy, Amex Platinum).</p>

    <!-- Expandable Category 1: Premium Banking & Relationship Support -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">🏦</span> 1. Premium Banking & Relationship Support
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Relationship Model</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">Dedicated Private RM + Family Pooling (Salaried ₹75L+ / Self-Employed ₹1Cr+)</td>
                        <td style="padding: 10px; color: #475569;">Individual strict NRV thresholds (₹1.5Cr-₹2Cr+) without family aggregation</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Idle Balance Yield</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">ActivMoney auto-sweep — FD-like returns on idle balances while keeping 100% liquidity</td>
                        <td style="padding: 10px; color: #475569;">Standard savings interest (3.0%-3.5%) unless manually locked in FDs</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>

    <!-- Expandable Category 2: Credit Card Rewards & Air Miles -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">💳</span> 2. Credit Card Rewards & Air Miles Structuring
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Travel Reward Rate</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">10 Air Miles / ₹100 via Kotak Unbox (1 Air Mile = ₹1 value)</td>
                        <td style="padding: 10px; color: #475569;">3.3% to 5% reward rate with conversion capping & devaluation risks</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Forex Markup Rate</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">0% Forex Markup on primary international spends (Saves ~₹14k on ₹4L intl spend)</td>
                        <td style="padding: 10px; color: #475569;">Standard 2.0% - 3.5% foreign currency transaction markup fee</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>

    <!-- Expandable Category 3: Dining & Lifestyle Privileges -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">🍽️</span> 3. Dining & Lifestyle Privileges
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Solitaire Table / District</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">20% off × ₹5,000 × 2 txns/month (Potential ₹1.20 Lakh annual savings)</td>
                        <td style="padding: 10px; color: #475569;">Capped at ₹1,000 - ₹1,500/month with venue restrictions</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Debit Card Dining</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">20% off Zomato up to ₹1,500/month (₹18,000 annual savings)</td>
                        <td style="padding: 10px; color: #475569;">Nil dining benefits on debit cards</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>

    <!-- Expandable Category 4: Airport Lounge Access & Travel Privileges -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">✈️</span> 4. Airport Lounge Access & Travel Privileges
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Lounge Access Policy</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">UNLIMITED domestic & international lounge access for Primary AND Add-on cards</td>
                        <td style="padding: 10px; color: #475569;">Capped at 4-8 visits per quarter, spend-linked unlock criteria</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Guest Access</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">Included complimentary guest lounge visits (Kotak value: ₹9,400)</td>
                        <td style="padding: 10px; color: #475569;">Guest access charged at full rack rate ($32-$35 per guest)</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>

    <!-- Expandable Category 5: Luxury Hotel & Stay Benefits -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">🏨</span> 5. Luxury Hotel & Stay Benefits
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Luxury Hotel Offers</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">3rd night free / 50% off 2nd night at ITC, Elivaas, Alaya; ₹5k off Postcard Hotels</td>
                        <td style="padding: 10px; color: #475569;">Standard portal booking discounts (10%-15%) without complimentary night stays</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>

    <!-- Expandable Category 6: Lending Rates & Asset-Backed Liquidity -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">🏠</span> 6. Lending Rates & Processing Advantages
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Home Loan Rate Edge</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">Pre-approved up to ₹7.5 Cr with ~0.25% rate discount & ZERO processing fee</td>
                        <td style="padding: 10px; color: #475569;">Standard rack rates with 0.50% processing fees & login charges</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Credit Line Overdraft</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">Pre-approved ₹25 Lakh OD credit line linked to primary account</td>
                        <td style="padding: 10px; color: #475569;">Fresh documentation and underwriting required for OD lines</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>

    <!-- Expandable Category 7: Wealth Management & Demat Pricing -->
    <details style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">📈</span> 7. Wealth Management & Demat Pricing
            </span>
            <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand</span>
        </summary>
        <div style="padding: 18px 20px; border-top: 1px solid #f1f5f9;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead style="background: #f8fafc; border-bottom: 1px solid #cbd5e1;">
                    <tr>
                        <th style="padding: 10px; color: #475569; width: 25%;">Feature</th>
                        <th style="padding: 10px; color: #1e3a8a; background: #eff6ff; width: 38%;">Kotak Solitaire Edge</th>
                        <th style="padding: 10px; color: #475569; width: 37%;">Competitor Benchmarks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Demat & Brokerage Rates</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">ZERO AMC Demat | 0.10% Delivery | 0.01% Intraday | Options @ ₹20/lot with phone dealer</td>
                        <td style="padding: 10px; color: #475569;">Standard 0.25%-0.50% delivery rates + ₹500-₹1,000 annual AMC charges</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                        <td style="padding: 10px; font-weight: 600;">Margin Trading (MTF)</td>
                        <td style="padding: 10px; background: #f0f9ff; color: #1e40af; font-weight: 700;">Preferential MTF rate @ 9.69% p.a. (NTB) / 9.75% p.a. (ETB) with 4x leverage</td>
                        <td style="padding: 10px; color: #475569;">MTF interest rates ranging between 12.0% - 18.0% p.a.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </details>
</div>
"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Updating Compare Program Feature in {fname} ====================")

# 1. Remove Compare Program button from top right header menu
c = re.sub(r'<button[^>]*onclick="openCompareModal\(\)"[^>]*>Compare Program</button>\s*', '', c)
print("Removed Compare Program button from top right menu!")

# 2. Update 7th card in products-grid to call showPanel('compare', this)
c = c.replace('onclick="openCompareModal()"', 'onclick="showPanel(\'compare\', this)"')
print("Updated 7th card onclick to showPanel('compare', this)!")

# 3. Add #panel-compare info-panel before </body> or inside #info-panels
if 'id="panel-compare"' not in c:
    pos_summary = c.find('id="panel-summary"')
    if pos_summary != -1:
        div_summary_end = c.find('</div>', c.find('</div>', pos_summary) + 10)
        # Find closing div of panel-summary
        p_cc_start = c.find('id="panel-cc"')
        div_cc_start = c.rfind('<div', 0, p_cc_start)
        
        c = c[:div_cc_start] + NEW_PANEL_COMPARE_HTML + "\n\n" + c[div_cc_start:]
        print("Injected #panel-compare with 7 expandable categories!")

save(fname, c)
print("Successfully saved updated experience_solitaire_dashboard_new.html!")
