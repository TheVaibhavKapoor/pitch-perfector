import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add ID to Key Benefits section so we can hide it
text = text.replace('<h3 style=\"font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;\">Key Benefits</h3>', 
                    '<div id=\"dc-new-grid\"><h3 style=\"font-weight: 700; color: #111827; margin-bottom: 16px; font-size: 0.95rem;\">Key Benefits</h3>')

# Find the end of product-features-grid (which ends with </ul></div></div></div>)
# We will insert the new table right after the product-features-grid and close the dc-new-grid div.
grid_end_regex = r'(<div class=\"feature-card\">.*?<div class=\"feat-card-header\"><span class=\"feat-icon\">??</span><h3>Important Note</h3></div>.*?</ul>\s*</div>\s*</div>)'
match = re.search(grid_end_regex, text, re.DOTALL)
if match:
    new_html = match.group(1) + '''
</div> <!-- Close dc-new-grid -->

<div id="dc-existing-table" style="display: none;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; position: relative;">
        <h3 style="font-weight: 800; color: #111827; font-size: 1.1rem; margin: 0;">Compare & Save More</h3>
        <img src="kotak_solitaire_cc_card.png" alt="Solitaire Card" style="height: 120px; object-fit: contain; filter: drop-shadow(0 20px 30px rgba(0,0,0,0.15)); position: absolute; right: 0; top: -70px;" />
    </div>
    
    <div style="border: 1px solid #e5e7eb; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); background: #ffffff;">
        <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
                <tr style="background: #f9fafb; border-bottom: 1px solid #e5e7eb;">
                    <th style="padding: 16px; font-weight: 700; color: #111827;">Benefits</th>
                    <th style="padding: 16px; font-weight: 600; color: #4b5563;">Now<br><span style="font-size: 0.8rem; font-weight: 400;">(Standard Debit Card)</span></th>
                    <th style="padding: 16px; font-weight: 700; color: #111827;">Solitaire Debit Card</th>
                    <th style="padding: 16px; font-weight: 700; color: #111827;">Benefit %<br><span style="font-size: 0.8rem; font-weight: 400;">(Improvement)</span></th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">??</span> ATM withdrawal limit (per day)
                    </td>
                    <td style="padding: 16px; color: #4b5563;">?50,000</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">?2,50,000</td>
                    <td style="padding: 16px; font-weight: 700; color: #10b981;">+400%</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">???</span> Purchase limit (per day)
                    </td>
                    <td style="padding: 16px; color: #4b5563;">?1,00,000</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">?15,00,000</td>
                    <td style="padding: 16px; font-weight: 700; color: #10b981;">+1400%</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">???</span> Dining offer with Zomato
                    </td>
                    <td style="padding: 16px; color: #4b5563;">5% off</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">20% off</td>
                    <td style="padding: 16px; font-weight: 700; color: #10b981;">+300%</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">???</span> Spend & Save Offer
                    </td>
                    <td style="padding: 16px; color: #4b5563;">Up to ?250</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">Up to ?1500</td>
                    <td style="padding: 16px; font-weight: 700; color: #10b981;">+500%</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">??</span> Airport Lounge Access
                    </td>
                    <td style="padding: 16px; color: #4b5563;">Not Available</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">Domestic: 8 | International: 2</td>
                    <td style="padding: 16px; color: #10b981;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    </td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">???</span> Insurance Cover
                    </td>
                    <td style="padding: 16px; color: #4b5563;">?2 Lakh</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">?25 Lakh</td>
                    <td style="padding: 16px; font-weight: 700; color: #10b981;">+1150%</td>
                </tr>
                <tr>
                    <td style="padding: 16px; color: #4b5563; display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.2rem;">???</span> Concierge Services
                    </td>
                    <td style="padding: 16px; color: #4b5563;">Not Available</td>
                    <td style="padding: 16px; font-weight: 700; color: #111827;">24x7 Dedicated Concierge</td>
                    <td style="padding: 16px; color: #10b981;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
'''
    text = text.replace(match.group(1), new_html)

# Add logic to switch based on type
js_code = '''
            const type = localStorage.getItem('solitaire_type');
            if (type === 'Existing') {
                document.getElementById('dc-new-grid').style.display = 'none';
                document.getElementById('dc-existing-table').style.display = 'block';
            }
'''
if 'const type = localStorage.getItem(\'solitaire_type\');' in text and 'dc-existing-table' not in text.split('const type = localStorage.getItem(\'solitaire_type\');')[1]:
    text = text.replace("const type = localStorage.getItem('solitaire_type');", js_code)
elif 'const type = localStorage.getItem(\'solitaire_type\');' in text:
    pass

with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated DC panel successfully")
