import os, re

filepath = r'customer_overview_solitaire.html'

try:
    with open(filepath, 'r', encoding='utf-16') as f:
        content = f.read()
    enc = 'utf-16'
except:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    enc = 'utf-8'

# Send Deck Modal replacement
send_deck_new = '''<div id="send-deck-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(4px); align-items: center; justify-content: center; z-index: 1000;">
    <div style="background: white; padding: 32px; border-radius: 16px; width: 90%; max-width: 480px; position: relative; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
        <button onclick="document.getElementById('send-deck-modal').style.display='none'" style="position: absolute; top: 16px; right: 16px; background: none; border: none; font-size: 1.5rem; color: #94a3b8; cursor: pointer;">&times;</button>
        <h3 style="margin-top: 0; margin-bottom: 24px; color: #0f172a; font-size: 1.5rem;">Send Pitch Deck</h3>
        <p style="color: #475569; margin-bottom: 24px; line-height: 1.5;">The pitch deck will be sent to the customer's registered email address.</p>
        <div style="margin-bottom: 24px;">
            <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Registered Email</label>
            <input type="email" id="send-deck-email" value="vaibhavkapoorwork@gmail.com" readonly style="width: 100%; padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 1rem; color: #64748b; background-color: #f8fafc; cursor: not-allowed; outline: none;">
        </div>
        <button onclick="handleSendDeck(this)" style="width: 100%; padding: 14px; background: #1e3a8a; color: white; border: none; border-radius: 8px; font-weight: 600; font-size: 1rem; cursor: pointer; transition: all 0.2s;">Send Email</button>
    </div>
</div>'''

# Create Lead Modal replacement
create_lead_new = '''<div id="create-lead-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(4px); align-items: center; justify-content: center; z-index: 1000;">
    <div style="background: white; padding: 32px; border-radius: 16px; width: 90%; max-width: 500px; position: relative; max-height: 90vh; overflow-y: auto; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);">
        <button onclick="document.getElementById('create-lead-modal').style.display='none'" style="position: absolute; top: 16px; right: 16px; background: none; border: none; font-size: 1.5rem; color: #94a3b8; cursor: pointer;">&times;</button>
        <h3 style="margin-top: 0; margin-bottom: 24px; color: #0f172a; font-size: 1.5rem;">Create Lead</h3>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
            <div>
                <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Customer Name</label>
                <input type="text" value="Rahul Sharma" readonly style="width: 100%; padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.95rem; color: #64748b; background-color: #f8fafc; cursor: not-allowed; outline: none;">
            </div>
            <div>
                <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Phone Number</label>
                <input type="text" value="+91 98765 43210" readonly style="width: 100%; padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.95rem; color: #64748b; background-color: #f8fafc; cursor: not-allowed; outline: none;">
            </div>
        </div>
        <div style="margin-bottom: 24px;">
            <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Email Address</label>
            <input type="email" value="rahul.sharma@example.com" readonly style="width: 100%; padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.95rem; color: #64748b; background-color: #f8fafc; cursor: not-allowed; outline: none;">
        </div>

        <div style="margin-bottom: 16px;">
            <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Select Program</label>
            <select style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; outline: none; background: white;">
                <option value="">Select a program...</option>
                <option value="solitaire">Kotak Solitaire</option>
                <option value="privy_plus">Privy League Plus</option>
                <option value="privy">Privy League</option>
            </select>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">
            <div>
                <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Investments Interest</label>
                <select style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; outline: none; background: white;">
                    <option value="none">None</option>
                    <option value="mf">Mutual Funds (SIP)</option>
                    <option value="pms">Portfolio Management Services</option>
                    <option value="fd">Fixed Deposits</option>
                </select>
            </div>
            <div>
                <label style="display: block; font-size: 0.875rem; font-weight: 600; color: #334155; margin-bottom: 8px;">Asset/Loan Interest</label>
                <select style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; outline: none; background: white;">
                    <option value="none">None</option>
                    <option value="hl">Home Loan</option>
                    <option value="lap">Loan Against Property</option>
                    <option value="al">Auto Loan</option>
                </select>
            </div>
        </div>

        <button onclick="handleCreateLead(this)" style="width: 100%; padding: 14px; background: #1e3a8a; color: white; border: none; border-radius: 8px; font-weight: 600; font-size: 1rem; cursor: pointer; transition: all 0.2s;">Create Lead</button>
    </div>
</div>'''

content = re.sub(r'<div[^>]*id="send-deck-modal"[^>]*>.*?(?=<div[^>]*id="create-lead-modal"|</script>)', send_deck_new + '\n\n', content, flags=re.DOTALL)
content = re.sub(r'<div[^>]*id="create-lead-modal"[^>]*>.*?(?=</script>|</body>)', create_lead_new + '\n\n', content, flags=re.DOTALL)

with open(filepath, 'w', encoding=enc) as f:
    f.write(content)

print("Modals updated successfully in customer_overview_solitaire.html")
