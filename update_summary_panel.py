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
# NEW PANEL SUMMARY HTML
# ─────────────────────────────────────────────────────────────────────────────
NEW_SUMMARY_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 8px;">Solitaire Relationship Value Summary</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">Illustrative annual economic value created through realistic utilization of the Solitaire ecosystem for an affluent customer.</p>

<!-- Hero Value Banner -->
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #172554 100%); color: white; border-radius: 16px; padding: 28px; margin-bottom: 24px; box-shadow: 0 12px 30px -5px rgba(30,58,138,0.35); border: 1px solid rgba(255,255,255,0.1);">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 18px;">
        <div>
            <span style="font-size: 0.82rem; font-weight: 700; color: #93c5fd; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 6px;">Your Solitaire Value Proposition</span>
            <h3 style="margin: 0; font-size: 2.2rem; font-weight: 900; color: #ffffff; letter-spacing: -0.02em;">₹2.0L – ₹3.0L+ <span style="font-size: 1.1rem; font-weight: 600; color: #cbd5e1;">/ year</span></h3>
            <p style="margin: 6px 0 0 0; color: #cbd5e1; font-size: 0.92rem;">Illustrative annual potential value based on active ecosystem utilisation</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 10px 16px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.15); text-align: right;">
            <span style="font-size: 0.78rem; color: #94a3b8; display: block;">Target Profile</span>
            <strong style="color: #fbbf24; font-size: 1rem;">₹1 Cr Net-Worth Customer</strong>
        </div>
    </div>

    <!-- RM Killer Line Callout -->
    <div style="background: rgba(255,255,255,0.08); border-left: 4px solid #fbbf24; padding: 14px 18px; border-radius: 0 8px 8px 0; font-size: 0.92rem; color: #f8fafc; line-height: 1.6; font-style: italic;">
        🗣️ <strong>The Killer RM Line:</strong> “For a ₹1 Cr customer who actually uses the Solitaire ecosystem—travel, dining, card spends, investments and lending—the relationship can potentially create ₹2–3L+ of annual economic value. The exact number depends on your spending and financial profile, so I can calculate it for you.”
    </div>
</div>

<!-- Customer Profile Assumptions Box -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px 20px; margin-bottom: 24px;">
    <h4 style="margin: 0 0 12px 0; font-size: 0.95rem; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
        <span>👤</span> Assumed Customer Profile (Affluent ₹1 Cr Net-Worth)
    </h4>
    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">Net Worth: ₹1 Cr</span>
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">Card Spends: ₹15–20L/yr</span>
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">Travel: ₹5–8L/yr</span>
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">Intl Spends: ₹3–5L/yr</span>
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">Trips: 2–4 times/yr</span>
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">Regular Investor</span>
        <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;">1–2 Add-on Cards</span>
    </div>
</div>

<!-- Master Potential Value Table -->
<h3 style="font-size: 1.1rem; font-weight: 700; color: #0f172a; margin-bottom: 14px;">Annual Potential Value Breakdown</h3>

<div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); margin-bottom: 24px;">
    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;">
        <thead style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;">
            <tr>
                <th style="padding: 14px 18px; font-weight: 700; color: #475569;">Solitaire Component</th>
                <th style="padding: 14px 18px; font-weight: 700; color: #475569;">Key Details & Usage</th>
                <th style="padding: 14px 18px; font-weight: 700; color: #0f172a; text-align: right;">Potential Annual Value</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #ffffff;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>💳</span> Credit Card (Illustrative)
                </td>
                <td style="padding: 14px 18px; color: #475569;">Kotak official illustrative chart on ₹20L annual spends</td>
                <td style="padding: 14px 18px; font-weight: 800; color: #1e3a8a; text-align: right;">₹2,06,750*</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #f8fafc;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>🍽️</span> District / Lifestyle Table
                </td>
                <td style="padding: 14px 18px; color: #475569;">20% off × ₹5,000 × 2 transactions/month (max ₹10k/mo)</td>
                <td style="padding: 14px 18px; font-weight: 800; color: #10b981; text-align: right;">₹1,20,000*</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #ffffff;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>💳</span> Debit Card Zomato
                </td>
                <td style="padding: 14px 18px; color: #475569;">20% off Zomato up to ₹1,500/month</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; text-align: right;">₹18,000</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #f8fafc;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>✈️</span> Air Miles Rewards
                </td>
                <td style="padding: 14px 18px; color: #475569;">10 Air Miles/₹100 on Unbox travel | 3 Air Miles base (1 Mile = ₹1)</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; text-align: right;">₹20,000 – ₹50,000</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #ffffff;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: gap: 8px;">
                    <span>🌐</span> Forex Savings
                </td>
                <td style="padding: 14px 18px; color: #475569;">0% markup vs standard 3.5% (e.g. ₹4L intl spends = ₹14,000 saved)</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; text-align: right;">₹10,000 – ₹20,000</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #f8fafc;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>🛋️</span> Lounge Access
                </td>
                <td style="padding: 14px 18px; color: #475569;">Unlimited domestic & intl lounge visits for primary & add-on cardholders</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; text-align: right;">₹30,000 – ₹50,000</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #ffffff;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>🏨</span> Luxury Stay Privileges
                </td>
                <td style="padding: 14px 18px; color: #475569;">3rd night free / 50% off 2nd night at ITC, Elivaas, Alaya; ₹5k off Postcard</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; text-align: right;">₹30,000+</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #f8fafc;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>🏠</span> Lending Advantage
                </td>
                <td style="padding: 14px 18px; color: #475569;">0.25% rate edge on Home Loan up to ₹7.5Cr / Credit Line up to ₹25L</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #3b82f6; text-align: right;">Calculate Dynamically</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9; background: #ffffff;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>📈</span> Wealth & Investments
                </td>
                <td style="padding: 14px 18px; color: #475569;">Zero AMC Demat, 0.10% delivery, 0.01% intraday, ASBA priority, AIF/PMS access</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #3b82f6; text-align: right;">Personalised Opportunity</td>
            </tr>
            <tr style="background: #f8fafc;">
                <td style="padding: 14px 18px; font-weight: 700; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                    <span>🛡️</span> Concierge & Insurance
                </td>
                <td style="padding: 14px 18px; color: #475569;">24/7 Concierge desk + ₹5 Cr Air Accident Cover + ₹1.5L Purchase Protection</td>
                <td style="padding: 14px 18px; font-weight: 700; color: #64748b; text-align: right;">Protection Value</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Kotak Official Credit Card Value Chart Accordion -->
