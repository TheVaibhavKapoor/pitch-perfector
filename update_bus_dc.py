# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the panel-business-dc inside the business wrapper
b_start = html.find('id="segment-business-content"')
dc_start = html.find('id="panel-business-dc"', b_start)
dc_end = html.find('id="panel-business-cc"', dc_start)

dc_content = html[dc_start:dc_end]

# Update the feature card text inside Business DC
dc_content = dc_content.replace('Air Accident Cover up to ₹1,00,00,000', 'Air Accident Cover up to ₹1,00,00,000')
dc_content = dc_content.replace('Personal Accident up to ₹15,00,000', 'Personal Accident up to ₹15,00,000')
dc_content = dc_content.replace('Lost Card Liability up to ₹4,75,000', 'Lost Card Liability up to ₹4,75,000') # Existing might be 6,00,000

# To be safe, just replace the entire Insurance Cover table and the bullet points in the grid for insurance.
# Let's find the table in dc_content
table_replacement = '''<table class="insurance-table">
                        <thead>
                            <tr>
                                <th>Debit Card Type</th>
                                <th>Lost Card Liability</th>
                                <th>Purchase Protection</th>
                                <th>Lost Baggage</th>
                                <th>Air Accident</th>
                                <th>Personal Accident Base*</th>
                                <th>Personal Accident Enhance**</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Solitaire Business Debit Card</strong></td>
                                <td>4,75,000</td>
                                <td>1,50,000</td>
                                <td>1,00,000</td>
                                <td>1,00,00,000</td>
                                <td>5,00,000</td>
                                <td>15,00,000</td>
                            </tr>
                        </tbody>
                    </table>'''

dc_content = re.sub(r'<table class="insurance-table">.*?</table>', table_replacement, dc_content, flags=re.DOTALL)

# Let's also update the feature card for Insurance in DC
feat_card_replacement = '''<div class="feature-card">
                                    <div class="feat-card-header"><span class="feat-icon">🛡️</span><h3>Insurance Cover</h3></div>
                                    <ul class="feat-list">
                                        <li>Air Accident Cover up to <strong style="color: #10b981;">₹1 Cr</strong></li>
                                        <li>Personal Accident up to <strong style="color: #10b981;">₹15 Lakhs</strong></li>
                                        <li>Lost Card Liability up to <strong style="color: #10b981;">₹4.75 Lakhs</strong></li>
                                        <li>Purchase Protection <strong style="color: #10b981;">₹1.5 Lakhs</strong></li>
                                    </ul>
                                </div>'''

dc_content = re.sub(r'<div class="feature-card">\s*<div class="feat-card-header"><span class="feat-icon">🛡️</span><h3>Insurance Cover</h3></div>.*?</ul>\s*</div>', feat_card_replacement, dc_content, flags=re.DOTALL)

# Also update the title in DC
dc_content = dc_content.replace('>Solitaire Debit Card</h2>', '>Solitaire Business Debit Card</h2>')

html = html[:dc_start] + dc_content + html[dc_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Business DC updated")
