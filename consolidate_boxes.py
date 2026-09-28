import os
import re

file_path = 'customer_overview_solitaire.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_html_pattern = r'<div class="sales-opportunities-grid">.*?</section>'
old_html_match = re.search(old_html_pattern, content, re.DOTALL)

if not old_html_match:
    print("Could not find sales-opportunities-grid section.")
    exit(1)

new_html = """<div style="display: flex; gap: 16px; margin-bottom: 28px; flex-wrap: wrap;">
                          <!-- Personalised offers (Slim) -->
                          <div style="flex: 1; min-width: 300px; background: linear-gradient(135deg, #3730a3 0%, #312e81 100%); border-radius: 12px; padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(49,46,129,0.15);">
                              <div style="display: flex; align-items: center; gap: 12px;">
                                  <div style="background: rgba(255,255,255,0.15); padding: 8px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                                          <rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect>
                                          <line x1="12" y1="18" x2="12.01" y2="18"></line>
                                      </svg>
                                  </div>
                                  <div>
                                      <div style="color: white; font-weight: 700; font-size: 0.95rem; line-height: 1.2;">Personalised offers</div>
                                      <div style="color: #a5b4fc; font-size: 0.75rem; margin-top: 2px;">View & redeem in Interact App</div>
                                  </div>
                              </div>
                              <button style="background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.3); color: white; padding: 6px 14px; border-radius: 8px; font-size: 0.8rem; font-weight: 600; cursor: pointer; transition: background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.3)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'">Open ↗</button>
                          </div>

                          <!-- Customer Cues (Slim) -->
                          <div style="flex: 2; min-width: 450px; background: linear-gradient(135deg, #065f46 0%, #064e3b 100%); border-radius: 12px; padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(6,95,70,0.15);">
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
                              <button onclick="window.location.href='etb_pitch.html'" style="background: white; border: none; color: #065f46; padding: 8px 16px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">✨ View Pitch</button>
                          </div>
                      </div>
                  </section>"""

content = content[:old_html_match.start()] + new_html + content[old_html_match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Consolidated big boxes into 1 line slim layout.")