<details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03); margin-bottom: 24px;">
    <summary style="padding: 16px 20px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
        <span style="display: flex; align-items: center; gap: 10px;">
            <span>📋</span> Official Kotak Solitaire Credit Card Value Chart (₹2,06,750 / Year)
        </span>
        <span style="font-size: 0.8rem; color: #64748b;">▼</span>
    </summary>
    <div style="padding: 16px 20px; border-top: 1px solid #f1f5f9;">
        <p style="color: #64748b; font-size: 0.85rem; margin-bottom: 14px;">Kotak Mahindra Bank's official published illustrative value chart for Solitaire Credit Card on ₹20L annual spends:</p>
        <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
                <tr>
                    <th style="padding: 8px 12px; font-weight: 600; color: #475569;">Benefit Component</th>
                    <th style="padding: 8px 12px; font-weight: 600; color: #0f172a; text-align: right;">Illustrative Annual Value</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Domestic hotel savings</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹10,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Domestic flight savings</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹10,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">International hotel savings</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹20,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">International flight savings</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹40,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Foreign-spend savings</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹14,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Fuel surcharge benefit</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹750</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Other-spend rewards</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹15,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Domestic lounge value</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹30,600</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">International lounge value</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹27,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Guest lounge value</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹9,400</td>
                </tr>
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 8px 12px; color: #334155;">Luxury-stay benefit</td>
                    <td style="padding: 8px 12px; text-align: right; font-weight: 600;">₹30,000</td>
                </tr>
                <tr style="background: #f8fafc; font-weight: 800;">
                    <td style="padding: 10px 12px; color: #0f172a;">Total Illustrative Card Value</td>
                    <td style="padding: 10px 12px; text-align: right; color: #1e3a8a; font-size: 0.98rem;">₹2,06,750</td>
                </tr>
            </tbody>
        </table>
    </div>
</details>

<!-- Compliance Footnote -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 16px; color: #64748b; font-size: 0.78rem; line-height: 1.5;">
    * <strong>Disclaimer:</strong> Values shown are illustrative maximum/potential values based on Kotak Mahindra Bank published charts and maximum offer terms. Actual economic value realized depends on customer's individual utilization, eligible spends, specific offers, and applicable program T&Cs. Benefits should not be represented to clients as guaranteed cash returns.
</div>
"""

c = get("experience_solitaire_dashboard_new.html")
p_summary_start = c.find('id="panel-summary"')
if p_summary_start != -1:
    div_start = c.rfind('<div', 0, p_summary_start)
    p_cc_start = c.find('id="panel-cc"')
    div_cc_start = c.rfind('<div', 0, p_cc_start)
    
    new_summary_panel = f'<div class="info-panel" id="panel-summary">\n{NEW_SUMMARY_HTML}\n</div>\n'
    c = c[:div_start] + new_summary_panel + c[div_cc_start:]
    save("experience_solitaire_dashboard_new.html", c)
    print("Updated panel-summary in experience_solitaire_dashboard_new.html successfully!")
