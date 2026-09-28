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
# 1. NEW PROGRAM INTRO CONTENT FOR panel-intro
# ─────────────────────────────────────────────────────────────────────────────
NEW_INTRO_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 16px;">Introduction to RM and Program</h2>

<!-- RM Greeting Pitch -->
<div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 18px 20px; margin-bottom: 24px; border-radius: 0 10px 10px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
    <p style="color: #1e3a8a; margin-bottom: 10px; font-weight: 700; font-size: 1rem;">Good morning, Sir/Ma’am. I’m Vaibhav Kapoor, your dedicated Relationship Manager at Kotak Mahindra Bank.</p>
    <p style="color: #475569; margin-bottom: 8px; font-size: 0.93rem; line-height: 1.6;">I’ll be your single point of contact for all your banking and wealth requirements going forward.</p>
    <p style="color: #475569; margin-bottom: 8px; font-size: 0.93rem; line-height: 1.6;">My role is not just to assist you whenever you need something, but to understand your overall financial requirements and proactively help you with the right solutions—whether it’s investments, lending, insurance, cards, or any other banking requirement.</p>
    <p style="color: #475569; margin-bottom: 8px; font-size: 0.93rem; line-height: 1.6;">I’d also like to understand how you currently use your Kotak relationship, what’s working well for you, and where you feel there is scope for improvement.</p>
    <p style="color: #475569; margin-bottom: 0; font-size: 0.93rem; line-height: 1.6;">My objective is very simple—to make your banking relationship with Kotak more seamless, personalised and valuable.</p>
</div>

<!-- Program Introduction (Always Visible Card) -->
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color: white; padding: 24px; border-radius: 14px; margin-bottom: 24px; box-shadow: 0 10px 25px -5px rgba(30,58,138,0.3);">
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
        <span style="font-size: 1.4rem;">💎</span>
        <h3 style="margin: 0; font-size: 1.2rem; font-weight: 800; color: #ffffff;">Kotak Solitaire Program Introduction</h3>
    </div>
    <p style="font-size: 0.95rem; line-height: 1.65; color: #e2e8f0; margin-bottom: 16px;">
        Kotak Solitaire is Kotak Mahindra Bank’s invite-only premium/private banking proposition designed for affluent and HNI customers and their families. It combines wealth management, premium banking, exclusive credit cards, preferential lending and lifestyle privileges with dedicated relationship support.
    </p>
    <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.15); padding: 14px 18px; border-radius: 10px; font-size: 0.88rem; color: #f8fafc; line-height: 1.55;">
        <strong style="color: #fbbf24;">Eligibility:</strong> Generally, salaried customers require <strong>₹75 lakh+ Relationship Value (RV)</strong>, while self-employed customers require <strong>₹1 crore+ RV</strong> across family relationships.
    </div>
</div>

<!-- Key Features Expandable Categories Accordion -->
<h3 style="font-size: 1.1rem; font-weight: 700; color: #0f172a; margin-bottom: 14px;">Program Features & Privileges</h3>

