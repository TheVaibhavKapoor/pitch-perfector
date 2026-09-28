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
# 1. NEW HOME LOAN (HL) PANE CONTENT (EXACT PITCHES A-G + INTERACTIVE HL CALCULATOR)
# ─────────────────────────────────────────────────────────────────────────────
NEW_HL_PANE_HTML = """    <div id="loan-content-hl" class="loan-detail-pane" style="display: block;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🏠</span> Home Loan (HL) Solutions
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
            <li><strong>Balance Transfer & Top-Up:</strong> Move existing high-cost loan and raise extra funds seamlessly</li>
            <li><strong>Doorstep Assistance:</strong> Dedicated Relationship Manager for end-to-end documentation</li>
        </ul>

        <!-- 2. Pitches (A to G) -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 12px 0; display: flex; align-items: center; gap: 6px;">
            <span>🗣️</span> Relationship Manager Conversation Pitches
        </h4>

        <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px;">

            <!-- Pitch A -->
            <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #1e40af; margin-bottom: 4px;">A. General Property Purchase Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “Sir/Ma'am, if you're planning to purchase a property, I'd be happy to help you evaluate the Home Loan option with Kotak as well. Apart from the loan amount, we can look at the overall structure—interest rate, tenure, EMI and associated charges—to make sure the financing is optimised for you.”
                </div>
            </div>

            <!-- Pitch B -->
            <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #065f46; margin-bottom: 4px;">B. Premium / Solitaire Member Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “Since you have a premium relationship with Kotak, I'd recommend that we evaluate your Home Loan requirement through Kotak before you finalise the financing elsewhere. We can look at the eligible loan amount, rate, tenure and structure, and I can help you work out the most efficient EMI for the property you're considering.”
                </div>
            </div>

            <!-- Pitch C -->
            <div style="background: #f8fafc; border-left: 4px solid #f59e0b; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #b45309; margin-bottom: 4px;">C. Customer Already Has a Home Loan Elsewhere</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic; margin-bottom: 6px;">
                    “Sir/Ma'am, if you already have a Home Loan with another bank, I can also evaluate whether moving it to Kotak makes financial sense. We can compare your current rate and remaining tenure against the Kotak option and calculate the actual interest saving rather than looking at just the rate difference.”
                </div>
                <div style="background: #fef3c7; color: #92400e; font-weight: 700; font-size: 0.82rem; padding: 6px 10px; border-radius: 6px; font-style: normal;">
                    🎯 CTA: “If you share your current outstanding, interest rate and remaining tenure, I can calculate the potential saving for you.”
                </div>
            </div>

            <!-- Pitch D -->
            <div style="background: #f8fafc; border-left: 4px solid #8b5cf6; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #6d28d9; margin-bottom: 4px;">D. BT + Top-Up Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic; margin-bottom: 6px;">
                    “If you already have a Home Loan and also need additional liquidity, we don't necessarily have to look at these as two separate requirements. We can evaluate a Balance Transfer along with a Top-Up, so you can potentially move the existing loan and raise additional funds against the property.”
                </div>
                <div style="background: #ede9fe; color: #5b21b6; font-weight: 700; font-size: 0.82rem; padding: 6px 10px; border-radius: 6px; font-style: normal;">
                    🎯 CTA: “Give me your current outstanding and the additional amount you're looking for, and I'll work out the combined EMI and overall benefit.”
                </div>
            </div>

            <!-- Pitch E -->
            <div style="background: #f8fafc; border-left: 4px solid #ec4899; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #be185d; margin-bottom: 4px;">E. First-Time Home Buyer</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “If this is your first property purchase, I can help you structure the financing from the beginning—how much to fund through the loan, how much to keep as your own contribution, and what tenure keeps the EMI comfortable without unnecessarily increasing the total interest burden.”
                </div>
            </div>

            <!-- Pitch F -->
            <div style="background: #f8fafc; border-left: 4px solid #06b6d4; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #0e7490; margin-bottom: 4px;">F. High-Value Property / HNI Customer</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “For a higher-value property, the important part isn't simply getting a loan. It's structuring the funding efficiently while keeping your liquidity available for your other investments and commitments. We can evaluate the Kotak Home Loan against your overall financial position and decide how much it makes sense to fund through debt.”
                </div>
            </div>

            <!-- Pitch G -->
            <div style="background: #f8fafc; border-left: 4px solid #64748b; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #334155; margin-bottom: 4px;">G. Short 15-Second Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “If you're considering a property purchase or already have a Home Loan, let me run the numbers for you with Kotak. I'll compare the EMI, total interest and overall cost so you can see whether there is a genuine financial advantage.”
                </div>
            </div>

        </div>

        <!-- 3. Interactive Home Loan Calculator -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px;">
            <h4 style="margin: 0 0 14px 0; font-size: 0.95rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🧮</span> Interactive Home Loan EMI & Savings Calculator
            </h4>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div>
                    <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Loan Amount (₹)</label>
                    <input type="range" id="hl-calc-amt" min="2500000" max="100000000" step="500000" value="30000000" oninput="runHLCalculator()" style="width: 100%;">
                    <div style="font-weight: 800; color: #1e3a8a; font-size: 1rem; margin-top: 4px;" id="hl-calc-amt-lbl">₹3.00 Crore</div>
                </div>

                <div>
                    <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Tenure (Years)</label>
                    <input type="range" id="hl-calc-tenure" min="5" max="30" step="1" value="20" oninput="runHLCalculator()" style="width: 100%;">
                    <div style="font-weight: 800; color: #1e3a8a; font-size: 1rem; margin-top: 4px;" id="hl-calc-tenure-lbl">20 Years</div>
                </div>

                <div>
                    <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Standard Rate vs Solitaire</label>
                    <select id="hl-calc-rate" onchange="runHLCalculator()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1; font-weight: 600; font-size: 0.85rem;">
                        <option value="8.75|8.50" selected>Standard 8.75% vs Solitaire 8.50% (0.25% off)</option>
                        <option value="9.00|8.65">Standard 9.00% vs Solitaire 8.65% (0.35% off)</option>
                        <option value="9.25|8.75">Standard 9.25% vs Solitaire 8.75% (0.50% off)</option>
                    </select>
                </div>
            </div>

            <!-- Output Display -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
                <div style="background: #ffffff; border: 1px solid #e2e8f0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.78rem; color: #64748b; display: block;">Solitaire Monthly EMI</span>
                    <strong style="font-size: 1.15rem; color: #1e3a8a;" id="hl-calc-emi">₹2,59,960 / mo</strong>
                </div>

                <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.78rem; color: #065f46; display: block;">1st-Year Interest Savings</span>
                    <strong style="font-size: 1.15rem; color: #059669;" id="hl-calc-yr1-savings">₹75,000 / yr</strong>
                </div>

                <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.78rem; color: #1e40af; display: block;">Total Lifetime Interest Savings</span>
                    <strong style="font-size: 1.15rem; color: #2563eb;" id="hl-calc-total-savings">₹11,43,200</strong>
                </div>
            </div>
        </div>
    </div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# 2. NEW MUTUAL FUNDS (MF) PANE CONTENT (EXACT PITCHES A-I + INTERACTIVE SIP/SWP CALCULATOR)
# ─────────────────────────────────────────────────────────────────────────────
NEW_MF_PANE_HTML = """    <div id="inv-content-mf" class="inv-detail-pane" style="display: block;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>📈</span> Mutual Funds & Objective-Driven Wealth Creation
            </h3>
            <span style="background: #eff6ff; color: #2563eb; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Direct Plan Access</span>
        </div>

        <!-- 1. Features -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0; display: flex; align-items: gap: 6px;">
            <span>📌</span> Key Features & Framework
        </h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Objective-First Approach:</strong> Start with customer goals (retirement, education, property) rather than product names</li>
            <li><strong>SIP & SWP Cash-Flow Planning:</strong> Automated wealth accumulation and tax-efficient monthly income streams</li>
            <li><strong>Surplus & FD Reallocation:</strong> Optimised asset allocation between stable fixed-income and market-linked growth</li>
            <li><strong>Consolidated Portfolio Review:</strong> Overlap removal and rebalancing for existing investments across platforms</li>
        </ul>

        <!-- 2. Pitches (A to I) -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 12px 0; display: flex; align-items: center; gap: 6px;">
            <span>🗣️</span> Relationship Manager Conversation Pitches
        </h4>

        <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px;">

            <!-- Pitch A -->
            <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #1e40af; margin-bottom: 4px;">A. General Investment Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “Sir/Ma'am, apart from keeping money in savings and fixed-income products, we can also look at creating a systematic investment portfolio based on your goals. Through Kotak, we can help you build and manage a Mutual Fund portfolio based on your investment horizon, risk profile and objectives.”
                </div>
            </div>

            <!-- Pitch B -->
            <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #065f46; margin-bottom: 4px;">B. Idle Savings / Excess Account Balance</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “I noticed you generally maintain a healthy balance in your account. Instead of keeping the entire surplus idle, would you be open to exploring whether a portion of it can be put to work through investments? We can keep your required liquidity aside and invest the surplus according to your goals and risk appetite.”
                </div>
            </div>

            <!-- Pitch C -->
            <div style="background: #f8fafc; border-left: 4px solid #f59e0b; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #b45309; margin-bottom: 4px;">C. Systematic Investment Plan (SIP) Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic; margin-bottom: 6px;">
                    “If your objective is long-term wealth creation, we don't necessarily need to start with a large lump sum. We can start with a monthly SIP and build the portfolio gradually. The amount can also be increased periodically as your income grows.”
                </div>
                <div style="background: #fef3c7; color: #92400e; font-weight: 700; font-size: 0.82rem; padding: 6px 10px; border-radius: 6px; font-style: normal;">
                    🎯 CTA: “If you tell me the amount you're comfortable investing every month and your time horizon, I can show you what the potential corpus could look like.”
                </div>
            </div>

            <!-- Pitch D -->
            <div style="background: #f8fafc; border-left: 4px solid #8b5cf6; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #6d28d9; margin-bottom: 4px;">D. Lump-Sum Investment Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “If you have a surplus amount that you don't need immediately, we can evaluate whether deploying a portion of it into Mutual Funds makes sense for your financial goals. Rather than investing the entire amount blindly, we can look at asset allocation, risk and investment horizon first.”
                </div>
            </div>

            <!-- Pitch E -->
            <div style="background: #f8fafc; border-left: 4px solid #ec4899; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #be185d; margin-bottom: 4px;">E. Existing FD Customer Pitch (Asset Allocation)</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “If a significant portion of your wealth is currently sitting in FDs, I wouldn't suggest replacing your FDs completely. Instead, we can look at the overall allocation—how much you want to keep in stable fixed-income products and whether a portion can be allocated towards market-linked investments for long-term growth.”
                </div>
            </div>

            <!-- Pitch F -->
            <div style="background: #f8fafc; border-left: 4px solid #06b6d4; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #0e7490; margin-bottom: 4px;">F. Existing MF Investor — Other Bank / Platform</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “If you already invest in Mutual Funds through another platform or bank, I'd be happy to review the portfolio with you. We can look at the current allocation, diversification, overlapping funds and whether the portfolio is aligned with your goals. If there are gaps, we can explore how Kotak can support the investment relationship.”
                </div>
            </div>

            <!-- Pitch G -->
            <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #065f46; margin-bottom: 4px;">G. Goal-Based Investment Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “Rather than selecting a Mutual Fund first, I'd prefer to understand what you're investing for—retirement, children's education, a property, travel or simply long-term wealth creation. Once we know the goal and time horizon, we can work backwards to determine the investment amount and suitable portfolio approach.”
                </div>
            </div>

            <!-- Pitch H -->
            <div style="background: #f8fafc; border-left: 4px solid #6366f1; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #4338ca; margin-bottom: 4px;">H. Wealth / Solitaire Member Consolidated Review</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “Given the size of your overall relationship, I would recommend looking at your investments as one consolidated portfolio rather than individual products. We can review your Mutual Funds, equity and other investments, understand the allocation and then identify where we can improve diversification or align the portfolio better with your long-term goals.”
                </div>
            </div>

            <!-- Pitch I -->
            <div style="background: #f8fafc; border-left: 4px solid #f43f5e; padding: 12px 16px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 700; font-size: 0.85rem; color: #be123c; margin-bottom: 4px;">I. SWP / Retirement Monthly Cash Flow Pitch</div>
                <div style="color: #334155; font-size: 0.88rem; line-height: 1.6; font-style: italic;">
                    “If you're approaching retirement or already have a sizeable investment corpus, the conversation changes from just accumulation to generating a sustainable cash flow. We can evaluate an investment and withdrawal strategy that provides regular liquidity while keeping the remaining corpus invested according to your requirements.”
                </div>
            </div>

        </div>

        <!-- 3. Interactive SIP & SWP Wealth Calculator -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px;">
            <h4 style="margin: 0 0 14px 0; font-size: 0.95rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🧮</span> Interactive SIP & SWP Wealth Calculator
            </h4>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div>
                    <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Monthly SIP Amount (₹)</label>
                    <input type="range" id="mf-calc-sip" min="5000" max="250000" step="5000" value="50000" oninput="runMFCalculator()" style="width: 100%;">
                    <div style="font-weight: 800; color: #1e3a8a; font-size: 1rem; margin-top: 4px;" id="mf-calc-sip-lbl">₹50,000 / mo</div>
                </div>

                <div>
                    <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Investment Horizon (Years)</label>
                    <input type="range" id="mf-calc-yrs" min="3" max="25" step="1" value="10" oninput="runMFCalculator()" style="width: 100%;">
                    <div style="font-weight: 800; color: #1e3a8a; font-size: 1rem; margin-top: 4px;" id="mf-calc-yrs-lbl">10 Years</div>
                </div>

                <div>
                    <label style="font-size: 0.82rem; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Expected Return (% p.a.)</label>
                    <select id="mf-calc-rate" onchange="runMFCalculator()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1; font-weight: 600; font-size: 0.85rem;">
                        <option value="10">Conservative Hybrid (10% p.a.)</option>
                        <option value="12" selected>Balanced Equity (12% p.a.)</option>
                        <option value="14">Aggressive Growth (14% p.a.)</option>
                    </select>
                </div>
            </div>

            <!-- Output Display -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
                <div style="background: #ffffff; border: 1px solid #e2e8f0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.78rem; color: #64748b; display: block;">Total Invested Amount</span>
                    <strong style="font-size: 1.15rem; color: #334155;" id="mf-calc-inv">₹60.00 Lakh</strong>
                </div>

                <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.78rem; color: #1e40af; display: block;">Projected Maturity Corpus</span>
                    <strong style="font-size: 1.15rem; color: #1e3a8a;" id="mf-calc-corpus">₹1.16 Crore</strong>
                </div>

                <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 0.78rem; color: #065f46; display: block;">Sustainable SWP Monthly Income</span>
                    <strong style="font-size: 1.15rem; color: #059669;" id="mf-calc-swp">~₹77,500 / mo</strong>
                </div>
            </div>
        </div>
    </div>
