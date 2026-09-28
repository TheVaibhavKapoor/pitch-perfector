import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reliability 2.0 - Customer Dashboard</title>
    <style>
        :root {
            --kotak-red: #ef4444;
            --kotak-dark-blue: #1e3a8a;
            --kotak-darker-blue: #172554;
            --bg-color: #f3f4f6; /* light gray/beige */
            --card-bg: #e5e7eb;
            --text-dark: #1f2937;
            --text-light: #f8fafc;
        }

        * {
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-dark);
        }

        /* Header */
        .header {
            background: white;
            display: flex;
            align-items: center;
            padding: 10px 20px;
            border-bottom: 1px solid #d1d5db;
        }
        
        .header-logo {
            color: var(--kotak-red);
            font-weight: 800;
            font-size: 1.2rem;
            margin-right: 40px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header-tabs {
            display: flex;
            gap: 24px;
            flex: 1;
        }

        .header-tab {
            color: #4b5563;
            font-weight: 600;
            font-size: 0.9rem;
            text-decoration: none;
            padding-bottom: 4px;
        }
        .header-tab.active {
            color: var(--kotak-dark-blue);
            border-bottom: 3px solid var(--kotak-dark-blue);
        }

        .header-right {
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 0.85rem;
        }

        .search-bar {
            padding: 8px 12px 10px 20px;
            background: white;
            border-bottom: 1px solid #d1d5db;
            display: flex;
            gap: 12px;
        }
        
        .search-input {
            padding: 6px 12px;
            border: 1px solid #9ca3af;
            border-radius: 4px;
            width: 250px;
        }
        
        .search-btn {
            background: var(--kotak-dark-blue);
            color: white;
            border: none;
            padding: 6px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
        }

        /* Layout */
        .container {
            display: grid;
            grid-template-columns: 380px 1fr;
            gap: 20px;
            padding: 20px;
        }

        /* Left Panel */
        .left-panel {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .customer-card {
            background: var(--kotak-dark-blue);
            color: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .customer-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding-bottom: 12px;
        }
        .customer-icon {
            width: 40px;
            height: 40px;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .customer-name {
            font-size: 1.4rem;
            font-weight: 700;
        }

        .details-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px 12px;
        }
        
        .detail-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .detail-label {
            color: #93c5fd;
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .detail-value {
            font-size: 0.85rem;
            font-weight: 600;
        }
        
        .rm-card {
            background: var(--bg-color);
            border: 1px solid #d1d5db;
            border-radius: 12px;
            padding: 16px;
        }
        .rm-card-header {
            font-weight: 700;
            color: var(--kotak-dark-blue);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .rm-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }

        /* Right Panel */
        .right-panel {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .section-header {
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .cards-row {
            display: flex;
            gap: 16px;
            margin-bottom: 16px;
        }

        .data-card {
            background: var(--card-bg);
            border: 1px solid #d1d5db;
            border-radius: 8px;
            padding: 12px 16px;
            flex: 1;
        }
        
        .data-card.highlight {
            background: #e0e7ff;
            border-color: #a5b4fc;
        }
        
        .data-label {
            font-size: 0.75rem;
            color: #4b5563;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .data-value {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-dark);
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 16px;
        }

        .product-holdings {
            background: var(--card-bg);
            border: 1px solid #d1d5db;
            border-radius: 8px;
            padding: 12px 16px;
        }
        .holdings-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 8px;
        }
        .tag {
            background: white;
            border: 1px solid #d1d5db;
            padding: 4px 10px;
            border-radius: 16px;
            font-size: 0.7rem;
            font-weight: 600;
            color: #4b5563;
        }

        .loans-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }

        /* Charts Section */
        .charts-section {
            background: var(--bg-color);
            margin-top: 20px;
        }
        .chart-tabs {
            display: flex;
            gap: 16px;
            border-bottom: 1px solid #d1d5db;
            margin-bottom: 20px;
            padding-bottom: 8px;
            overflow-x: auto;
        }
        .chart-tab {
            font-size: 0.8rem;
            font-weight: 600;
            color: #4b5563;
            cursor: pointer;
        }
        .chart-tab.active {
            color: var(--kotak-dark-blue);
        }
        
        .donuts-row {
            display: flex;
            justify-content: space-around;
            padding: 20px;
        }
        .donut-container {
            text-align: center;
        }
        .donut-title {
            font-weight: 700;
            font-size: 0.9rem;
            margin-bottom: 16px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 6px;
        }
        .donut {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            margin: 0 auto;
            position: relative;
        }
        .donut::after {
            content: '';
            position: absolute;
            top: 25px; left: 25px; right: 25px; bottom: 25px;
            background: var(--bg-color);
            border-radius: 50%;
        }
        
        /* Cues Table Section */
        .bottom-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #e5e7eb;
        }
        
        .line-chart-placeholder {
            background: var(--bg-color);
            border: 1px solid #d1d5db;
            height: 200px;
            border-radius: 8px;
            position: relative;
            margin-bottom: 20px;
            overflow: hidden;
        }
        .line-chart-placeholder svg {
            width: 100%;
            height: 100%;
        }
        
        .cues-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.8rem;
        }
        .cues-table th, .cues-table td {
            border: 1px solid #d1d5db;
            padding: 10px;
            text-align: left;
        }
        .cues-table th {
            background: #e5e7eb;
            font-weight: 600;
            color: #4b5563;
        }
        .btn-pitched {
            background: #dcfce7;
            color: #166534;
            border: 1px solid #bbf7d0;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 600;
            margin-right: 4px;
        }
        .btn-not-pitched {
            background: #fee2e2;
            color: #991b1b;
            border: 1px solid #fecaca;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 600;
        }
    </style>
</head>
<body>

    <!-- Header -->
    <div class="header">
        <div class="header-logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/>
            </svg>
            kotak
        </div>
        <div style="font-weight: 600; font-size: 0.9rem; margin-right: 30px; color: #4b5563;">Reliability 2.0</div>
        
        <div class="header-tabs">
            <a href="#" class="header-tab active">Customer One View</a>
            <a href="#" class="header-tab">Reports</a>
            <a href="#" class="header-tab">Customer Case Summary</a>
        </div>
        
        <div class="header-right">
            <span style="color: #ef4444; font-weight: 600;">Help &#9432;</span>
            <span style="color: #4b5563;">Hello, Vaibhav K (Consumer Bank, KMBL) &#9662;</span>
            <div style="background: #e5e7eb; padding: 4px 10px; border-radius: 4px; font-size: 0.7rem; text-align: center;">
                <div>Data available as of:</div>
                <div style="font-weight: 700;">11th Aug'26</div>
            </div>
        </div>
    </div>
    
    <div class="search-bar">
        <input type="text" value="277849512" class="search-input">
        <button class="search-btn">Search</button>
    </div>

    <!-- Main Container -->
    <div class="container">
        
        <!-- Left Panel -->
        <div class="left-panel">
            
            <div class="customer-card">
                <div class="customer-header">
                    <div class="customer-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"></circle><path d="M20 21a8 8 0 0 0-16 0"></path></svg>
                    </div>
                    <div class="customer-name">Aritri Singh</div>
                </div>
                
                <div class="details-grid">
                    <div class="detail-item">
                        <div class="detail-label">&#128197; Date of Birth</div>
                        <div class="detail-value">17-09-1989</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#128101; Family ID</div>
                        <div class="detail-value">277849512</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#127960; City</div>
                        <div class="detail-value">Mumbai</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#128197; CRN Creation Date</div>
                        <div class="detail-value">10-06-2018</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#127970; Branch</div>
                        <div class="detail-value">631</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#127970; Branch Name</div>
                        <div class="detail-value">Mumbai - Santacruz (E), - Kalina Ings Point</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#128100; Customer Classification</div>
                        <div class="detail-value">K_ASA</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#9733; Affluent Customer</div>
                        <div class="detail-value">Yes</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#10003; KYC Compliant</div>
                        <div class="detail-value">Yes</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#128100; Customer Persona</div>
                        <div class="detail-value">SALARIED FEMALE ADULT(>30)</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#9888; Risk Profile</div>
                        <div class="detail-value">HIGH</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#128100; Customer Type</div>
                        <div class="detail-value">KEY</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">&#128203; Customer LOB</div>
                        <div class="detail-value">51</div>
                    </div>
                </div>
            </div>
            
            <div class="rm-card">
                <div class="rm-card-header">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"></circle><path d="M20 21a8 8 0 0 0-16 0"></path></svg>
                    Customer RM Details
                </div>
                <div class="rm-grid">
                    <div class="detail-item">
                        <div class="detail-label" style="color:#6b7280;">Relationship Manager</div>
                        <div class="detail-value" style="color:var(--text-dark); font-size:0.8rem;">Vaibhav Kapoor</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label" style="color:#6b7280;">Associate RM</div>
                        <div class="detail-value" style="color:var(--text-dark); font-size:0.8rem;">Dilip Magan Rathod</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label" style="color:#6b7280;">VRM-Affluent</div>
                        <div class="detail-value" style="color:var(--text-dark); font-size:0.8rem;">Aniket Surendra Karkera</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label" style="color:#6b7280;">WC Relationship Manager</div>
                        <div class="detail-value" style="color:var(--text-dark); font-size:0.8rem;">-</div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Right Panel -->
        <div class="right-panel">
            
            <!-- Relationship Details -->
            <div>
                <div class="section-header">&#129309; Relationship Details</div>
                
                <div class="cards-row" style="margin-left: 40px;">
                    <div class="data-card highlight">
                        <div class="data-label">&#128100; Customer RV</div>
                        <div class="data-value">&#8377;9,91,04,773</div>
                        <div style="font-size:0.65rem; color:#4b5563; text-align:center; background:white; padding:2px; margin-top:6px; border-radius:4px; border:1px solid #d1d5db;">See details</div>
                    </div>
                    <div class="data-card highlight">
                        <div class="data-label">&#128101; Family RV</div>
                        <div class="data-value">&#8377;9,91,04,773</div>
                        <div style="font-size:0.65rem; color:#4b5563; text-align:center; background:white; padding:2px; margin-top:6px; border-radius:4px; border:1px solid #d1d5db;">See details</div>
                    </div>
                </div>

                <div class="metrics-grid">
                    <div class="data-card">
                        <div class="data-label">Indicative Affluence Index</div>
                        <div class="data-value" style="font-size:0.9rem;">A:Affluent</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Proposed Program</div>
                        <div class="data-value" style="font-size:0.9rem;">Solitaire</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Existing Program</div>
                        <div class="data-value" style="font-size:0.9rem;">Solitaire</div>
                    </div>
                    
                    <div class="data-card">
                        <div class="data-label">Avg.Salary:Last 3Mths</div>
                        <div class="data-value" style="font-size:0.9rem;">No Salary</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Customer Profitability</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;89</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Customer Value Score</div>
                        <div class="data-value" style="font-size:0.9rem;">6</div>
                    </div>

                    <div class="data-card">
                        <div class="data-label">MF Redemption Amt</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    <div class="data-card" style="grid-column: span 2;">
                        <div class="data-label">MF Purchase Amount</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;1,79,991</div>
                    </div>
                </div>

                <div class="product-holdings">
                    <div class="data-label">Product Holdings (8)</div>
                    <div class="holdings-tags">
                        <span class="tag">TD</span>
                        <span class="tag">Forex</span>
                        <span class="tag">SA</span>
                        <span class="tag">Trade</span>
                        <span class="tag">MF</span>
                        <span class="tag">CREDIT_CARD</span>
                        <span class="tag">Demat_tag</span>
                        <span class="tag">Trading_tag</span>
                        <span class="tag">Demat_Trading</span>
                    </div>
                </div>
            </div>

            <!-- Loan Off-Us Details -->
            <div style="margin-top: 10px;">
                <div class="section-header" style="justify-content: space-between;">
                    <span>&#127974; Loan Off-Us Details</span>
                    <span style="font-size:0.65rem; font-weight:normal; color:#6b7280;">Data refreshed monthly</span>
                </div>
                
                <div class="loans-grid">
                    <div class="data-card">
                        <div class="data-label">&#127968; Home Loan</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">&#128100; Personal Loan</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">&#128274; Secured Personal Loan</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">&#128188; Loan Against Property</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    
                    <div class="data-card">
                        <div class="data-label">&#128179; Credit Card Limit</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;1,94,000</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">&#127970; Business Loan</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">&#128200; MF Transactions</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">&#128202; Demat</div>
                        <div class="data-value" style="font-size:0.9rem;">&#8377;0</div>
                    </div>
                </div>
                <div style="text-align:right; font-size:0.75rem; color:#4b5563; font-weight:600; margin-top:8px;">
                    See all off-us products &rarr;
                </div>
            </div>

            <!-- Charts Section -->
            <div class="charts-section">
                <div class="chart-tabs">
                    <span class="chart-tab active">Overview</span>
                    <span class="chart-tab">CA</span>
                    <span class="chart-tab">SA</span>
                    <span class="chart-tab">TD</span>
                    <span class="chart-tab">Forex</span>
                    <span class="chart-tab">HL</span>
                    <span class="chart-tab">PL</span>
                    <span class="chart-tab">OD</span>
                    <span class="chart-tab">CC</span>
                    <span class="chart-tab">WC</span>
                    <span class="chart-tab">MF</span>
                    <span class="chart-tab">DEMAT</span>
                    <span class="chart-tab">Life Insurance</span>
                    <span class="chart-tab">General Insurance</span>
                </div>

                <div class="donuts-row">
                    <div class="donut-container">
                        <div class="donut-title">&#128176; Liabilities</div>
                        <div class="donut" style="background: conic-gradient(#b91c1c 0% 99%, var(--bg-color) 99% 100%);">
                            <span style="position:absolute; top:40%; left:15%; font-weight:bold; font-size:0.8rem; z-index:10;">99%</span>
                            <span style="position:absolute; top:40%; right:15%; font-weight:bold; font-size:0.8rem; z-index:10;">0%</span>
                        </div>
                    </div>
                    
                    <div class="donut-container">
                        <div class="donut-title">&#128176; Assets</div>
                        <div class="donut" style="background: #15803d;">
                            <span style="position:absolute; top:45%; left:35%; font-weight:bold; font-size:0.8rem; z-index:10; color:white;">100%</span>
                        </div>
                    </div>

                    <div class="donut-container">
                        <div class="donut-title">&#128200; Investments</div>
                        <div class="donut" style="background: conic-gradient(#1d4ed8 0% 66%, #3b82f6 66% 100%);">
                            <span style="position:absolute; top:25%; right:25%; font-weight:bold; font-size:0.75rem; z-index:10; color:white;">33%</span>
                            <span style="position:absolute; bottom:25%; left:30%; font-weight:bold; font-size:0.8rem; z-index:10; color:white;">66%</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Bottom Line Charts and Cues -->
            <div class="bottom-section">
                
                <!-- Line Charts -->
                <div>
                    <div class="chart-tabs" style="border:none; margin-bottom:10px;">
                        <span class="chart-tab active" style="font-weight:700; color:var(--text-dark); border-bottom: 2px solid var(--text-dark);">EOP</span>
                        <span class="chart-tab">AMB</span>
                        <span class="chart-tab">AQB</span>
                        <span class="chart-tab">RV</span>
                        <span class="chart-tab">Salary</span>
                    </div>
                    
                    <div style="font-size:0.85rem; font-weight:700; text-align:center; margin-bottom:8px;">Customer EOP Balance for last 7 days</div>
                    <div class="line-chart-placeholder">
                        <svg viewBox="0 0 400 200" preserveAspectRatio="none">
                            <polyline fill="none" stroke="#1e3a8a" stroke-width="2" points="0,150 50,80 100,50 150,50 200,50 250,50 300,50 350,140 400,200"/>
                            <!-- Grid lines -->
                            <line x1="0" y1="50" x2="400" y2="50" stroke="#d1d5db" stroke-dasharray="2,2"/>
                            <line x1="0" y1="100" x2="400" y2="100" stroke="#d1d5db" stroke-dasharray="2,2"/>
                            <line x1="0" y1="150" x2="400" y2="150" stroke="#d1d5db" stroke-dasharray="2,2"/>
                            
                            <!-- Text labels -->
                            <text x="5" y="55" font-size="10" fill="#6b7280">64.1K</text>
                            <text x="5" y="105" font-size="10" fill="#6b7280">40.0K</text>
                            <text x="5" y="155" font-size="10" fill="#6b7280">20.0K</text>
                            
                            <!-- X Axis labels -->
                            <text x="40" y="190" font-size="10" fill="#6b7280">D1</text>
                            <text x="90" y="190" font-size="10" fill="#6b7280">D2</text>
                            <text x="140" y="190" font-size="10" fill="#6b7280">D3</text>
                            <text x="190" y="190" font-size="10" fill="#6b7280">D4</text>
                            <text x="240" y="190" font-size="10" fill="#6b7280">D5</text>
                            <text x="290" y="190" font-size="10" fill="#6b7280">D6</text>
                            <text x="340" y="190" font-size="10" fill="#6b7280">D7</text>
                        </svg>
                    </div>

                    <div style="font-size:0.85rem; font-weight:700; text-align:center; margin-bottom:8px;">Family EOP Balance for last 7 days</div>
                    <div class="line-chart-placeholder">
                        <svg viewBox="0 0 400 200" preserveAspectRatio="none">
                            <polyline fill="none" stroke="#1e3a8a" stroke-width="2" points="0,170 50,100 100,70 150,65 200,65 250,70 300,75 350,150 400,200"/>
                            <!-- Grid lines -->
                            <line x1="0" y1="70" x2="400" y2="70" stroke="#d1d5db" stroke-dasharray="2,2"/>
                            <line x1="0" y1="120" x2="400" y2="120" stroke="#d1d5db" stroke-dasharray="2,2"/>
                            <line x1="0" y1="170" x2="400" y2="170" stroke="#d1d5db" stroke-dasharray="2,2"/>
                            
                            <!-- Text labels -->
                            <text x="5" y="75" font-size="10" fill="#6b7280">64.1K</text>
                            <text x="5" y="125" font-size="10" fill="#6b7280">40.0K</text>
                        </svg>
                    </div>
                </div>

                <!-- Offers & Cues -->
                <div>
                    <div class="section-header" style="font-size: 1.1rem;">&#128221; Offers</div>
                    <div style="font-weight: 700; margin-bottom: 12px; margin-top: 16px;">Cues</div>
                    
                    <div style="display:flex; justify-content:space-between; font-size:0.75rem; margin-bottom:12px;">
                        <div>
                            <strong>Key CRN:</strong> 277849512<br>
                            <strong>Name:</strong> Aritri Singh
                        </div>
                        <div style="display:flex; align-items:center; gap:8px;">
                            <span>Contact Type*:</span>
                            <select style="padding:2px 4px; border-radius:4px;"><option>- Select -</option></select>
                        </div>
                        <div style="display:flex; gap:12px;">
                            <span>&#128197; Last Contacted <span style="font-weight:600;">Contact not initiated</span></span>
                            <span>&#128101; Meeting Type <span style="font-weight:600;">NA</span></span>
                        </div>
                    </div>

                    <table class="cues-table">
                        <thead>
                            <tr>
                                <th>Product</th>
                                <th>Description</th>
                                <th>Status Update</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Information Cue</td>
                                <td>Information Cue: Customer persona - Global traveller (international traveller, spender, Fx remitter).</td>
                                <td style="text-align:center; color:#6b7280;">Information Only</td>
                            </tr>
                            <tr>
                                <td>Service - Activation</td>
                                <td>Activation Cue - Enable Autopay of CC bill</td>
                                <td>
                                    <button class="btn-pitched">&#128077; Pitched</button>
                                    <button class="btn-not-pitched">&#128078; Not Pitched</button>
                                </td>
                            </tr>
                            <tr>
                                <td>Kotak remit</td>
                                <td>Remit - offus remit active with value of Rs 989.4 lacs but not onus active. Pitch Kotak Remit</td>
                                <td>
                                    <button class="btn-pitched">&#128077; Pitched</button>
                                    <button class="btn-not-pitched">&#128078; Not Pitched</button>
                                </td>
                            </tr>
                            <tr>
                                <td>Car Loan</td>
                                <td>CL - Solitaire CL offer 100.0 lacs- Pitch CL.</td>
                                <td>
                                    <button class="btn-pitched">&#128077; Pitched</button>
                                    <button class="btn-not-pitched">&#128078; Not Pitched</button>
                                </td>
                            </tr>
                            <tr>
                                <td>Loan Against Property</td>
                                <td>LAP - Solitaire LAP offer 700.0 lacs- Pitch LAP.</td>
                                <td>
                                    <button class="btn-pitched">&#128077; Pitched</button>
                                    <button class="btn-not-pitched">&#128078; Not Pitched</button>
                                </td>
                            </tr>
                            <tr>
                                <td>Life Insurance</td>
                                <td>LI - Pitch Term plan.</td>
                                <td>
                                    <button class="btn-pitched">&#128077; Pitched</button>
                                    <button class="btn-not-pitched">&#128078; Not Pitched</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>

        </div>
    </div>
</body>
</html>
"""

with open("reliability.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated reliability.html")