<div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">

    <!-- Category 1: Premium Banking -->
    <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.1rem;">🏦</span> Premium Banking
            </span>
            <span style="font-size: 0.8rem; color: #64748b;">▼</span>
        </summary>
        <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9; background: #ffffff;">
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>Dedicated Relationship Manager</strong> as single point of contact</li>
                <li><strong>Priority & personalised banking service</strong> across all touchpoints</li>
                <li><strong>Family relationship banking</strong> (extend privileges to family members)</li>
                <li><strong>Preferential rates</strong> on select banking products and services</li>
                <li><strong>ActivMoney</strong> — FD-like higher returns on idle savings account balance</li>
            </ul>
        </div>
    </details>

    <!-- Category 2: Solitaire Credit Card -->
    <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.1rem;">💳</span> Solitaire Credit Card
            </span>
            <span style="font-size: 0.8rem; color: #64748b;">▼</span>
        </summary>
        <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9; background: #ffffff;">
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>Invite-only premium metal credit card</strong></li>
                <li><strong>10 Air Miles per ₹100</strong> on eligible flight & hotel bookings through Kotak Unbox</li>
                <li><strong>3 Air Miles per ₹100</strong> on other eligible spends</li>
                <li><strong>0% forex markup</strong> on international spends worldwide</li>
                <li><strong>Complimentary airport lounge access</strong> for primary cardholder and family</li>
                <li><strong>1% low cash withdrawal charge</strong> at ATMs worldwide</li>
                <li><strong>Annual fee waived</strong> for Solitaire customers while eligibility is maintained</li>
            </ul>
        </div>
    </details>

    <!-- Category 3: Lending & Liquidity -->
    <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.1rem;">💰</span> Lending & Liquidity
            </span>
            <span style="font-size: 0.8rem; color: #64748b;">▼</span>
        </summary>
        <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9; background: #ffffff;">
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>Pre-approved home loan</strong> up to ₹7.5 crore</li>
                <li><strong>Pre-approved credit line</strong> up to ₹25 lakh (Mid-Month Advance / Overdraft)</li>
                <li><strong>Quick loan solutions</strong> with minimal documentation</li>
                <li><strong>Preferential lending propositions</strong> & competitive interest rates</li>
            </ul>
        </div>
    </details>

    <!-- Category 4: Wealth Management -->
    <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.1rem;">📈</span> Wealth Management
            </span>
            <span style="font-size: 0.8rem; color: #64748b;">▼</span>
        </summary>
        <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9; background: #ffffff;">
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>Personalised investment solutions</strong> tailored to risk profile & goals</li>
                <li><strong>Access & referrals to alternate investments</strong> including AIFs (Cat I, II, III) & PMS</li>
                <li><strong>Mutual funds, equities, bonds & structured solutions</strong></li>
                <li><strong>Global investment & remittance opportunities</strong></li>
                <li><strong>Overseas investment facility</strong> up to USD 2,50,000 annually under LRS</li>
                <li><strong>Outward remittances</strong> up to USD 50,000 through stated facility</li>
            </ul>
        </div>
    </details>

    <!-- Category 5: Lifestyle -->
    <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
            <span style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.1rem;">✈️</span> Lifestyle Privileges
            </span>
            <span style="font-size: 0.8rem; color: #64748b;">▼</span>
        </summary>
        <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9; background: #ffffff;">
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>Premium travel benefits</strong> (airport assistance, lounge access, luxury transfers)</li>
                <li><strong>Hotel & flight privileges</strong> (complimentary night stays & discounted rates)</li>
                <li><strong>Exclusive events & experiences</strong> (chef's tables, fine dining, cultural pre-sales)</li>
                <li><strong>Concierge-style relationship support</strong> 24/7</li>
            </ul>
        </div>
    </details>

</div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# 2. NEW INVESTMENTS PANEL CONTENT FOR panel-investments
# ─────────────────────────────────────────────────────────────────────────────
NEW_INVESTMENTS_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">Investment Suite</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">Access institutional-grade investment strategies, zero subscription fees, and dedicated dealer support.</p>

<div class="inner-tabs-container" style="display: flex; gap: 8px; margin-bottom: 24px; background: #f1f5f9; padding: 6px; border-radius: 12px;">
    <button class="inner-tab-btn active" onclick="switchInnerTab(this, 'features')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #0f172a; background: white; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;">Features</button>
    <button class="inner-tab-btn" onclick="switchInnerTab(this, 'pitches')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;">Pitches</button>
    <button class="inner-tab-btn" onclick="switchInnerTab(this, 'calculator')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;">Calculator</button>
</div>

<!-- FEATURES TAB -->
<div class="inner-tab-content inner-tab-content-features" style="display: block;">
    <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">

        <!-- Demat & Trading -->
        <details open style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">📊</span> Demat & Equity Trading
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li><strong style="color: #10b981;">Zero AMC</strong> on Demat Account for Solitaire members</li>
                    <li>Competitive pricing <strong>without subscription fees</strong></li>
                    <li>Delivery @ <strong style="color: #10b981;">0.10%</strong> | Intraday & Futures @ <strong style="color: #10b981;">0.01%</strong></li>
                    <li>Options @ <strong style="color: #10b981;">₹20/lot</strong> (with dealer) | <strong style="color: #10b981;">₹10/lot</strong> (without dealer)</li>
                    <li><strong>Dedicated Dealer Support</strong> included</li>
                </ul>
            </div>
        </details>

        <!-- Mutual Funds & SIP -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">📈</span> Mutual Funds & SIP Solutions
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Access to top-performing mutual funds across equity, debt & hybrid asset classes</li>
                    <li>Automated <strong>SIP & SWP tools</strong> for systematic wealth creation & cash flow planning</li>
                    <li>Comprehensive portfolio review and rebalancing guidance</li>
                </ul>
            </div>
        </details>

        <!-- IPO & Primary Market -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">🚀</span> IPO & Primary Market (ASBA)
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Priority ASBA bidding support for Mainboard & SME IPOs</li>
                    <li>HNI category bidding with instant fund block/unblock</li>
                    <li>Research insights on upcoming public issues & anchor allocations</li>
                </ul>
            </div>
        </details>

        <!-- Margin Trading Facility (MTF) -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">⚡</span> Margin Trading Facility (MTF)
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Preferential interest rates: <strong style="color: #10b981;">9.69% p.a.</strong> (NTB) | <strong style="color: #10b981;">9.75% p.a.</strong> (ETB)</li>
                    <li>Leverage up to <strong>4x</strong> on 1,000+ approved stocks</li>
                    <li>Hold margin positions seamlessly with cash or stock collateral</li>
                </ul>
            </div>
        </details>

        <!-- Alternate Investments (AIF / PMS) -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">💎</span> Alternate Investments (AIF & PMS)
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Curated referrals & access to <strong>Category I, II, III AIFs</strong> (Private Equity, Venture Capital, Hedge Funds)</li>
                    <li>Bespoke Portfolio Management Services (PMS) with professional fund managers</li>
                    <li>Structured products & high-yield private debt opportunities</li>
                </ul>
            </div>
        </details>

        <!-- Global Investments & Remittances -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">🌐</span> Global Investments & Outward Remittance
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li><strong>LRS Overseas Investment facility</strong> up to <strong>USD 2,50,000</strong> annually</li>
                    <li><strong>Outward remittances</strong> up to <strong>USD 50,000</strong> through dedicated desk</li>
                    <li>Seamless FX conversion rates for overseas education, property, or equity investments</li>
                </ul>
            </div>
        </details>

    </div>
</div>

<!-- PITCHES TAB -->
<div class="inner-tab-content inner-tab-content-pitches" style="display: none;">
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
        
        <div style="margin-bottom: 24px;">
            <h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">1. Demat & Trading Pitch</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 14px 16px; font-style: italic; color: #334155; font-size: 0.93rem; border-radius: 0 8px 8px 0; line-height: 1.6;">
                “Sir/Ma’am, as part of your Solitaire relationship, you get zero AMC on your Demat account along with institutional-grade trading rates—just 0.10% delivery and 0.01% intraday. You also get a dedicated dealer so you can place trades directly over phone without waiting in customer queues.”
            </div>
        </div>

        <div style="margin-bottom: 24px;">
            <h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">2. Margin Trading (MTF) Pitch</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 14px 16px; font-style: italic; color: #334155; font-size: 0.93rem; border-radius: 0 8px 8px 0; line-height: 1.6;">
                “If you regularly take short-to-medium term equity positions and want leverage without liquidating existing holdings, our Solitaire MTF rate is as low as 9.69% p.a. You can get up to 4x funding against your cash or stock margin.”
            </div>
        </div>

        <div style="margin-bottom: 24px;">
            <h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">3. Alternate Investments (AIF/PMS) Pitch</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 14px 16px; font-style: italic; color: #334155; font-size: 0.93rem; border-radius: 0 8px 8px 0; line-height: 1.6;">
                “For HNIs looking to diversify beyond traditional mutual funds, we provide access to curated Category I, II & III AIFs, PMS strategies, and structured high-yield debt opportunities tailored to your risk appetite.”
            </div>
        </div>

        <div>
            <h3 style="color: #0f172a; margin-bottom: 12px; font-size: 1.1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">4. Global Investment & Remittance Pitch</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 14px 16px; font-style: italic; color: #334155; font-size: 0.93rem; border-radius: 0 8px 8px 0; line-height: 1.6;">
                “Whether you are planning overseas investments, foreign education payments, or asset purchases abroad, under Solitaire you can remit up to USD 2,50,000 annually under LRS with preferential forex rates and zero processing hassle.”
            </div>
        </div>

    </div>
</div>

<!-- CALCULATOR TAB -->
<div class="inner-tab-content inner-tab-content-calculator" style="display: none;">
    <div style="background: linear-gradient(135deg, #f8faff 0%, #eff4ff 100%); border: 1.5px solid #e0e7ff; border-radius: 16px; padding: 28px; margin-bottom: 20px;">
        <h3 style="font-weight: 800; color: #1e3a8a; margin-bottom: 6px; font-size: 1.05rem;">📈 Investment Return Calculator</h3>
        <p style="color: #64748b; font-size: 0.85rem; margin-bottom: 20px;">Calculate your returns across SIP, SWP, and Lumpsum investments</p>
        
        <!-- Calculator Type Tabs -->
        <div style="display: flex; gap: 8px; margin-bottom: 24px; background: #e8eeff; border-radius: 10px; padding: 4px;">
            <button id="inv-tab-sip" onclick="switchInvCalc('sip')" style="flex:1; padding: 10px; border: none; border-radius: 8px; font-weight: 700; font-size: 0.9rem; cursor: pointer; background: #1e3a8a; color: white; transition: all 0.2s;">SIP</button>
            <button id="inv-tab-swp" onclick="switchInvCalc('swp')" style="flex:1; padding: 10px; border: none; border-radius: 8px; font-weight: 700; font-size: 0.9rem; cursor: pointer; background: transparent; color: #1e3a8a; transition: all 0.2s;">SWP</button>
            <button id="inv-tab-lump" onclick="switchInvCalc('lump')" style="flex:1; padding: 10px; border: none; border-radius: 8px; font-weight: 700; font-size: 0.9rem; cursor: pointer; background: transparent; color: #1e3a8a; transition: all 0.2s;">Lumpsum</button>
        </div>

        <!-- SIP Calculator -->
        <div id="inv-calc-sip" style="display:block;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Monthly SIP (₹)</label>
                    <input id="sip-amount" type="number" value="10000" min="500" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="10000" min="500" max="200000" step="500" oninput="document.getElementById('sip-amount').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Expected Return (%)</label>
                    <input id="sip-rate" type="number" value="12" min="1" max="30" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="12" min="1" max="30" step="0.5" oninput="document.getElementById('sip-rate').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Time Period (Years)</label>
                    <input id="sip-years" type="number" value="10" min="1" max="40" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="10" min="1" max="40" step="1" oninput="document.getElementById('sip-years').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
            </div>
        </div>

        <!-- SWP Calculator -->
        <div id="inv-calc-swp" style="display:none;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Total Investment (₹)</label>
                    <input id="swp-corpus" type="number" value="1000000" min="10000" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="1000000" min="100000" max="10000000" step="100000" oninput="document.getElementById('swp-corpus').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Monthly Withdrawal (₹)</label>
                    <input id="swp-withdrawal" type="number" value="8000" min="500" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="8000" min="500" max="200000" step="500" oninput="document.getElementById('swp-withdrawal').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Expected Return (%)</label>
                    <input id="swp-rate" type="number" value="8" min="1" max="20" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="8" min="1" max="20" step="0.5" oninput="document.getElementById('swp-rate').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
            </div>
        </div>

        <!-- Lumpsum Calculator -->
        <div id="inv-calc-lump" style="display:none;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Investment Amount (₹)</label>
                    <input id="lump-amount" type="number" value="500000" min="1000" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="500000" min="10000" max="10000000" step="10000" oninput="document.getElementById('lump-amount').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Expected Return (%)</label>
                    <input id="lump-rate" type="number" value="12" min="1" max="30" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="12" min="1" max="30" step="0.5" oninput="document.getElementById('lump-rate').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
                <div>
                    <label style="font-size: 0.8rem; font-weight: 700; color: #374151; display: block; margin-bottom: 6px;">Time Period (Years)</label>
                    <input id="lump-years" type="number" value="10" min="1" max="40" oninput="calcInv()" style="width:100%; padding: 10px 12px; border: 1.5px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; box-sizing: border-box;"/>
                    <input type="range" value="10" min="1" max="40" step="1" oninput="document.getElementById('lump-years').value=this.value;calcInv()" style="width:100%; margin-top:6px; accent-color:#1e3a8a;"/>
                </div>
            </div>
        </div>

        <!-- Results Row -->
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; background: white; padding: 20px; border-radius: 12px; border: 1px solid #e0e7ff; margin-top: 16px;">
            <div style="text-align: center;">
                <div style="font-size: 0.78rem; font-weight: 600; color: #64748b; text-transform: uppercase;">Invested Amount</div>
                <div id="inv-res-invested" style="font-size: 1.3rem; font-weight: 800; color: #1e293b; margin-top: 4px;">₹12,00,000</div>
            </div>
            <div style="text-align: center; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0;">
                <div style="font-size: 0.78rem; font-weight: 600; color: #64748b; text-transform: uppercase;">Est. Returns</div>
                <div id="inv-res-returns" style="font-size: 1.3rem; font-weight: 800; color: #10b981; margin-top: 4px;">₹11,23,391</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 0.78rem; font-weight: 600; color: #64748b; text-transform: uppercase;">Total Value</div>
                <div id="inv-res-total" style="font-size: 1.3rem; font-weight: 800; color: #1e3a8a; margin-top: 4px;">₹23,23,391</div>
            </div>
        </div>

    </div>
</div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# 3. NEW LIFESTYLE PANEL CONTENT FOR panel-lifestyle
# ─────────────────────────────────────────────────────────────────────────────
NEW_LIFESTYLE_HTML = """<h2 style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 8px;">Lifestyle Privileges</h2>
<p style="color: #64748b; line-height: 1.6; margin-bottom: 24px;">Curated dining, concierge, travel, and tactical live offers tailored for Solitaire members.</p>

<div class="inner-tabs-container" style="display: flex; gap: 8px; margin-bottom: 24px; background: #f1f5f9; padding: 6px; border-radius: 12px;">
    <button class="inner-tab-btn active" onclick="switchInnerTab(this, 'features')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #0f172a; background: white; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;">Features</button>
    <button class="inner-tab-btn" onclick="switchInnerTab(this, 'tactical')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;">Tactical / Live Offers</button>
    <button class="inner-tab-btn" onclick="switchInnerTab(this, 'pitches')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;">Pitches</button>
</div>

<!-- FEATURES TAB -->
<div class="inner-tab-content inner-tab-content-features" style="display: block;">
    <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">

        <!-- 1. Dining & Experiences -->
        <details open style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">🍽️</span> Dining & Experiences
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; margin-bottom: 14px; color: #166534;">
                    <strong style="font-size: 0.95rem;">Solitaire Table / District:</strong>
                    <ul style="margin: 6px 0 0 18px; padding: 0;">
                        <li><strong>20% Off</strong> up to <strong>₹5,000 per transaction</strong></li>
                        <li>Valid for <strong>2 transactions per month</strong> (Potential Value: <strong>₹10,000 / month</strong>)</li>
                    </ul>
                </div>
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Curated fine-dining experiences at premier luxury restaurants</li>
                    <li>Early access to select culinary events and pop-ups</li>
                    <li>Exclusive access to Chef's tables and custom tasting menus</li>
                </ul>
            </div>
        </details>

        <!-- 2. Travel & Concierge -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">🧳</span> Travel & Concierge (24/7 Solitaire Desk)
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li><strong>Solitaire Concierge:</strong> 24/7 dedicated lifestyle & travel assistance</li>
                    <li>Priority restaurant reservations & private dining arrangements</li>
                    <li>Hotel assistance, itinerary planning & bespoke travel arrangements</li>
                    <li>Fast-track Visa assistance & international travel guidance</li>
                    <li>Airport assistance & luxury airport transfers</li>
                    <li>Private shopping, luxury gifting assistance & special celebration planning</li>
                </ul>
            </div>
        </details>

        <!-- 3. Hotels & Stays -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">🏨</span> Hotels & Stays Privileges
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Luxury hotel privileges across top domestic & international chains</li>
                    <li>Selected <strong>complimentary-night / 50% off second-night</strong> offers (ITC Stays, Alaya, Elivaas)</li>
                    <li>Flat <strong>₹5,000 discount</strong> on stays at Postcard Hotels (India, Bhutan, Sri Lanka)</li>
                    <li>Premium stay experiences with complimentary room upgrades & early check-in subject to availability</li>
                </ul>
            </div>
        </details>

        <!-- 4. Entertainment & Experiences -->
        <details style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.98rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.1rem;">🎬</span> Entertainment & Experiences
                </span>
                <span style="font-size: 0.8rem; color: #64748b;">▼</span>
            </summary>
            <div style="padding: 16px 20px; color: #475569; font-size: 0.92rem; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Curated entertainment privileges & VIP event passes</li>
                    <li>Selected movie privileges (PVR Buy 1 Get 1 ticket offers)</li>
                    <li>Exclusive family experiences & cultural event access</li>
                </ul>
            </div>
        </details>

    </div>
</div>

<!-- TACTICAL / LIVE OFFERS TAB -->
<div class="inner-tab-content inner-tab-content-tactical" style="display: none;">
    <div style="background: #fffbeb; border: 1px solid #fef3c7; border-radius: 10px; padding: 14px 18px; margin-bottom: 20px; color: #92400e; font-size: 0.9rem;">
        ⚡ <strong>Tactical / Live Offers:</strong> Time-bound promotional offers with start & end dates. (Core Solitaire benefits remain live permanently).
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">

        <!-- 1. Dining -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="margin:0; font-size: 0.98rem; color: #0f172a;">🍽️ Dining & District Campaigns</h4>
                <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Valid till 31 Oct 2026</span>
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.88rem; line-height: 1.6;">
                <li>District Fine-Dining Promo: Extra ₹1,000 voucher on spends > ₹10,000</li>
                <li>Zomato Gold 1-Year complimentary activation</li>
            </ul>
        </div>

        <!-- 2. Travel -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="margin:0; font-size: 0.98rem; color: #0f172a;">✈️ Travel & Air Miles Campaigns</h4>
                <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Valid till 15 Nov 2026</span>
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.88rem; line-height: 1.6;">
                <li>Air India 1:1 Transfer Bonus: 15% extra miles on point transfers</li>
                <li>Airport meet-and-assist complimentary session on international flights</li>
            </ul>
        </div>

        <!-- 3. Entertainment -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="margin:0; font-size: 0.98rem; color: #0f172a;">🎬 Entertainment & Movies</h4>
                <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Valid till 30 Sep 2026</span>
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.88rem; line-height: 1.6;">
                <li>PVR Luxe: Buy 1 Get 1 ticket complimentary on eligible bookings</li>
                <li>Exclusive pre-sale passes to national concert tours</li>
            </ul>
        </div>

        <!-- 4. Shopping -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="margin:0; font-size: 0.98rem; color: #0f172a;">🛍️ Shopping & Luxury Retail</h4>
                <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Valid till 31 Dec 2026</span>
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.88rem; line-height: 1.6;">
                <li>10% instant cashback on selected luxury apparel partners</li>
                <li>Electronics voucher campaign: Accelerated Air Miles on brand vouchers</li>
            </ul>
        </div>

        <!-- 5. Vouchers -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="margin:0; font-size: 0.98rem; color: #0f172a;">🎁 Brand Vouchers</h4>
                <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Valid till 30 Nov 2026</span>
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.88rem; line-height: 1.6;">
                <li>5X Air Miles on Amazon & Taj brand gift vouchers via Unbox portal</li>
            </ul>
        </div>

        <!-- 6. Hotels -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="margin:0; font-size: 0.98rem; color: #0f172a;">🏨 Seasonal Hotel Campaigns</h4>
                <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Valid till 15 Nov 2026</span>
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 0.88rem; line-height: 1.6;">
                <li>Postcard Hotels: ₹5,000 off + complimentary spa credit on 2+ night bookings</li>
            </ul>
        </div>

    </div>
</div>

<!-- PITCHES TAB -->
<div class="inner-tab-content inner-tab-content-pitches" style="display: none;">
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
        
        <!-- Pitch A: Introduction -->
        <div style="margin-bottom: 28px;">
            <h3 style="color: #0f172a; margin-bottom: 8px; font-size: 1.05rem; font-weight: 700; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">A. INTRODUCTION PITCH</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px 18px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.93rem; line-height: 1.6; font-style: italic;">
                “Sir/Ma'am, Solitaire is not just a premium banking programme. Along with the banking and wealth benefits, you also get access to a range of curated lifestyle privileges. My role as your RM is to make sure you're actually able to use these benefits rather than having them simply sit as a feature on your account.”
            </div>
        </div>

        <!-- Pitch B: Dining -->
        <div style="margin-bottom: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; margin-bottom: 8px;">
                <h3 style="color: #0f172a; margin:0; font-size: 1.05rem; font-weight: 700;">B. DINING PITCH</h3>
                <span style="font-size: 0.78rem; background: #e0e7ff; color: #3730a3; padding: 2px 8px; border-radius: 4px; font-weight: 600;">🎯 Trigger: Customer mentions Dining / Restaurants / Weekend plans / Family dinner / Fine dining</span>
            </div>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px 18px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.93rem; line-height: 1.6; font-style: italic;">
                “If you regularly dine out, one Solitaire benefit I'd recommend using is the Solitaire Table through District. You can currently get 20% off, up to ₹5,000 per transaction, twice a month. There are also curated dining experiences and early access to select premium experiences.”
            </div>
        </div>

        <!-- Pitch C: Travel -->
        <div style="margin-bottom: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; margin-bottom: 8px;">
                <h3 style="color: #0f172a; margin:0; font-size: 1.05rem; font-weight: 700;">C. TRAVEL PITCH</h3>
                <span style="font-size: 0.78rem; background: #e0e7ff; color: #3730a3; padding: 2px 8px; border-radius: 4px; font-weight: 600;">🎯 Trigger: Customer mentions International travel / Holiday / Flights / Hotels / Family vacation</span>
            </div>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px 18px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.93rem; line-height: 1.6; font-style: italic;">
                “If you travel frequently, Solitaire has quite a strong lifestyle proposition around travel. Apart from the card benefits, you have access to Concierge support for hotels, travel planning, airport assistance and other arrangements. Before your next trip, I'd recommend checking with me first so I can see what Solitaire benefits are currently available.”
            </div>
        </div>

        <!-- Pitch D: Concierge -->
        <div style="margin-bottom: 28px;">
            <h3 style="color: #0f172a; margin-bottom: 8px; font-size: 1.05rem; font-weight: 700; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">D. CONCIERGE PITCH</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px 18px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.93rem; line-height: 1.6; font-style: italic;">
                “One benefit I particularly want you to be aware of is Solitaire Concierge. If there's something you need arranged—whether it's a restaurant reservation, hotel, airport assistance, gifting or a special occasion—you can reach out to the Concierge. The idea is to save you the time of coordinating these things yourself.”
            </div>
        </div>

        <!-- Pitch E: Hotel -->
        <div style="margin-bottom: 28px;">
            <h3 style="color: #0f172a; margin-bottom: 8px; font-size: 1.05rem; font-weight: 700; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">E. HOTEL PITCH</h3>
            <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px 18px; border-radius: 0 8px 8px 0; color: #334155; font-size: 0.93rem; line-height: 1.6; font-style: italic;">
                “Before you book your next premium hotel stay, I'd recommend checking with me once. Solitaire has access to selected hotel privileges and campaigns, and depending on the property and dates, you may be able to get a complimentary night, a discounted night or another exclusive benefit.”
            </div>
        </div>

        <!-- Pitch F: Tactical Offer -->
        <div>
            <h3 style="color: #0f172a; margin-bottom: 8px; font-size: 1.05rem; font-weight: 700; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px;">F. TACTICAL OFFER PITCH (Dynamic)</h3>
            <div style="background: #eef2ff; border-left: 4px solid #3b82f6; padding: 16px 18px; border-radius: 0 8px 8px 0; color: #1e40af; font-size: 0.93rem; line-height: 1.6; font-style: italic; margin-bottom: 12px;">
                “Sir/Ma'am, there's currently a Solitaire offer running that I thought would be relevant to you. <strong>[OFFER BENEFIT]</strong>. It's valid until <strong>[DATE]</strong>, so if you're planning <strong>[USE CASE]</strong>, this would be a good time to use it.”
            </div>
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px 16px; border-radius: 8px; color: #166534; font-size: 0.88rem; line-height: 1.55;">
                <strong>Example Script:</strong> “Sir, there's currently a Solitaire movie offer where you can get a complimentary ticket on eligible bookings. Since you mentioned you usually watch movies with your family, this could be useful before the offer expires on 30 September.”
            </div>
        </div>

    </div>
</div>
"""

def update_file(fname):
    c = get(fname)
    print(f"\n==================== Updating {fname} ====================")
    
    # 1. Replace panel-intro content
    # Find <div class="info-panel active" id="panel-intro"> ... </div> (up to panel-lifestyle)
    p_intro_start = c.find('id="panel-intro"')
    if p_intro_start != -1:
        # find opening <div for panel-intro
        div_start = c.rfind('<div', 0, p_intro_start)
        # find start of panel-lifestyle
        p_life_start = c.find('id="panel-lifestyle"')
        div_life_start = c.rfind('<div', 0, p_life_start)
        
        old_intro = c[div_start:div_life_start]
        new_intro_panel = f'<div class="info-panel active" id="panel-intro">\n{NEW_INTRO_HTML}\n</div>\n'
        c = c[:div_start] + new_intro_panel + c[div_life_start:]
        print("Updated panel-intro!")
        
    # 2. Replace panel-investments content
    p_inv_start = c.find('id="panel-investments"')
    if p_inv_start != -1:
        div_start = c.rfind('<div', 0, p_inv_start)
        # find end of panel-investments (next panel or closing div)
        # usually next panel is <div class="info-panel" ...> or end of section
        next_panel = c.find('class="info-panel"', p_inv_start)
        if next_panel == -1:
            next_panel = c.find('<!-- close', p_inv_start)
        if next_panel == -1:
            next_panel = c.find('</body>', p_inv_start)
        div_next_start = c.rfind('<div', 0, next_panel) if 'class="info-panel"' in c[next_panel-20:next_panel+50] else next_panel
        
        new_inv_panel = f'<div class="info-panel" id="panel-investments">\n{NEW_INVESTMENTS_HTML}\n</div>\n'
        c = c[:div_start] + new_inv_panel + c[div_next_start:]
        print("Updated panel-investments!")

    # 3. Replace panel-lifestyle content
    p_life_start = c.find('id="panel-lifestyle"')
    if p_life_start != -1:
        div_start = c.rfind('<div', 0, p_life_start)
        p_summary_start = c.find('id="panel-summary"')
        div_summary_start = c.rfind('<div', 0, p_summary_start)
        
        new_life_panel = f'<div class="info-panel" id="panel-lifestyle">\n{NEW_LIFESTYLE_HTML}\n</div>\n'
        c = c[:div_start] + new_life_panel + c[div_summary_start:]
        print("Updated panel-lifestyle!")

    save(fname, c)
    print(f"Saved {fname} successfully!")

update_file("experience_solitaire_dashboard_new.html")
