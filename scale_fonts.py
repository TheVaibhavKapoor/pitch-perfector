import os

file_path = 'home_loan_calculator.html'

if not os.path.exists(file_path):
    print("File not found")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the card-title slightly smaller
content = content.replace(
    ".card-title { font-size: 0.95rem; font-weight: 800;", 
    ".card-title { font-size: 0.85rem; font-weight: 800;"
)

# Output Box Padding
content = content.replace(
    ".output-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; margin-bottom: 16px; }",
    ".output-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 14px; margin-bottom: 12px; }"
)

# Output Row Labels and Vals
content = content.replace(
    ".output-label { font-size: 0.8rem; font-weight: 600; color: #64748b; }",
    ".output-label { font-size: 0.72rem; font-weight: 600; color: #64748b; }"
)
content = content.replace(
    ".output-val { font-size: 1rem; font-weight: 800; color: #0f172a; }",
    ".output-val { font-size: 0.9rem; font-weight: 800; color: #0f172a; }"
)
content = content.replace(
    ".highlight .output-val { color: #ffffff; font-size: 1.15rem; }",
    ".highlight .output-val { color: #ffffff; font-size: 1.05rem; }"
)

# Hero Number
content = content.replace(
    ".hero-number { font-size: 2rem; font-weight: 900; color: #10b981; line-height: 1.1; margin: 8px 0; }",
    ".hero-number { font-size: 1.6rem; font-weight: 900; color: #10b981; line-height: 1.1; margin: 6px 0; }"
)
content = content.replace(
    '<span style="font-size:1rem; font-weight:600; color:#cbd5e1;">/ mo lower EMI</span>',
    '<span style="font-size:0.85rem; font-weight:600; color:#cbd5e1;">/ mo lower EMI</span>'
)

# Big Net Benefit
content = content.replace(
    ".big-net-benefit { text-align: center; background: #ecfdf5; border: 2px dashed #10b981; padding: 24px; border-radius: 16px; margin-top: 20px; }",
    ".big-net-benefit { text-align: center; background: #ecfdf5; border: 2px dashed #10b981; padding: 16px; border-radius: 16px; margin-top: 14px; }"
)
content = content.replace(
    'font-size:2.2rem; font-weight:900; color:#059669;',
    'font-size:1.8rem; font-weight:900; color:#059669;'
)

# Solitaire Benefit Table
content = content.replace(
    ".solitaire-benefit-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 0.8rem; }",
    ".solitaire-benefit-table { width: 100%; border-collapse: collapse; margin-top: 14px; font-size: 0.72rem; }"
)
content = content.replace(
    ".solitaire-benefit-table th, .solitaire-benefit-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid #e2e8f0; }",
    ".solitaire-benefit-table th, .solitaire-benefit-table td { padding: 8px 10px; text-align: left; border-bottom: 1px solid #e2e8f0; }"
)
content = content.replace(
    'font-size: 0.95rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;',
    'font-size: 0.85rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px;'
)
content = content.replace(
    'margin-top: 32px; border-top: 1px solid #e2e8f0; padding-top: 24px;',
    'margin-top: 20px; border-top: 1px solid #e2e8f0; padding-top: 16px;'
)

# Break even and total interest grid numbers
content = content.replace(
    'font-size:1.4rem; font-weight:800; color:#0f172a;',
    'font-size:1.15rem; font-weight:800; color:#0f172a;'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fonts scaled down successfully!")
