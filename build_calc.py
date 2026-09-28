import os

file_path = 'home_loan_calculator.html'

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Bank - Solitaire Advanced RM Calculator</title>
    <!-- Google Fonts Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        html { font-size: 93%; }
        html, body {
            height: auto !important; min-height: 100% !important; overflow-x: hidden !important; overflow-y: auto !important;
            font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; margin: 0; padding: 0; line-height: 1.5;
        }
        .calc-container { max-width: 1200px; margin: 0 auto; padding: 24px 20px 60px; }
        .calc-header {
            display: flex; justify-content: space-between; align-items: center; background: #ffffff; padding: 16px 28px;
            border-radius: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.03); margin-bottom: 24px; border: 1px solid #e2e8f0;
        }
        .btn-back {
            display: inline-flex; align-items: center; gap: 8px; padding: 9px 18px; background: #f1f5f9; color: #1e3a8a;
            border: 1px solid #cbd5e1; border-radius: 8px; font-weight: 700; font-size: 0.85rem; text-decoration: none; transition: all 0.2s;
        }
        .btn-back:hover { background: #e2e8f0; color: #0f172a; }
        .hero-banner {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%); border-radius: 20px; padding: 28px 32px;
            color: white; position: relative; overflow: hidden; box-shadow: 0 12px 30px rgba(30, 58, 138, 0.2); margin-bottom: 24px;
        }
        .hero-badge {
            display: inline-flex; align-items: center; gap: 6px; background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(8px);
            padding: 4px 14px; border-radius: 16px; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 12px; border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Config Box */
        .config-box {
            background: #ffffff; border: 1.5px dashed #cbd5e1; border-radius: 16px; padding: 20px 24px; margin-bottom: 24px;
        }
        .config-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-top: 12px; }
        .config-item { display: flex; flex-direction: column; gap: 4px; }
        .config-item label { font-size: 0.75rem; font-weight: 700; color: #475569; text-transform: uppercase; }
        .config-item input { padding: 8px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #0f172a; outline: none; }
        .config-item input:focus { border-color: #1e3a8a; }

        /* Calculator Grid */
        .calc-grid { display: grid; grid-template-columns: 1.25fr 1fr; gap: 28px; margin-bottom: 32px; align-items: start; }
        @media (max-width: 900px) { .calc-grid { grid-template-columns: 1fr; } }
        .calc-card { background: #ffffff; border-radius: 18px; padding: 28px; border: 1px solid #e2e8f0; box-shadow: 0 4px 16px rgba(0,0,0,0.02); }
        .card-title { font-size: 0.95rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
        
        /* Loan Type Tabs */
        .loan-tabs { display: flex; gap: 8px; margin-bottom: 24px; background: #f8fafc; padding: 6px; border-radius: 12px; border: 1px solid #e2e8f0; }
        .loan-tab { flex: 1; padding: 10px 0; border: none; background: transparent; border-radius: 8px; font-weight: 700; font-size: 0.82rem; color: #64748b; cursor: pointer; transition: all 0.2s; }
        .loan-tab.active { background: #1e3a8a; color: white; box-shadow: 0 2px 8px rgba(30,58,138,0.2); }

        /* Inputs */
        .input-group { margin-bottom: 24px; }
        .input-label-row { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 10px; }
        .input-label { font-size: 0.85rem; font-weight: 700; color: #334155; }
        .input-val-box { background: #f1f5f9; padding: 8px 12px; border-radius: 8px; border: 1px solid #cbd5e1; font-weight: 800; font-size: 1rem; color: #0f172a; text-align: right; min-width: 120px; display: flex; align-items: center; justify-content: space-between; }
        .input-val-box span { color: #64748b; font-size: 0.8rem; font-weight: 600; margin-right: 8px; }
        .input-val-box input { background: transparent; border: none; font-weight: 800; font-size: 1rem; color: #0f172a; text-align: right; width: 100%; outline: none; font-family: 'Inter', sans-serif; }
        
        /* Range Sliders */
        input[type=range] { -webkit-appearance: none; width: 100%; background: transparent; }
        input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; height: 20px; width: 20px; border-radius: 50%; background: #1e3a8a; cursor: pointer; margin-top: -8px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        input[type=range]::-webkit-slider-runnable-track { width: 100%; height: 6px; cursor: pointer; background: #e2e8f0; border-radius: 3px; }

        /* Output Formatting */
        .sticky-sidebar { position: sticky; top: 24px; }
        .output-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; margin-bottom: 16px; }
        .output-box.highlight { background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color: white; border: none; box-shadow: 0 8px 20px rgba(30,58,138,0.15); }
        .output-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
        .output-row:last-child { margin-bottom: 0; }
        .output-label { font-size: 0.8rem; font-weight: 600; color: #64748b; }
        .output-val { font-size: 1rem; font-weight: 800; color: #0f172a; }
        .highlight .output-label { color: #94a3b8; }
        .highlight .output-val { color: #ffffff; font-size: 1.15rem; }
        
        .hero-number { font-size: 2rem; font-weight: 900; color: #10b981; line-height: 1.1; margin: 8px 0; }
        .tag-pill { background: #d1fae5; color: #065f46; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; }

        .solitaire-benefit-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 0.8rem; }
        .solitaire-benefit-table th, .solitaire-benefit-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid #e2e8f0; }
        .solitaire-benefit-table th { font-weight: 800; color: #475569; background: #f1f5f9; }
        .solitaire-benefit-table td { font-weight: 600; color: #0f172a; }
        
        .big-net-benefit { text-align: center; background: #ecfdf5; border: 2px dashed #10b981; padding: 24px; border-radius: 16px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="calc-container">
        <!-- Header -->
        <header class="calc-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <svg width="36" height="36" viewBox="0 0 40 40" fill="none">
                    <circle cx="20" cy="20" r="18" fill="#1e3a8a"/>
                    <rect x="18.5" y="8" width="3" height="24" fill="#d61f26"/>
                    <path d="M13 15 C8 15 8 25 13 25 C18 25 22 15 27 15 C32 15 32 25 27 25 C22 25 18 15 13 15 Z" stroke="#ffffff" stroke-width="3" fill="none"/>
                </svg>
                <div>
                    <span style="font-weight: 900; font-size: 1.15rem; color: #1e3a8a;">Cloud Bank</span>
                    <span style="font-weight: 800; font-size: 1.15rem; color: #d61f26;"> Solitaire</span>
                </div>
            </div>
            <a href="javascript:history.back()" class="btn-back">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <line x1="19" y1="12" x2="5" y2="12"></line>
                    <polyline points="12 19 5 12 12 5"></polyline>
                </svg>
                Back to Dashboard
            </a>
        </header>

        <!-- Hero Banner -->
        <section class="hero-banner">
            <div class="hero-badge">🏡 ADVANCED RM CALCULATOR</div>
            <h1 style="font-size: 1.6rem; font-weight: 900; margin: 0 0 5px 0; letter-spacing: -0.5px;">Solitaire Home Loan Analytics</h1>
            <p style="color: #cbd5e1; font-size: 0.9rem; margin: 0; max-width: 600px;">Pitch pure financial value. Dynamically compare New Loans, Balance Transfers, and Top-Ups to demonstrate the net benefit of Solitaire.</p>
        </section>
        
        <!-- Admin Config -->
        <div class="config-box">
            <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="document.getElementById('config-body').style.display = document.getElementById('config-body').style.display === 'none' ? 'block' : 'none'">
                <h3 style="margin: 0; font-size: 0.9rem; font-weight: 800; color: #1e3a8a; display: flex; align-items: center; gap: 8px;">⚙️ Master Configuration (Click to Expand)</h3>
            </div>
            <div id="config-body" style="display: block;">
                <div class="config-grid">
                    <div class="config-item"><label>Standard Market Rate (%)</label><input type="number" id="cfg-market-rate" value="7.80" step="0.05" oninput="calculate()"></div>
                    <div class="config-item"><label>Solitaire Rate (%)</label><input type="number" id="cfg-sol-rate" value="7.50" step="0.05" oninput="calculate()"></div>
                    <div class="config-item"><label>Existing Bank Proc. Fee (₹)</label><input type="number" id="cfg-market-pf" value="50000" step="1000" oninput="calculate()"></div>
                    <div class="config-item"><label>Kotak Processing Fee (₹)</label><input type="number" id="cfg-sol-pf" value="0" step="1000" oninput="calculate()"></div>
                    <div class="config-item"><label>Other BT Costs (₹)</label><input type="number" id="cfg-bt-costs" value="10000" step="500" oninput="calculate()"></div>
                </div>
            </div>
        </div>

        <div class="calc-grid">
            <!-- LEFT COLUMN: INPUTS -->
            <div class="calc-card">
                <div class="card-title"><span>📝</span> Scenario Inputs</div>
                
                <div class="loan-tabs">
                    <button class="loan-tab active" onclick="setMode('new', this)">New Home Loan</button>
                    <button class="loan-tab" onclick="setMode('bt', this)">Balance Transfer</button>
                    <button class="loan-tab" onclick="setMode('topup', this)">Top-Up</button>
                    <button class="loan-tab" onclick="setMode('bttopup', this)">BT + Top-Up</button>
                </div>

                <div id="inputs-container">
                    <!-- Inputs injected by JS based on mode -->
                </div>
            </div>

            <!-- RIGHT COLUMN: OUTPUTS -->
            <div class="calc-card sticky-sidebar">
                <div class="card-title"><span>📊</span> Pitch & Financial Benefit</div>
                <div id="outputs-container">
                    <!-- Outputs injected by JS based on mode -->
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentMode = 'new';
        
        function formatCrL(val) {
            if (val >= 10000000) return (val / 10000000).toFixed(2) + ' Cr';
            if (val >= 100000) return (val / 100000).toFixed(2) + ' L';
            return val.toLocaleString('en-IN');
        }

        function setMode(mode, btn) {
            currentMode = mode;
            document.querySelectorAll('.loan-tab').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderInputs();
            calculate();
        }

        // The HTML generation for the left panel inputs
        function renderInputs() {
            const container = document.getElementById('inputs-container');
            let html = '';

            // Common Property Value
            html += `
                <div class="input-group">
                    <div class="input-label-row">
                        <label class="input-label">Property Value (₹)</label>
                        <div class="input-val-box"><span>₹</span><input type="number" id="in-prop-val" value="29000000" oninput="calculate()"></div>
                    </div>
                    <div style="font-size:0.75rem; color:#64748b; text-align:right;" id="in-prop-val-txt">2.90 Cr</div>
                </div>
            `;

            if (currentMode === 'new') {
                html += `
                    <div class="input-group">
                        <div class="input-label-row">
                            <label class="input-label">Down Payment (₹)</label>
                            <div class="input-val-box"><span>₹</span><input type="number" id="in-dp-val" value="3770000" oninput="calculate()"></div>
                        </div>
                        <div style="font-size:0.75rem; color:#64748b; text-align:right;" id="in-dp-val-txt">13.00% / 37.70 L</div>
                    </div>
                    <div class="input-group">
                        <div class="input-label-row">
                            <label class="input-label">Loan Tenure (Years)</label>
                            <div class="input-val-box"><span>Yrs</span><input type="number" id="in-tenure" value="20" oninput="calculate()"></div>
                        </div>
                    </div>
                `;
            }

            if (currentMode === 'bt' || currentMode === 'topup' || currentMode === 'bttopup') {
                html += `
                    <div class="input-group">
                        <div class="input-label-row">
                            <label class="input-label">Current Outstanding Loan (₹)</label>
                            <div class="input-val-box"><span>₹</span><input type="number" id="in-cur-os" value="25200000" oninput="calculate()"></div>
                        </div>
                        <div style="font-size:0.75rem; color:#64748b; text-align:right;" id="in-cur-os-txt">2.52 Cr</div>
                    </div>
                    <div class="input-group">
                        <div class="input-label-row">
                            <label class="input-label">Current Interest Rate (%)</label>
                            <div class="input-val-box"><span>%</span><input type="number" id="in-cur-rate" value="7.80" step="0.05" oninput="calculate()"></div>
                        </div>
                    </div>
                    <div class="input-group">
                        <div class="input-label-row">
                            <label class="input-label">Remaining Tenure (Years)</label>
                            <div class="input-val-box"><span>Yrs</span><input type="number" id="in-cur-tenure" value="20" oninput="calculate()"></div>
                        </div>
                    </div>
                `;
            }

            if (currentMode === 'topup' || currentMode === 'bttopup') {
                html += `
                    <div class="input-group" style="background:#eff6ff; padding:16px; border-radius:12px; border:1px solid #bfdbfe;">
                        <div class="input-label-row">
                            <label class="input-label" style="color:#1e3a8a;">Top-Up Amount Required (₹)</label>
                            <div class="input-val-box" style="background:white;"><span>₹</span><input type="number" id="in-topup-req" value="3000000" oninput="calculate()"></div>
                        </div>
                        <div style="font-size:0.75rem; color:#1e3a8a; font-weight:600; text-align:right;" id="in-topup-req-txt">30.00 L</div>
                    </div>
                `;
            }
            
            // All BT / Topup have a Kotak New Tenure field
            if (currentMode === 'bt' || currentMode === 'bttopup') {
                 html += `
                    <div class="input-group">
                        <div class="input-label-row">
                            <label class="input-label">New Kotak Tenure (Years)</label>
                            <div class="input-val-box"><span>Yrs</span><input type="number" id="in-new-tenure" value="20" oninput="calculate()"></div>
                        </div>
                    </div>
                `;
            }

            container.innerHTML = html;
        }

        function calculateEMI(p, r_annual_pct, years) {
            const r = r_annual_pct / 100 / 12;
            const n = years * 12;
            if(r === 0) return p / n;
            return p * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
        }

        function calculate() {
            // Get Configs
            const marketRate = parseFloat(document.getElementById('cfg-market-rate').value) || 0;
            const solRate = parseFloat(document.getElementById('cfg-sol-rate').value) || 0;
            const pfMarket = parseFloat(document.getElementById('cfg-market-pf').value) || 0;
            const pfSol = parseFloat(document.getElementById('cfg-sol-pf').value) || 0;
            const btCosts = parseFloat(document.getElementById('cfg-bt-costs').value) || 0;

            const propVal = parseFloat(document.getElementById('in-prop-val')?.value) || 0;
            if(document.getElementById('in-prop-val-txt')) document.getElementById('in-prop-val-txt').innerText = formatCrL(propVal);

            let outHTML = '';

            if (currentMode === 'new') {
                const dpVal = parseFloat(document.getElementById('in-dp-val').value) || 0;
                const tenure = parseInt(document.getElementById('in-tenure').value) || 0;
                
                const dpPct = (dpVal / propVal * 100).toFixed(2);
                if(document.getElementById('in-dp-val-txt')) document.getElementById('in-dp-val-txt').innerText = dpPct + '% / ' + formatCrL(dpVal);

                const loanAmount = propVal - dpVal;
                const ltv = ((loanAmount / propVal) * 100).toFixed(1);

                const emiMarket = calculateEMI(loanAmount, marketRate, tenure);
                const emiSol = calculateEMI(loanAmount, solRate, tenure);

                const monthlySave = emiMarket - emiSol;
                const intMarket = (emiMarket * tenure * 12) - loanAmount;
                const intSol = (emiSol * tenure * 12) - loanAmount;
                const intSave = intMarket - intSol;
                const pfSave = pfMarket - pfSol;
                const netBenefit = intSave + pfSave;

                outHTML = `
                    <div class="output-box" style="display:flex; justify-content:space-between; align-items:center; background:#fefce8; border-color:#fef08a;">
                        <span class="output-label" style="color:#a16207;">Loan Amount required</span>
                        <span class="output-val" style="color:#854d0e; font-size:1.2rem;">₹ ${formatCrL(loanAmount)}</span>
                    </div>
                    <div style="font-size:0.75rem; color:#64748b; text-align:right; margin-top:-10px; margin-bottom:16px;">Loan-to-Value (LTV): <strong>${ltv}%</strong></div>

                    <div class="output-box">
                        <div class="output-row">
                            <span class="output-label">Standard Market Rate (${marketRate}%)</span>
                            <span class="output-val" style="color:#ef4444;">₹ ${Math.round(emiMarket).toLocaleString('en-IN')}</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">Kotak Solitaire Rate (${solRate}%)</span>
                            <span class="output-val" style="color:#10b981;">₹ ${Math.round(emiSol).toLocaleString('en-IN')}</span>
                        </div>
                    </div>

                    <div class="output-box highlight">
                        <div style="font-size:0.8rem; font-weight:700; text-transform:uppercase; color:#6ee7b7;">Solitaire Advantage</div>
                        <div class="hero-number">₹ ${Math.round(monthlySave).toLocaleString('en-IN')} <span style="font-size:1rem; font-weight:600; color:#cbd5e1;">/ mo lower EMI</span></div>
                        <div class="output-row" style="margin-top:16px;">
                            <span class="output-label">Total Interest Saving</span>
                            <span class="output-val">₹ ${formatCrL(intSave)}</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">Processing Fee Saving</span>
                            <span class="output-val">₹ ${Math.round(pfSave).toLocaleString('en-IN')}</span>
                        </div>
                    </div>
                    
                    <div class="big-net-benefit">
                        <div style="font-size:0.85rem; font-weight:800; color:#065f46; text-transform:uppercase;">Total Financial Benefit</div>
                        <div style="font-size:2.2rem; font-weight:900; color:#059669; line-height:1.2;">₹ ${formatCrL(netBenefit)}</div>
                    </div>
                `;
            } 
            else if (currentMode === 'bt') {
                const curOs = parseFloat(document.getElementById('in-cur-os').value) || 0;
                if(document.getElementById('in-cur-os-txt')) document.getElementById('in-cur-os-txt').innerText = formatCrL(curOs);
                const curRate = parseFloat(document.getElementById('in-cur-rate').value) || 0;
                const remTenure = parseInt(document.getElementById('in-cur-tenure').value) || 0;
                const newTenure = parseInt(document.getElementById('in-new-tenure').value) || 0;

                const ltv = ((curOs / propVal) * 100).toFixed(1);
                
                // Max 80% LTV available topup
                const maxLoan = propVal * 0.8;
                const availTopup = Math.max(0, maxLoan - curOs);

                const emiCur = calculateEMI(curOs, curRate, remTenure);
                const emiSol = calculateEMI(curOs, solRate, newTenure);

                const monthlySave = emiCur - emiSol;
                const intCur = (emiCur * remTenure * 12) - curOs;
                const intSol = (emiSol * newTenure * 12) - curOs;
                const intSave = intCur - intSol;
                
                const pfSave = pfMarket - pfSol;
                const netBenefit = intSave + pfSave - btCosts;
                
                const breakEvenMonths = (btCosts / (monthlySave > 0 ? monthlySave : 1)).toFixed(1);

                outHTML = `
                    <div style="display:flex; justify-content:space-between; font-size:0.8rem; color:#64748b; margin-bottom:16px;">
                        <span>Current LTV: <strong>${ltv}%</strong></span>
                        <span style="color:#0284c7; font-weight:700;">Indicative Top-Up Available: ₹ ${formatCrL(availTopup)}</span>
                    </div>

                    <div class="output-box" style="border-left: 4px solid #ef4444;">
                        <div style="font-size:0.75rem; font-weight:800; color:#ef4444; margin-bottom:8px;">CURRENT BANK</div>
                        <div class="output-row">
                            <span class="output-label">Outstanding</span>
                            <span class="output-val">₹ ${formatCrL(curOs)}</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">Rate / EMI</span>
                            <span class="output-val">${curRate}% / ₹ ${Math.round(emiCur).toLocaleString('en-IN')}</span>
                        </div>
                    </div>

                    <div class="output-box highlight" style="border-left: 4px solid #10b981;">
                        <div style="font-size:0.75rem; font-weight:800; color:#6ee7b7; margin-bottom:8px;">KOTAK SOLITAIRE</div>
                        <div class="output-row">
                            <span class="output-label">New Rate / EMI</span>
                            <span class="output-val">${solRate}% / ₹ ${Math.round(emiSol).toLocaleString('en-IN')}</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">Monthly EMI Saving</span>
                            <span class="output-val" style="color:#a7f3d0;">₹ ${Math.round(monthlySave).toLocaleString('en-IN')}</span>
                        </div>
                    </div>
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="output-box" style="text-align:center;">
                            <div style="font-size:0.7rem; font-weight:700; color:#64748b; text-transform:uppercase;">Break-Even Period</div>
                            <div style="font-size:1.4rem; font-weight:800; color:#0f172a;">${breakEvenMonths} mo</div>
                        </div>
                        <div class="output-box" style="text-align:center;">
                            <div style="font-size:0.7rem; font-weight:700; color:#64748b; text-transform:uppercase;">Total Interest Saved</div>
                            <div style="font-size:1.4rem; font-weight:800; color:#0f172a;">₹ ${formatCrL(intSave)}</div>
                        </div>
                    </div>

                    <div class="big-net-benefit">
                        <div style="font-size:0.85rem; font-weight:800; color:#065f46; text-transform:uppercase;">Net Financial Benefit</div>
                        <div style="font-size:0.75rem; color:#059669; margin-top:4px;">Interest Saved + Proc Fee Saved - BT Costs</div>
                        <div style="font-size:2.2rem; font-weight:900; color:#059669; line-height:1.2; margin-top:8px;">₹ ${formatCrL(netBenefit)}</div>
                    </div>
                `;
            }
            else if (currentMode === 'bttopup' || currentMode === 'topup') {
                const curOs = parseFloat(document.getElementById('in-cur-os').value) || 0;
                if(document.getElementById('in-cur-os-txt')) document.getElementById('in-cur-os-txt').innerText = formatCrL(curOs);
                const curRate = parseFloat(document.getElementById('in-cur-rate').value) || 0;
                const remTenure = parseInt(document.getElementById('in-cur-tenure').value) || 0;
                
                const topupReq = parseFloat(document.getElementById('in-topup-req').value) || 0;
                if(document.getElementById('in-topup-req-txt')) document.getElementById('in-topup-req-txt').innerText = formatCrL(topupReq);
                
                const newTenure = currentMode === 'bttopup' ? (parseInt(document.getElementById('in-new-tenure').value) || 0) : remTenure;

                const combinedExposure = curOs + topupReq;
                const ltv = ((combinedExposure / propVal) * 100).toFixed(1);

                const emiCur = calculateEMI(curOs, curRate, remTenure);
                const emiBT = calculateEMI(curOs, solRate, newTenure); // Just the BT portion
                const emiCombined = calculateEMI(combinedExposure, solRate, newTenure);

                outHTML = `
                    <div style="display:flex; justify-content:space-between; font-size:0.8rem; color:#64748b; margin-bottom:16px;">
                        <span>New Combined LTV: <strong>${ltv}%</strong></span>
                    </div>

                    <div class="output-box" style="border-left: 4px solid #ef4444;">
                        <div style="font-size:0.75rem; font-weight:800; color:#ef4444; margin-bottom:8px;">CURRENT BANK (WITHOUT TOP-UP)</div>
                        <div class="output-row">
                            <span class="output-label">Outstanding</span>
                            <span class="output-val">₹ ${formatCrL(curOs)}</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">Rate / EMI</span>
                            <span class="output-val">${curRate}% / ₹ ${Math.round(emiCur).toLocaleString('en-IN')}</span>
                        </div>
                    </div>

                    <div class="output-box" style="border-left: 4px solid #3b82f6;">
                        <div style="font-size:0.75rem; font-weight:800; color:#3b82f6; margin-bottom:8px;">KOTAK BT ONLY SCENARIO</div>
                        <div class="output-row">
                            <span class="output-label">Loan / Rate</span>
                            <span class="output-val">₹ ${formatCrL(curOs)} / ${solRate}%</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">Monthly EMI</span>
                            <span class="output-val">₹ ${Math.round(emiBT).toLocaleString('en-IN')}</span>
                        </div>
                    </div>

                    <div class="output-box highlight" style="border-left: 4px solid #10b981; background:linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);">
                        <div style="font-size:0.75rem; font-weight:800; color:#6ee7b7; margin-bottom:8px;">KOTAK BT + TOP-UP SCENARIO</div>
                        <div class="output-row">
                            <span class="output-label">Combined Loan</span>
                            <span class="output-val">₹ ${formatCrL(combinedExposure)}</span>
                        </div>
                        <div class="output-row">
                            <span class="output-label">New Combined EMI</span>
                            <span class="output-val">₹ ${Math.round(emiCombined).toLocaleString('en-IN')}</span>
                        </div>
                        <div style="margin-top:16px; background:rgba(255,255,255,0.1); padding:12px; border-radius:8px; font-weight:700; font-size:1.05rem; text-align:center; color:#fff;">
                            "Get ₹ ${formatCrL(topupReq)} additional liquidity while keeping your EMI at ₹ ${Math.round(emiCombined).toLocaleString('en-IN')}."
                        </div>
                    </div>
                `;
            }

            // Append Solitaire Value Section
            outHTML += `
                <div style="margin-top: 32px; border-top: 1px solid #e2e8f0; padding-top: 24px;">
                    <div style="font-size: 0.95rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;">💎 PLUS YOUR SOLITAIRE BENEFITS</div>
                    <table class="solitaire-benefit-table">
                        <thead>
                            <tr><th>Benefit</th><th style="text-align:right;">Potential Value</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Processing fee saving</td><td style="text-align:right;">₹ ${Math.round(pfMarket - pfSol).toLocaleString('en-IN')}</td></tr>
                            <tr><td>District / Solitaire Table</td><td style="text-align:right; color:#059669;">Up to ₹ 1.20L/year*</td></tr>
                            <tr><td>Credit-card travel benefits</td><td style="text-align:right; font-weight:500;">Usage dependent</td></tr>
                            <tr><td>0% forex markup</td><td style="text-align:right; font-weight:500;">Usage dependent</td></tr>
                            <tr><td>Unlimited lounge & Concierge</td><td style="text-align:right; font-weight:500;">Service benefit</td></tr>
                        </tbody>
                    </table>
                </div>
            `;

            document.getElementById('outputs-container').innerHTML = outHTML;
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            renderInputs();
            calculate();
        });
    </script>
</body>
</html>"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {file_path} successfully!")
