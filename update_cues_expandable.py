import os
import re

file_path = 'customer_overview_solitaire.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the slim Customer Cues block
pattern = r'<!-- Customer Cues \(Slim\) -->\s*<div style="flex: 1; min-width: 100%; background: linear-gradient.*?</div>\s*</div>\s*</div>\s*<button.*?</button>\s*</div>'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find Customer Cues block")
    exit(1)

new_html = """<!-- Customer Cues (Expandable) -->
                            <div style="flex: 1; min-width: 100%; background: linear-gradient(135deg, #065f46 0%, #064e3b 100%); border-radius: 12px; box-shadow: 0 4px 12px rgba(6,95,70,0.15); overflow: hidden;">
                                <div style="padding: 12px 20px; display: flex; align-items: center; justify-content: space-between;">
                                    <div style="display: flex; align-items: center; gap: 16px;">
                                        <div style="background: rgba(255,255,255,0.15); padding: 8px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="#fbbf24">
                                                <path d="M12 2L14.5 9.5L22 12L14.5 14.5L12 22L9.5 14.5L2 12L9.5 9.5L12 2Z"/>
                                            </svg>
                                        </div>
                                        <div>
                                            <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
                                                <span style="color: white; font-weight: 700; font-size: 0.95rem;">5 Customer Cues</span>
                                                <div style="display: flex; gap: 6px;">
                                                    <span style="background: rgba(255,255,255,0.15); color: #d1fae5; padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; font-weight: 600;">Service - Updation</span>
                                                    <span style="background: rgba(255,255,255,0.15); color: #d1fae5; padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; font-weight: 600;">Mutual Funds</span>
                                                    <span style="background: rgba(255,255,255,0.15); color: #d1fae5; padding: 2px 8px; border-radius: 12px; font-size: 0.7rem; font-weight: 600;">Term Deposit</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <button onclick="var content = document.getElementById('cues-expanded-content'); var isHidden = content.style.display === 'none'; content.style.display = isHidden ? 'block' : 'none'; this.innerHTML = isHidden ? 'View Less' : 'View More';" style="background: white; border: none; color: #065f46; padding: 8px 16px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">View More</button>
                                </div>
                                <div id="cues-expanded-content" style="display: none; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                                        <h3 style="color: white; margin: 0; font-size: 1rem; font-weight: 700;">Active Offers</h3>
                                        <button onclick="window.location.href='experience_solitaire_dashboard_new.html'" style="background: #fbbf24; border: none; color: #78350f; padding: 6px 14px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">✨ View Pitches</button>
                                    </div>
                                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px;">
                                        <div style="background: rgba(255,255,255,0.1); padding: 12px; border-radius: 8px;">
                                            <div style="color: #fbbf24; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Credit Card Limit Upgrade</div>
                                            <div style="color: #d1fae5; font-size: 0.75rem; line-height: 1.4;">Pre-approved limit enhancement of ₹1,50,000 on existing Platinum Card.</div>
                                        </div>
                                        <div style="background: rgba(255,255,255,0.1); padding: 12px; border-radius: 8px;">
                                            <div style="color: #fbbf24; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Home Loan Top-up</div>
                                            <div style="color: #d1fae5; font-size: 0.75rem; line-height: 1.4;">Eligible for ₹10L top-up at preferential interest rate of 8.45%.</div>
                                        </div>
                                        <div style="background: rgba(255,255,255,0.1); padding: 12px; border-radius: 8px;">
                                            <div style="color: #fbbf24; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Term Deposit Renewal</div>
                                            <div style="color: #d1fae5; font-size: 0.75rem; line-height: 1.4;">₹5L FD maturing next week. Offer higher yield ActivMoney.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>"""

content = content[:match.start()] + new_html + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Customer Cues to be expandable.")