"""

# JS Functions for HL & MF Calculators
JS_CALCULATOR_SCRIPTS = """
function runHLCalculator() {
    const amtEl = document.getElementById('hl-calc-amt');
    const tenureEl = document.getElementById('hl-calc-tenure');
    const rateEl = document.getElementById('hl-calc-rate');
    
    if (!amtEl || !tenureEl || !rateEl) return;
    
    const P = parseFloat(amtEl.value);
    const N = parseInt(tenureEl.value) * 12;
    const rates = rateEl.value.split('|');
    const rStd = parseFloat(rates[0]) / 12 / 100;
    const rSol = parseFloat(rates[1]) / 12 / 100;
    
    document.getElementById('hl-calc-amt-lbl').innerText = `₹${(P / 10000000).toFixed(2)} Crore`;
    document.getElementById('hl-calc-tenure-lbl').innerText = `${tenureEl.value} Years`;
    
    # Calculate Solitaire EMI
    const emiSol = (P * rSol * Math.pow(1 + rSol, N)) / (Math.pow(1 + rSol, N) - 1);
    const emiStd = (P * rStd * Math.pow(1 + rStd, N)) / (Math.pow(1 + rStd, N) - 1);
    
    document.getElementById('hl-calc-emi').innerText = `₹${Math.round(emiSol).toLocaleString('en-IN')} / mo`;
    
    # First Year Interest Savings
    const rateDiff = (parseFloat(rates[0]) - parseFloat(rates[1])) / 100;
    const yr1Savings = Math.round(P * rateDiff);
    document.getElementById('hl-calc-yr1-savings').innerText = `₹${yr1Savings.toLocaleString('en-IN')} / yr`;
    
    # Total Lifetime Interest Savings
    const totalPaySol = emiSol * N;
    const totalPayStd = emiStd * N;
    const totalSavings = Math.round(totalPayStd - totalPaySol);
    document.getElementById('hl-calc-total-savings').innerText = `₹${totalSavings.toLocaleString('en-IN')}`;
}

