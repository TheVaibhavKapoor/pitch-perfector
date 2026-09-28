import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

dc_panel_new = '''                <div id="panel-dc" class="info-panel active">
                    <div style="border: 1px solid #777777; border-radius: 12px; display: flex; overflow: hidden; background: #ffffff;">
                        <!-- Current -->
                        <div style="flex: 1; border-right: 1px solid #777777; padding-bottom: 24px;">
                            <div style="padding: 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #000000; margin-bottom: 16px;">
                                Current
                            </div>
                            <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 16px;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Transaction Limit</span>
                                    <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">150000</span>
                                </div>
                            </div>
                        </div>

                        <!-- Solitaire -->
                        <div style="flex: 1; padding-bottom: 24px;">
                            <div style="padding: 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #ffffff; background: linear-gradient(180deg, #991b1b 0%, #dc2626 40%, #ffffff 100%); margin-bottom: 16px; border-top-right-radius: 12px; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
                                Solitaire
                            </div>
                            <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 16px;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Transaction Limit</span>
                                    <div style="display: flex; align-items: center; gap: 12px;">
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">150000</span>
                                        <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">12% More</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

cc_panel_new = '''                <div id="panel-cc" class="info-panel">
                    <div style="border: 1px solid #777777; border-radius: 12px; display: flex; overflow: hidden; background: #ffffff;">
                        <!-- Current -->
                        <div style="flex: 1; border-right: 1px solid #777777; padding-bottom: 24px;">
                            <div style="padding: 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #000000; margin-bottom: 16px;">
                                Current
                            </div>
                            <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 16px;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Credit Limit</span>
                                    <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">200000</span>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Reward Rate</span>
                                    <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1.0%</span>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Forex Markup</span>
                                    <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">3.5%</span>
                                </div>
                            </div>
                        </div>

                        <!-- Solitaire -->
                        <div style="flex: 1; padding-bottom: 24px;">
                            <div style="padding: 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #ffffff; background: linear-gradient(180deg, #991b1b 0%, #dc2626 40%, #ffffff 100%); margin-bottom: 16px; border-top-right-radius: 12px; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
                                Solitaire
                            </div>
                            <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 16px;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Credit Limit</span>
                                    <div style="display: flex; align-items: center; gap: 12px;">
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1000000</span>
                                        <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">+400%</span>
                                    </div>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Reward Rate</span>
                                    <div style="display: flex; align-items: center; gap: 12px;">
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">3.5%</span>
                                        <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">+250%</span>
                                    </div>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span style="color: #333333; font-size: 0.95rem;">Forex Markup</span>
                                    <div style="display: flex; align-items: center; gap: 12px;">
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1.5%</span>
                                        <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">Save 57%</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = re.sub(r'<div id="panel-dc" class="info-panel">.*?(?=<div id="panel-cc" class="info-panel)', dc_panel_new + '\n\n', content, flags=re.DOTALL)
content = re.sub(r'<div id="panel-cc" class="info-panel active">.*?(?=<div id="panel-assets" class="info-panel">)', cc_panel_new + '\n\n', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Panels!')
