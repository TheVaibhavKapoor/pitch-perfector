# 🗺️ Pitch Perfector : Solitaire - Complete Site Hierarchy & Page Map

This document establishes the **ground truth mapping** for all pages within the Pitch Perfector Solitaire portal. All development, updates, and navigation logic MUST follow this exact structure.

---

## 📐 Complete Navigation Hierarchy

```
PITCH PERFECTOR PORTAL
│
├── 1. HOME PAGE (`index.html`)
│     └── Primary Bank & Pitch Perfector Portal Entry
│
└── 2. PITCH PERFECTOR : SOLITAIRE (`solitaire.html`)
      │   └── Main Solitaire Wealth & Savings Program Overview Page
      │
      ├── 3. PITCH PERFECTOR : SOLITAIRE > HOME PAGE > CC (`solitaire_cc.html`)
      │     └── Pitch & Features for Solitaire Credit Cards (Metal Card, Airport Lounge, Golf, 5X Rewards)
      │
      ├── 4. PITCH PERFECTOR : SOLITAIRE > HOME PAGE > LOANS (`loan_against_property.html` / `home_loan_calculator.html`)
      │     └── Pitch & Rates for Solitaire Asset-Backed Loans & Home Loans (Featured HL 8.75%, LAP, LASP, Auto Loan)
      │
      └── 5. PITCH PERFECTOR : SOLITAIRE > EXPERIENCE (`experience_solitaire.html`)
            │   └── Solitaire Interactive Experience Hub & Customer Selection Page
            │
            ├── 6. PITCH PERFECTOR : SOLITAIRE > EXPERIENCE > NTB (`experience_solitaire_dashboard_new.html`)
            │     └── Interactive Dashboard for New To Bank (NTB) Customers
            │           ├── Individual & Business Segment Tabs
            │           ├── Debit Card Panel (Privileges, Cashbacks, Free ATM)
            │           ├── Credit Card Panel (Comparison Boxes, Solitaire Metal vs Signature)
            │           ├── Loans & Assets Panel (Featured Home Loan @ 8.75%, LAP, LASP, Personal, Auto)
            │           ├── Investment Suite Panel (SIP / SWP / Lumpsum Calculator with Bar Chart, Zero AMC)
            │           ├── Forex Panel (Multi-Currency, Zero Cross-Currency Mark-up)
            │           └── Other Privileges Panel (Concierge, Priority Service, Lockers, Events)
            │
            └── 7. PITCH PERFECTOR : SOLITAIRE > EXPERIENCE > EXISTING (`experience_solitaire_dashboard.html`)
                  └── Interactive Dashboard for Existing To Bank (ETB) Customers
                        ├── Individual & Business Segment Tabs
                        ├── Debit Card Panel (Comparison & Existing Customer Rates/Tables)
                        ├── Credit Card Panel (Comparison Boxes, Upgrade Benefits)
                        ├── Loans & Assets Panel (Featured Home Loan @ 8.75%, LAP, LASP, Personal, Auto)
                        ├── Investment Suite Panel (SIP / SWP / Lumpsum Calculator with Bar Chart, Zero AMC)
                        ├── Forex Panel (Multi-Currency, Corporate Salary Rates)
                        └── Other Privileges Panel (Concierge, Priority Service, Lockers, Events)
```

---

## 📄 File Mapping Table

| Section Name | File Name | Target Audience / Purpose | Key Features & Included Content |
| :--- | :--- | :--- | :--- |
| **1. HOME PAGE** | `index.html` | General Portal Entry | Main product navigation & program launcher |
| **2. SOLITAIRE OVERVIEW** | `solitaire.html` | Solitaire Program Pitch | Overall benefits, eligibility criteria, relationship tiers |
| **3. SOLITAIRE > CC** | `solitaire_cc.html` | Credit Card Prospects | Solitaire Credit Card pitch, metal card showcase, airport lounge, golf, rewards |
| **4. SOLITAIRE > LOANS** | `loan_against_property.html`<br>`home_loan_calculator.html` | Loan Seekers | Asset-backed loan pitch, Home Loan rate breakdown (8.75%), LAP, calculator |
| **5. SOLITAIRE > EXPERIENCE** | `experience_solitaire.html` | Selection Entry Point | Gateway to choose between New To Bank (NTB) or Existing Customer experience |
| **6. EXPERIENCE > NTB** | `experience_solitaire_dashboard_new.html` | New Customers (NTB) | Full 6-panel interactive dashboard (DC, CC, Loans, Investments + Calculators, Forex, Other) |
| **7. EXPERIENCE > EXISTING** | `experience_solitaire_dashboard.html` | Existing Customers (ETB) | Full 6-panel interactive dashboard with ETB comparison boxes and calculators |

---

## 🔒 Content Integrity Rules
1. **Never alter page paths or merge NTB/ETB dashboards**: `experience_solitaire_dashboard_new.html` and `experience_solitaire_dashboard.html` are distinct pages with customer-type specific panels.
2. **Investments Panel Standard**: Must contain the 3-in-1 Investment Return Calculator (SIP / SWP / Lumpsum) with interactive sliders and year-by-year SVG growth bar chart.
3. **Assets/Loans Panel Standard**: Must feature the prominent Home Loan Hero Card (8.75% p.a., Zero processing fee, 30-year max) followed by 4 distinct product rate cards (LAP, Personal Loan, LASP, Auto Loan).
4. **Credit Card Panel Standard**: Must contain comparison boxes detailing Solitaire Credit Card tiers and features.
