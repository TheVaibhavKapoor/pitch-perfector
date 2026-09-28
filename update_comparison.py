import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the top comparison section
start_marker = '<!-- Upgrade Comparison Section -->'
end_marker = '<div style=\"background: #ffffff; border-bottom: 1px solid #e5e7eb; padding: 0 32px; display: flex; gap: 32px;\">'

if start_marker in content and end_marker in content:
    content = content[:content.find(start_marker)] + end_marker + content[content.find(end_marker)+len(end_marker):]

# 2. Update panel-individual-dc
dc_panel_html = '''<div id=\"panel-individual-dc\" class=\"info-panel\">
    <div style=\"border: 1px solid #e2e8f0; border-radius: 16px; display: flex; overflow: hidden; background: #ffffff;\">
        <!-- Current -->
        <div style=\"flex: 1; border-right: 1px solid #e2e8f0; padding-bottom: 24px;\">
            <div style=\"padding: 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #000000; margin-bottom: 16px;\">
                Current
            </div>
            <div style=\"padding: 0 24px; display: flex; flex-direction: column; gap: 16px;\">
                <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                    <span style=\"color: #475569; font-size: 0.95rem;\">Transaction Limit</span>
                    <span style=\"font-weight: 700; font-size: 1.05rem; color: #000000;\">150000</span>
                </div>
                <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                    <span style=\"color: #475569; font-size: 0.95rem;\">ATM Withdrawal Limit</span>
                    <span style=\"font-weight: 700; font-size: 1.05rem; color: #000000;\">50000</span>
                </div>
                <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                    <span style=\"color: #475569; font-size: 0.95rem;\">Lounge Access</span>
                    <span style=\"font-weight: 700; font-size: 1.05rem; color: #000000;\">None</span>
                </div>
            </div>
        </div>

        <!-- Solitaire -->
        <div style=\"flex: 1; padding-bottom: 24px;\">
            <div style=\"padding: 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #ffffff; background: linear-gradient(180deg, #991b1b 0%, #dc2626 40%, #ffffff 100%); margin-bottom: 16px; border-top-right-radius: 16px;\">
                Solitaire
            </div>
            <div style=\"padding: 0 24px; display: flex; flex-direction: column; gap: 16px;\">
                <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                    <span style=\"color: #475569; font-size: 0.95rem;\">Transaction Limit</span>
                    <div style=\"display: flex; align-items: center; gap: 12px;\">
                        <span style=\"font-weight: 700; font-size: 1.05rem; color: #000000;\">500000</span>
                        <span style=\"border: 1px solid #22c55e; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;\">233% More</span>
                    </div>
                </div>
                <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                    <span style=\"color: #475569; font-size: 0.95rem;\">ATM Withdrawal Limit</span>
                    <div style=\"display: flex; align-items: center; gap: 12px;\">
                        <span style=\"font-weight: 700; font-size: 1.05rem; color: #000000;\">200000</span>
                        <span style=\"border: 1px solid #22c55e; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;\">300% More</span>
                    </div>
                </div>
                <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                    <span style=\"color: #475569; font-size: 0.95rem;\">Lounge Access</span>
                    <div style=\"display: flex; align-items: center; gap: 12px;\">
                        <span style=\"font-weight: 700; font-size: 1.05rem; color: #000000;\">Unlimited</span>
                        <span style=\"border: 1px solid #22c55e; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;\">Premium</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>'''

# Replace panel-individual-dc
dc_start = '<div id=\"panel-individual-dc\" class=\"info-panel\">'
dc_end = '</div>\\n                    <div id=\"panel-individual-cc\"'
if dc_start in content and dc_end in content:
    content = content[:content.find(dc_start)] + dc_panel_html + '\\n                    ' + dc_end[dc_end.find('<div id=\"panel-individual-cc\"'):]

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(\"Updated HTML!\")
