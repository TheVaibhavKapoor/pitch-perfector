import os
import re

file_path = 'customer_overview_solitaire.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the bank summary grid
pattern = r'<section class="bank-summary-grid".*?</section>'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find bank-summary-grid")
    exit(1)

new_html = """<section class="bank-summary-grid" style="margin-bottom: 24px; display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px;">
    <!-- Bank Accounts -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='#1e3a8a'" onmouseout="this.style.borderColor='#e2e8f0'">
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; margin-bottom: 4px; text-transform: uppercase;">Bank Accounts</div>
        <div style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">₹ 2.91L</div>
        <div style="background: #f1f5f9; color: #475569; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 6px; display: inline-block;">2 ACTIVE</div>
    </div>
    
    <!-- Deposits -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='#1e3a8a'" onmouseout="this.style.borderColor='#e2e8f0'">
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; margin-bottom: 4px; text-transform: uppercase;">Deposits</div>
        <div style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">₹ 31.60L</div>
        <div style="background: #f1f5f9; color: #475569; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 6px; display: inline-block;">10 ACTIVE</div>
    </div>

    <!-- Debit Cards -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='#1e3a8a'" onmouseout="this.style.borderColor='#e2e8f0'">
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; margin-bottom: 4px; text-transform: uppercase;">Debit Cards</div>
        <div style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">2 Cards</div>
        <div style="background: #f1f5f9; color: #475569; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 6px; display: inline-block;">2 OPEN</div>
    </div>

    <!-- Credit Cards -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='#1e3a8a'" onmouseout="this.style.borderColor='#e2e8f0'">
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; margin-bottom: 4px; text-transform: uppercase;">Credit Cards</div>
        <div style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">2 Cards</div>
        <div style="background: #f1f5f9; color: #475569; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 6px; display: inline-block;">2 ACTIVE</div>
    </div>

    <!-- Loans -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='#1e3a8a'" onmouseout="this.style.borderColor='#e2e8f0'">
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; margin-bottom: 4px; text-transform: uppercase;">Loans</div>
        <div style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">₹ 52.27L</div>
        <div style="background: #f1f5f9; color: #475569; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 6px; display: inline-block;">1 ACTIVE</div>
    </div>

    <!-- Investments -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='#1e3a8a'" onmouseout="this.style.borderColor='#e2e8f0'">
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; margin-bottom: 4px; text-transform: uppercase;">Investments</div>
        <div style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">₹ 18.45L</div>
        <div style="background: #f0fdf4; color: #15803d; font-size: 0.65rem; font-weight: 700; padding: 2px 6px; border-radius: 6px; display: inline-block;">3 ACTIVE SIPS</div>
    </div>
</section>"""

content = content[:match.start()] + new_html + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Consolidated summary boxes into 1 line.")