function runMFCalculator() {
    const sipEl = document.getElementById('mf-calc-sip');
    const yrsEl = document.getElementById('mf-calc-yrs');
    const rateEl = document.getElementById('mf-calc-rate');
    
    if (!sipEl || !yrsEl || !rateEl) return;
    
    const P = parseFloat(sipEl.value);
    const yrs = parseInt(yrsEl.value);
    const rate = parseFloat(rateEl.value);
    const n = yrs * 12;
    const i = rate / 12 / 100;
    
    document.getElementById('mf-calc-sip-lbl').innerText = `₹${P.toLocaleString('en-IN')} / mo`;
    document.getElementById('mf-calc-yrs-lbl').innerText = `${yrs} Years`;
    
    const totalInv = P * n;
    const corpus = P * ((Math.pow(1 + i, n) - 1) / i) * (1 + i);
    const swpMonthly = (corpus * 0.08) / 12; # 8% annual SWP rate
    
    document.getElementById('mf-calc-inv').innerText = `₹${(totalInv / 100000).toFixed(2)} Lakh`;
    document.getElementById('mf-calc-corpus').innerText = corpus >= 10000000 ? `₹${(corpus / 10000000).toFixed(2)} Crore` : `₹${(corpus / 100000).toFixed(2)} Lakh`;
    document.getElementById('mf-calc-swp').innerText = `~₹${Math.round(swpMonthly).toLocaleString('en-IN')} / mo`;
}
"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)
print(f"\n==================== Injecting HL Pitches A-G & MF Pitches A-I into {fname} ====================")

# Replace loan-content-hl
hl_start = c.find('<div id="loan-content-hl"')
if hl_start != -1:
    lap_start = c.find('<div id="loan-content-lap"')
    c = c[:hl_start] + NEW_HL_PANE_HTML + "\n" + c[lap_start:]
    print("Replaced loan-content-hl with exact pitches A-G and interactive HL calculator!")

# Replace inv-content-mf
mf_start = c.find('<div id="inv-content-mf"')
if mf_start != -1:
    ipo_start = c.find('<div id="inv-content-ipo"')
    c = c[:mf_start] + NEW_MF_PANE_HTML + "\n" + c[ipo_start:]
    print("Replaced inv-content-mf with exact pitches A-I and interactive SIP/SWP calculator!")

# Inject JS calculator logic before </body>
if "function runHLCalculator" not in c:
    pos_body = c.find('</body>')
    if pos_body != -1:
        c = c[:pos_body] + f'\n<script>\n{JS_CALCULATOR_SCRIPTS}\n</script>\n' + c[pos_body:]
        print("Injected JS calculator logic before </body>!")

save(fname, c)
print("Successfully saved updated experience_solitaire_dashboard_new.html!")
