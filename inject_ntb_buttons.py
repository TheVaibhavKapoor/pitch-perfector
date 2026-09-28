import os
import re

files_to_update = [
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard_new.html'
]

header_html = """
<header class="top-header" style="display: flex; justify-content: flex-end; align-items: center; padding: 16px 32px; background: white; border-bottom: 1px solid #e5e7eb; gap: 12px;">
    <button onclick="document.getElementById('compare-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Compare Program</button>
    <button onclick="document.getElementById('send-deck-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Send Deck</button>
    <button onclick="document.getElementById('create-lead-modal').style.display='flex'" style="background: #1e3a8a; border: none; padding: 9px 20px; border-radius: 8px; font-weight: 600; color: white; cursor: pointer; box-shadow: 0 4px 12px rgba(30,58,138,0.2); transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">Create Lead</button>
</header>
"""

modals_html = """
<!-- MODALS -->
<style>
.ntb-modal-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); display: none; align-items: center; justify-content: center; z-index: 9999; backdrop-filter: blur(4px);
}
.ntb-modal {
    background: white; border-radius: 16px; padding: 32px; width: 100%; max-width: 600px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); position: relative; max-height: 90vh; overflow-y: auto;
}
.ntb-modal-close {
    position: absolute; top: 24px; right: 24px; cursor: pointer; color: #64748b; font-size: 1.5rem; line-height: 1; border: none; background: none; padding: 0;
}
.ntb-modal h3 { font-size: 1.4rem; font-weight: 800; color: #0f172a; margin-bottom: 8px; margin-top: 0; }
.ntb-modal p { color: #64748b; font-size: 0.95rem; margin-bottom: 24px; }
.ntb-modal-input { width: 100%; padding: 12px 16px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 1rem; margin-bottom: 16px; outline: none; transition: border-color 0.2s; box-sizing: border-box; font-family: inherit; }
.ntb-modal-input:focus { border-color: #1e3a8a; }
.ntb-modal-btn { width: 100%; padding: 14px; background: #1e3a8a; color: white; border: none; border-radius: 8px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: background 0.2s; }
.ntb-modal-btn:hover { background: #172554; }

.program-compare-table { width: 100%; border-collapse: collapse; margin-bottom: 16px; }
.program-compare-table th, .program-compare-table td { border: 1px solid #e2e8f0; padding: 12px 16px; text-align: left; font-size: 0.9rem; }
.program-compare-table th { background: #f8fafc; font-weight: 700; color: #0f172a; }
.program-compare-table td { color: #475569; }

.lead-checkbox-group { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
.lead-checkbox-label { display: flex; align-items: center; gap: 12px; cursor: pointer; font-size: 0.95rem; color: #334155; font-weight: 500; }
.lead-checkbox-label input { width: 18px; height: 18px; cursor: pointer; }
</style>

<!-- Compare Modal -->
<div id="compare-modal" class="ntb-modal-overlay" onclick="if(event.target===this) this.style.display='none'">
    <div class="ntb-modal">
        <button class="ntb-modal-close" onclick="document.getElementById('compare-modal').style.display='none'">&times;</button>
        <h3>Program Comparison</h3>
        <p>A quick view of the eligibility and core benefits across our premium tiers.</p>
        
        <table class="program-compare-table">
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Kotak Solitaire</th>
                    <th>Kotak Privy+</th>
                    <th>Kotak Privy</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Eligibility (Salaried)</strong></td>
                    <td>₹75 Lakh+ RV</td>
                    <td>₹30 Lakh+ RV or ₹3L+ Salary</td>
                    <td>₹10 Lakh+ RV or ₹1L+ Salary</td>
                </tr>
                <tr>
                    <td><strong>Dedicated RM</strong></td>
                    <td>Yes (Senior RM)</td>
                    <td>Yes</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <td><strong>Credit Card</strong></td>
                    <td>Solitaire Metal Card</td>
                    <td>Privy+ Signature</td>
                    <td>Privy Signature</td>
                </tr>
                <tr>
                    <td><strong>Lounge Access</strong></td>
                    <td>Unlimited + Guest (Global)</td>
                    <td>Unlimited (Domestic)</td>
                    <td>4/Quarter (Domestic)</td>
                </tr>
                <tr>
                    <td><strong>Pricing</strong></td>
                    <td>Nil Charges</td>
                    <td>Nil Charges</td>
                    <td>Nil Charges</td>
                </tr>
            </tbody>
        </table>
        <button class="ntb-modal-btn" onclick="document.getElementById('compare-modal').style.display='none'">Close Comparison</button>
    </div>
</div>

<!-- Send Deck Modal -->
<div id="send-deck-modal" class="ntb-modal-overlay" onclick="if(event.target===this) this.style.display='none'">
    <div class="ntb-modal" style="max-width: 450px;">
        <button class="ntb-modal-close" onclick="document.getElementById('send-deck-modal').style.display='none'">&times;</button>
        <h3>Send Pitch Deck</h3>
        <p>Share the complete program presentation with your prospect.</p>
        <input type="email" class="ntb-modal-input" id="send-deck-email" placeholder="client@example.com">
        <button class="ntb-modal-btn" onclick="handleSendDeck(this)">Send Email</button>
    </div>
</div>

<!-- Create Lead Modal -->
<div id="create-lead-modal" class="ntb-modal-overlay" onclick="if(event.target===this) this.style.display='none'">
    <div class="ntb-modal" style="max-width: 500px;">
        <button class="ntb-modal-close" onclick="document.getElementById('create-lead-modal').style.display='none'">&times;</button>
        <h3>Create New Lead</h3>
        <p>Verify client details and select the programs they are interested in.</p>
        
        <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 12px; color: #0f172a;">Client Details</h4>
        <input type="text" class="ntb-modal-input" placeholder="Client Name" value="Vaibhav Kapoor">
        <input type="tel" class="ntb-modal-input" placeholder="Phone Number" value="+91 9876543210">
        
        <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 12px; margin-top: 8px; color: #0f172a;">Interested In</h4>
        <div class="lead-checkbox-group">
            <label class="lead-checkbox-label">
                <input type="checkbox" checked> Kotak Solitaire Program
            </label>
            <label class="lead-checkbox-label">
                <input type="checkbox"> Home Loan / Financing
            </label>
            <label class="lead-checkbox-label">
                <input type="checkbox"> Investment & Wealth
            </label>
            <label class="lead-checkbox-label">
                <input type="checkbox"> Current Account / Business
            </label>
        </div>
        
        <button class="ntb-modal-btn" onclick="handleCreateLead(this)">Create Lead</button>
    </div>
</div>

<script>
function handleSendDeck(btn) {
    const email = document.getElementById('send-deck-email').value;
    if(!email) { alert("Please enter an email address."); return; }
    btn.innerText = "Sending...";
    btn.style.opacity = "0.7";
    setTimeout(() => {
        btn.innerText = "Sent Successfully!";
        btn.style.background = "#10b981";
        btn.style.opacity = "1";
        setTimeout(() => {
            document.getElementById('send-deck-modal').style.display='none';
            btn.innerText = "Send Email";
            btn.style.background = "#1e3a8a";
            document.getElementById('send-deck-email').value = "";
        }, 1500);
    }, 1000);
}

function handleCreateLead(btn) {
    btn.innerText = "Creating...";
    btn.style.opacity = "0.7";
    setTimeout(() => {
        btn.innerText = "Lead Created Successfully!";
        btn.style.background = "#10b981";
        btn.style.opacity = "1";
        setTimeout(() => {
            document.getElementById('create-lead-modal').style.display='none';
            btn.innerText = "Create Lead";
            btn.style.background = "#1e3a8a";
        }, 1500);
    }, 1000);
}
</script>
<!-- END MODALS -->
"""

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Avoid duplicating
        if "id=\"compare-modal\"" in content:
            print(f"Modals already exist in {filename}, skipping.")
            continue
            
        # 1. Insert header
        # Find <!-- top-header removed --> or <main class="main-content">
        if '<!-- top-header removed -->' in content:
            content = content.replace('<!-- top-header removed -->', header_html)
        elif '<main class="main-content">' in content:
            content = content.replace('<main class="main-content">', '<main class="main-content">\n' + header_html)
            
        # 2. Append modals right before </body>
        if '</body>' in content:
            content = content.replace('</body>', modals_html + '\n</body>')
        else:
            content += modals_html
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added top-right options and modals to {filename}")
