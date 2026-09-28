import os
import re

file_path = 'home_loan_calculator.html'

if not os.path.exists(file_path):
    print("File not found")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the calc-grid to align-items: start (required for sticky to work without stretching)
# and adjust the ratio slightly if desired, but 1fr 1fr is fine, maybe 1.2fr 1fr looks better.
old_grid = """        .calc-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            margin-bottom: 32px;
        }"""
        
new_grid = """        .calc-grid {
            display: grid;
            grid-template-columns: 1.3fr 1fr;
            gap: 28px;
            margin-bottom: 32px;
            align-items: start;
        }"""
        
content = content.replace(old_grid, new_grid)

# 2. Add sticky class to the right column
old_right = """<!-- Right Column: Live Savings Output -->
            <div class="calc-card">"""
new_right = """<!-- Right Column: Live Savings Output -->
            <div class="calc-card" style="position: sticky; top: 24px;">"""

content = content.replace(old_right, new_right)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated home_loan_calculator.html successfully!")
