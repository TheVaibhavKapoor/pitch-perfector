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
# 1. NEW EXPANDABLE HOME LOAN (HL) PANE
# ─────────────────────────────────────────────────────────────────────────────
NEW_HL_PANE_EXPANDABLE = """    <div id="loan-content-hl" class="loan-detail-pane" style="display: block;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🏠</span> Home Loan (HL) Solutions
            </h3>
            <span style="background: #eff6ff; color: #2563eb; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Pre-approved up to ₹7.5 Cr</span>
        </div>

        <!-- 1. Features (Always Visible) -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0; display: flex; align-items: center; gap: 6px;">
            <span>📌</span> Key Features & Privileges
        </h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Preferential Rate Advantage:</strong> ~0.25% interest rate discount for Solitaire members</li>
            <li><strong>Zero Processing Fees</strong> & priority credit underwriting with fast-track processing</li>
            <li><strong>Balance Transfer & Top-Up:</strong> Move existing high-cost loan and raise extra funds seamlessly</li>
            <li><strong>Doorstep Assistance:</strong> Dedicated Relationship Manager for end-to-end documentation</li>
        </ul>

        <!-- 2. EXPANDABLE Pitches (A to G) -->
        <details style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; overflow: hidden; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 8px;">
                    <span>🗣️</span> Relationship Manager Conversation Pitches (7 Pitches & CTAs)
                </span>
                <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand Pitches</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; display: flex; flex-direction: column; gap: 10px;">

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
        </details>

        <!-- 3. EXPANDABLE Home Loan Calculator -->
        <details style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 8px;">
                    <span>🧮</span> Interactive Home Loan EMI & Savings Calculator
                </span>
                <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand Calculator</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
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
        </details>
    </div>
"""


# ─────────────────────────────────────────────────────────────────────────────
# 2. NEW EXPANDABLE MUTUAL FUNDS (MF) PANE
# ─────────────────────────────────────────────────────────────────────────────
NEW_MF_PANE_EXPANDABLE = """    <div id="inv-content-mf" class="inv-detail-pane" style="display: block;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; border-bottom: 1px solid #f1f5f9; padding-bottom: 12px;">
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>📈</span> Mutual Funds & Objective-Driven Wealth Creation
            </h3>
            <span style="background: #eff6ff; color: #2563eb; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Direct Plan Access</span>
        </div>

        <!-- 1. Features (Always Visible) -->
        <h4 style="font-size: 0.92rem; font-weight: 700; color: #1e293b; margin: 0 0 8px 0; display: flex; align-items: center; gap: 6px;">
            <span>📌</span> Key Features & Framework
        </h4>
        <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 0.9rem; line-height: 1.65;">
            <li><strong>Objective-First Approach:</strong> Start with customer goals (retirement, education, property) rather than product names</li>
            <li><strong>SIP & SWP Cash-Flow Planning:</strong> Automated wealth accumulation and tax-efficient monthly income streams</li>
            <li><strong>Surplus & FD Reallocation:</strong> Optimised asset allocation between stable fixed-income and market-linked growth</li>
            <li><strong>Consolidated Portfolio Review:</strong> Overlap removal and rebalancing for existing investments across platforms</li>
        </ul>

        <!-- 2. EXPANDABLE Pitches (A to I) -->
        <details style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; overflow: hidden; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 8px;">
                    <span>🗣️</span> Relationship Manager Conversation Pitches (9 Objective Pitches & CTAs)
                </span>
                <span style="font-size: 0.8rem; color: #10b981; font-weight: 700;">▼ Click to Expand Pitches</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; display: flex; flex-direction: column; gap: 10px;">

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
        </details>

        <!-- 3. EXPANDABLE SIP & SWP Calculator -->
        <details style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span style="display: flex; align-items: center; gap: 8px;">
                    <span>🧮</span> Interactive SIP & SWP Wealth Calculator
                </span>
                <span style="font-size: 0.8rem; color: #10b981; font-weight: 700;">▼ Click to Expand Calculator</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0; background: #ffffff;">
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
        </details>
    </div>
"""

# Apply expandable wrap for other products as well (LAP, LAS, OD, Auto, Personal, Demat, IPO, MTF, AIF, LRS)
def make_pitch_expandable_general(html_text):
    # Match pitch block and wrap in details
    html_text = re.sub(
        r'<h4 style="[^"]*">🗣️ (.*?)Pitch Script</h4>\s*<div class="pitch-box" style="([^"]*)">(.*?)</div>',
        r'''<details style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; overflow: hidden; margin-bottom: 16px;">
    <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
        <span>🗣️ Relationship Manager Pitch Script</span>
        <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand Pitch</span>
    </summary>
    <div style="padding: 18px; border-top: 1px solid #e2e8f0;">
        <div style="\2">\3</div>
    </div>
</details>''',
        html_text,
        flags=re.DOTALL
    )
    return html_text

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)
print(f"\n==================== Making Pitches and Calculators Expandable in {fname} ====================")

# Replace loan-content-hl
hl_start = c.find('<div id="loan-content-hl"')
if hl_start != -1:
    lap_start = c.find('<div id="loan-content-lap"')
    c = c[:hl_start] + NEW_HL_PANE_EXPANDABLE + "\n" + c[lap_start:]
    print("Replaced loan-content-hl with expandable pitches and expandable calculator!")

# Replace inv-content-mf
mf_start = c.find('<div id="inv-content-mf"')
if mf_start != -1:
    ipo_start = c.find('<div id="inv-content-ipo"')
    c = c[:mf_start] + NEW_MF_PANE_EXPANDABLE + "\n" + c[ipo_start:]
    print("Replaced inv-content-mf with expandable pitches and expandable calculator!")

# Wrap pitch script sections in details for all other loan panes (LAP, LAS, OD, Auto, Personal)
panes = ["lap", "las", "od", "auto", "personal", "demat", "ipo", "mtf", "aif", "lrs"]
for pane_id in panes:
    p_start = c.find(f'id="loan-content-{pane_id}"') if pane_id in ["lap", "las", "od", "auto", "personal"] else c.find(f'id="inv-content-{pane_id}"')
    if p_start != -1:
        next_pane_idx = c.find('<div id="', p_start + 10)
        if next_pane_idx == -1: next_pane_idx = c.find('</div>\n\n</div>', p_start)
        
        pane_block = c[p_start:next_pane_idx]
        
        # Replace pitch h4 + div with details wrapper if not already details
        if '🗣️' in pane_block and '<details' not in pane_block[pane_block.find('🗣️')-50:pane_block.find('🗣️')]:
            old_pattern = re.compile(r'<h4 style="[^"]*">🗣️ Relationship Manager Pitch Script</h4>\s*<div style="([^"]*)">(.*?)</div>', re.DOTALL)
            new_block = old_pattern.sub(
                r'''<details style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; overflow: hidden; margin-bottom: 16px;">
            <summary style="padding: 14px 18px; font-weight: 700; color: #0f172a; font-size: 0.92rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; user-select: none;">
                <span>🗣️ Relationship Manager Pitch Script</span>
                <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼ Click to Expand Pitch</span>
            </summary>
            <div style="padding: 18px; border-top: 1px solid #e2e8f0;">
                <div style="\1">\2</div>
            </div>
        </details>''',
                pane_block
            )
            c = c[:p_start] + new_block + c[next_pane_idx:]
            print(f"Wrapped pitch script in expandable details for pane: {pane_id}!")

save(fname, c)
print("Successfully saved expandable pitches and calculators in experience_solitaire_dashboard_new.html!")
