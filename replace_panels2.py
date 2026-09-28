import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

dc_panel_new = '''                <div id="panel-dc" class="info-panel active">
                    <div style="background: #ffffff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e5e7eb;">
                        <div style="border: 1px solid #a3a3a3; border-radius: 12px; display: flex; overflow: hidden; background: #ffffff;">
                            <!-- Current -->
                            <div style="flex: 1; border-right: 1px solid #a3a3a3; padding-bottom: 24px;">
                                <div style="padding: 20px 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #000000; margin-bottom: 8px;">
                                    Current
                                </div>
                                <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 20px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Transaction Limit</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1,50,000</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">ATM Limit</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">50,000</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Lounge Access</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">None</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Fuel Surcharge</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1% Waiver</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Reward Points</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1 per ?200</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Solitaire -->
                            <div style="flex: 1; padding-bottom: 24px;">
                                <div style="padding: 20px 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #ffffff; background: linear-gradient(180deg, #c92a2a 0%, #e03131 40%, #ffffff 100%); margin-bottom: 8px; border-top-right-radius: 12px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                                    Solitaire
                                </div>
                                <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 20px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Transaction Limit</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">15,00,000</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">900% More</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">ATM Limit</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">2,50,000</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">400% More</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Lounge Access</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">Unlimited</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">Added</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Fuel Surcharge</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">2.5% Waiver</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">150% More</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Reward Points</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">3X Multiplier</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">Added</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

cc_panel_new = '''                <div id="panel-cc" class="info-panel">
                    <div style="background: #ffffff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e5e7eb;">
                        <div style="border: 1px solid #a3a3a3; border-radius: 12px; display: flex; overflow: hidden; background: #ffffff;">
                            <!-- Current -->
                            <div style="flex: 1; border-right: 1px solid #a3a3a3; padding-bottom: 24px;">
                                <div style="padding: 20px 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #000000; margin-bottom: 8px;">
                                    Current
                                </div>
                                <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 20px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Credit Limit</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">2,00,000</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Reward Rate</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1.0%</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Forex Markup</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">3.5%</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Lounge Access</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">2/Quarter</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Golf Privileges</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">None</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Annual Fee</span>
                                        <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">?5,000</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Solitaire -->
                            <div style="flex: 1; padding-bottom: 24px;">
                                <div style="padding: 20px 16px; text-align: center; font-weight: 700; font-size: 1.25rem; color: #ffffff; background: linear-gradient(180deg, #c92a2a 0%, #e03131 40%, #ffffff 100%); margin-bottom: 8px; border-top-right-radius: 12px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                                    Solitaire
                                </div>
                                <div style="padding: 0 24px; display: flex; flex-direction: column; gap: 20px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Credit Limit</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">10,00,000</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">+400%</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Reward Rate</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">3.5%</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">+250%</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Forex Markup</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">1.5%</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">Save 57%</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Lounge Access</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">Unlimited</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">Added</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Golf Privileges</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">4 Rounds/Year</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">Added</span>
                                        </div>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="color: #4b5563; font-size: 1rem;">Annual Fee</span>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="font-weight: 700; font-size: 1.05rem; color: #000000;">Nil</span>
                                            <span style="border: 1px solid #16a34a; color: #16a34a; padding: 2px 10px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; background: #ffffff;">Save ?5k</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = re.sub(r'<div id="panel-dc" class="info-panel active">.*?(?=<div id="panel-cc" class="info-panel)', dc_panel_new + '\n\n', content, flags=re.DOTALL)
content = re.sub(r'<div id="panel-cc" class="info-panel">.*?(?=<div id="panel-assets" class="info-panel">)', cc_panel_new + '\n\n', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Panels!')
