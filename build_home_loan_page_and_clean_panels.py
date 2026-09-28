import re, codecs

summary_panel_html = '''<div class="info-panel" id="panel-assets">
                    <h2 style="font-size: 1.25rem; font-weight: 800; color: #111827; margin-bottom: 6px;">Premium Home Loans &amp; Lending</h2>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 20px;">Unlock bespoke asset-backed lending with preferential rates, zero processing fees, and express approvals.</p>

                    <!-- FEATURED: Home Loan Summary Hero Card -->
                    <div style="background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #1d4ed8 100%); border-radius: 16px; padding: 24px; margin-bottom: 24px; color: white; position: relative; overflow: hidden; box-shadow: 0 8px 24px rgba(30, 58, 138, 0.25);">
                        <div style="position: absolute; top: -20px; right: -20px; width: 140px; height: 140px; background: rgba(255,255,255,0.06); border-radius: 50%;"></div>
                        <div style="position: absolute; bottom: -30px; right: 80px; width: 90px; height: 90px; background: rgba(255,255,255,0.05); border-radius: 50%;"></div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; position: relative; z-index: 2;">
                            <div>
                                <div style="display: inline-flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.18); border-radius: 20px; padding: 4px 14px; font-size: 0.75rem; font-weight: 700; margin-bottom: 14px; letter-spacing: 0.5px;">? FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>
                                <h3 style="font-size: 1.5rem; font-weight: 900; margin-bottom: 6px; letter-spacing: -0.5px;">Home Loan</h3>
                                <p style="opacity: 0.82; font-size: 0.88rem; margin-bottom: 18px;">Solitaire exclusive preferential pricing for your dream home</p>
                                <div style="display: flex; align-items: flex-end; gap: 8px; margin-bottom: 8px;">
                                    <span style="font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; line-height: 1;">7.50%</span>
                                    <span style="font-size: 1rem; opacity: 0.8; margin-bottom: 10px;">p.a. onwards*</span>
                                </div>
                                <div style="font-size: 0.78rem; opacity: 0.85; background: rgba(255,255,255,0.12); display: inline-block; padding: 5px 12px; border-radius: 6px;">Standard market rate is 7.80% &mdash; You save <strong style="color: #6ee7b7;">0.30% p.a.</strong></div>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 8px; min-width: 180px;">
                                <div style="background: rgba(255,255,255,0.13); border-radius: 10px; padding: 12px;">
                                    <div style="font-size: 0.7rem; opacity: 0.75; margin-bottom: 4px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Max Loan Amount</div>
                                    <div style="font-size: 1.1rem; font-weight: 800;">&#8377;5 Crore+</div>
                                </div>
                                <div style="background: rgba(255,255,255,0.13); border-radius: 10px; padding: 12px;">
                                    <div style="font-size: 0.7rem; opacity: 0.75; margin-bottom: 4px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Max Tenure</div>
                                    <div style="font-size: 1.1rem; font-weight: 800;">30 Years</div>
                                </div>
                                <div style="background: rgba(255,255,255,0.13); border-radius: 10px; padding: 12px;">
                                    <div style="font-size: 0.7rem; opacity: 0.75; margin-bottom: 4px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Processing Fee</div>
                                    <div style="font-size: 1.1rem; font-weight: 800; color: #6ee7b7;">ZERO &#10003;</div>
                                </div>
                            </div>
                        </div>

                        <div style="margin-top: 20px; display: flex; gap: 8px; flex-wrap: wrap; position: relative; z-index: 2;">
                            <span style="background: rgba(255,255,255,0.14); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 600;">&#9989; Balance Transfer Available</span>
                            <span style="background: rgba(255,255,255,0.14); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 600;">&#9989; Top-Up Facility</span>
                            <span style="background: rgba(255,255,255,0.14); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 600;">&#9989; Part-Payment Free</span>
                            <span style="background: rgba(255,255,255,0.14); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 600;">&#9989; Dedicated RM</span>
                        </div>

                        <div style="margin-top: 20px; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.18); padding-top: 18px; position: relative; z-index: 2;">
                            <span style="font-size: 0.88rem; font-weight: 600; opacity: 0.95;">Want to calculate your exact EMI &amp; interest savings?</span>
                            <button onclick="window.open('home_loan_calculator.html', '_blank')" style="background: #ffffff; color: #1e3a8a; border: none; padding: 12px 24px; border-radius: 10px; font-weight: 800; font-size: 0.9rem; cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,0.2); transition: transform 0.2s;">
                                &#129358; CALCULATE YOUR HOME LOAN BENEFIT &rarr;
                            </button>
                        </div>
                    </div>

                    <!-- All Solitaire Loan Products -->
                    <h3 style="font-weight: 700; color: #111827; margin-bottom: 14px; font-size: 0.95rem;">All Solitaire Loan Products</h3>
                    <div class="product-features-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 24px;">
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">&#127968;</span><h3>Home Loan (Preferential)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #10b981;">7.50% p.a.</strong> (vs 7.80% market rate)</li>
                                <li>Max: <strong>&#8377;5 Crore+</strong> | Tenure: up to 30 years</li>
                                <li><strong style="color: #10b981;">Zero</strong> processing fee</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">&#127970;</span><h3>Loan Against Property (LAP)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #1e3a8a;">9.50% &ndash; 11.00% p.a.</strong></li>
                                <li>Max: <strong>&#8377;15 Crore</strong> | Tenure: 15 years</li>
                                <li><strong style="color: #10b981;">Zero</strong> processing fee</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">&#128092;</span><h3>Personal Loan (Solitaire)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #1e3a8a;">10.25% p.a.</strong></li>
                                <li>Up to <strong>&#8377;50 Lakh</strong> | Tenure: 5 years</li>
                                <li><strong style="color: #10b981;">Instant</strong> disbursal</li>
                            </ul>
                        </div>
                        <div class="feature-card" style="border-left: 4px solid #1e3a8a;">
                            <div class="feat-card-header"><span class="feat-icon">&#128202;</span><h3>Loan Against Securities (LASP)</h3></div>
                            <ul class="feat-list">
                                <li>Rate: <strong style="color: #1e3a8a;">9.00% &ndash; 10.50% p.a.</strong></li>
                                <li>Up to <strong>80% of portfolio value</strong></li>
                                <li>Pledge stocks, MFs &amp; bonds</li>
                            </ul>
                        </div>
                    </div>
                </div>'''

def update_dashboards():
    for filepath in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
        print(f"=== Restoring panel-assets summary in {filepath} ===")
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        # Replace panel-assets content with clean summary box
        panel_pattern = r'<div class="info-panel" id="panel-assets">.*?(?=<div class="info-panel" id="panel-investments">)'
        text = re.sub(panel_pattern, summary_panel_html + '\n\n', text, flags=re.DOTALL)

        # Fix any remaining ?? emoji glitches
        text = text.replace('??', '?')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Done restoring {filepath}")

update_dashboards()
