import os
import re

file_path = 'customer_overview_solitaire.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the cues-expanded-content div
pattern = r'<div id="cues-expanded-content".*?</div>\s*</div>\s*</div>'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find cues-expanded-content block")
    exit(1)

new_html = """<div id="cues-expanded-content" style="display: none; padding: 20px; background: white; border-top: 1px solid #e2e8f0;">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                                        <h3 style="color: #065f46; margin: 0; font-size: 1.1rem; font-weight: 800;">Active Offers</h3>
                                        <button onclick="window.location.href='experience_solitaire_dashboard_new.html'" style="background: #065f46; border: none; color: white; padding: 6px 14px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; cursor: pointer; box-shadow: 0 2px 8px rgba(6,95,70,0.2); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">✨ View Pitches</button>
                                    </div>
                                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px;">
                                        <div style="background: white; border: 1px solid #e2e8f0; padding: 12px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                                            <div style="color: #065f46; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Credit Card Limit Upgrade</div>
                                            <div style="color: #475569; font-size: 0.75rem; line-height: 1.4;">Pre-approved limit enhancement of ₹1,50,000 on existing Platinum Card.</div>
                                        </div>
                                        <div style="background: white; border: 1px solid #e2e8f0; padding: 12px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                                            <div style="color: #065f46; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Home Loan Top-up</div>
                                            <div style="color: #475569; font-size: 0.75rem; line-height: 1.4;">Eligible for ₹10L top-up at preferential interest rate of 8.45%.</div>
                                        </div>
                                        <div style="background: white; border: 1px solid #e2e8f0; padding: 12px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                                            <div style="color: #065f46; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Term Deposit Renewal</div>
                                            <div style="color: #475569; font-size: 0.75rem; line-height: 1.4;">₹5L FD maturing next week. Offer higher yield ActivMoney.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>"""

content = content[:match.start()] + new_html + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated cues expanded background to white.")
