import os
import re

file_path = 'customer_overview_solitaire.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<section class="bank-summary-grid".*?</section>'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find bank-summary-grid")
    exit(1)

new_html = """<section class="bank-summary-grid" style="margin-bottom: 24px;">
    <div style="background: #0f172a; color: white; border-radius: 8px; overflow: hidden; display: flex; align-items: stretch; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <div style="background: #d61f26; padding: 10px 16px; font-weight: 800; font-size: 0.75rem; letter-spacing: 0.5px; text-transform: uppercase; white-space: nowrap; display: flex; align-items: center; gap: 6px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            Portfolio
        </div>
        <div style="flex: 1; display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; flex-wrap: nowrap; overflow: hidden; white-space: nowrap;">
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span style="color: #94a3b8; font-weight: 600; font-size: 0.7rem; text-transform: uppercase;">Bank:</span>
                <span style="font-weight: 700; font-size: 0.85rem; color: #38bdf8;">₹ 2.91L</span>
            </span>
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span style="color: #94a3b8; font-weight: 600; font-size: 0.7rem; text-transform: uppercase;">Deposits:</span>
                <span style="font-weight: 700; font-size: 0.85rem; color: #34d399;">₹ 31.60L</span>
            </span>
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span style="color: #94a3b8; font-weight: 600; font-size: 0.7rem; text-transform: uppercase;">Debit:</span>
                <span style="font-weight: 700; font-size: 0.85rem; color: #f87171;">2</span>
            </span>
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span style="color: #94a3b8; font-weight: 600; font-size: 0.7rem; text-transform: uppercase;">Credit:</span>
                <span style="font-weight: 700; font-size: 0.85rem; color: #f87171;">2</span>
            </span>
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span style="color: #94a3b8; font-weight: 600; font-size: 0.7rem; text-transform: uppercase;">Loans:</span>
                <span style="font-weight: 700; font-size: 0.85rem; color: #fbbf24;">₹ 52.27L</span>
            </span>
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span style="color: #94a3b8; font-weight: 600; font-size: 0.7rem; text-transform: uppercase;">Investments:</span>
                <span style="font-weight: 700; font-size: 0.85rem; color: #a78bfa;">₹ 18.45L</span>
            </span>
        </div>
    </div>
</section>"""

content = content[:match.start()] + new_html + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Forced single row layout.")
