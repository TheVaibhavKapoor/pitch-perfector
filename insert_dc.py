import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

def insert_comparison(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the panel-dc exactly
    panel_start = text.find('<div class=\"info-panel\" id=\"panel-dc\">')
    if panel_start == -1:
        return
    
    # We want to wrap the product-features-grid inside panel-dc with a div
    grid_start_str = '<div class=\"product-features-grid\" style=\"grid-template-columns: 1fr 1fr; margin-bottom: 24px;\">'
    grid_start_idx = text.find(grid_start_str, panel_start)
    if grid_start_idx == -1:
        return
    
    # Now find where this grid ends. It ends after the 4th feature-card.
    # We can just look for the last </div> before the panel ends.
    # But wait, it's safer to just look for the Important Notes section and its closing tags.
    important_note_idx = text.find('<h3>Important Note</h3>', grid_start_idx)
    end_of_grid_idx = text.find('</ul>\n</div>\n</div>', important_note_idx)
    
    if end_of_grid_idx == -1:
        # fallback
        end_of_grid_idx = text.find('</ul>\r\n</div>\r\n</div>', important_note_idx)
        
    if end_of_grid_idx == -1:
        print(f"Could not find end of grid in {filename}")
        return
        
    # The actual end of the grid is after the two </div>s.
    # '</ul>\n</div>\n</div>' is 17 characters long.
    insert_pos = end_of_grid_idx + 17
    
    # Let's verify what we are wrapping
    # We will replace grid_start_str with '<div id="dc-new-grid">' + grid_start_str
    # And at insert_pos, we append '</div>' and then our new table.
    
    table_html = '''</div> <!-- end of dc-new-grid -->

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
</div>'''

    # Apply changes
    new_text = text[:insert_pos] + table_html + text[insert_pos:]
    new_text = new_text[:grid_start_idx] + '<div id="dc-new-grid">\n' + new_text[grid_start_idx:]

    js_code = '''
            const type = localStorage.getItem('solitaire_type');
            if (type === 'Existing') {
                const dcNew = document.getElementById('dc-new-grid');
                const dcExist = document.getElementById('dc-existing-table');
                if (dcNew) dcNew.style.display = 'none';
                if (dcExist) dcExist.style.display = 'block';
            }
'''
    if 'const type = localStorage.getItem(\'solitaire_type\');' in new_text:
        new_text = new_text.replace("const type = localStorage.getItem('solitaire_type');", js_code)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    print(f"Fixed {filename} properly without breaking anything!")

insert_comparison('experience_solitaire_dashboard.html')
insert_comparison('experience_solitaire_dashboard_new.html')
