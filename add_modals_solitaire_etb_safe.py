import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("customer_overview_solitaire.html")

modals_html = """
<!-- Send Deck Modal -->
<div id="send-deck-modal" class="ntb-modal-overlay" onclick="if(event.target===this) this.style.display='none'">
    <div class="ntb-modal" style="max-width: 500px;">
        <button class="ntb-modal-close" onclick="document.getElementById('send-deck-modal').style.display='none'">&times;</button>
        <h3>Send Program Deck</h3>
        <p>Send the exclusive Solitaire program benefits deck to the client's registered email address.</p>
        
        <div style="margin-bottom: 20px;">
            <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Registered Email Address</label>
            <input type="email" id="send-deck-email" class="ntb-modal-input" value="ashishkumar@gmail.com" readonly style="background: #f1f5f9; color: #64748b; cursor: not-allowed; border-color: #cbd5e1;">
        </div>
        
        <button class="ntb-modal-btn" onclick="handleSendDeck(this)">Send Email</button>
    </div>
</div>

<!-- Create Lead Modal -->
<div id="create-lead-modal" class="ntb-modal-overlay" onclick="if(event.target===this) this.style.display='none'">
    <div class="ntb-modal" style="max-width: 500px;">
        <button class="ntb-modal-close" onclick="document.getElementById('create-lead-modal').style.display='none'">&times;</button>
        <h3>Create Sales Lead</h3>
        <p>Log a new product lead for the customer. Core profile fields are locked.</p>
        
        <div style="margin-bottom: 16px;">
            <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Customer Name</label>
            <input type="text" value="Ashish Kumar" readonly style="width: 100%; padding: 12px 16px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 1rem; background: #f1f5f9; color: #64748b; cursor: not-allowed; outline: none; box-sizing: border-box;">
        </div>
        
        <div style="display: flex; gap: 12px; margin-bottom: 16px;">
            <div style="flex: 1;">
                <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Phone Number</label>
                <input type="text" value="9210860082" readonly style="width: 100%; padding: 12px 16px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 1rem; background: #f1f5f9; color: #64748b; cursor: not-allowed; outline: none; box-sizing: border-box;">
            </div>
            <div style="flex: 1;">
                <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Email Address</label>
                <input type="text" value="ashishkumar@gmail.com" readonly style="width: 100%; padding: 12px 16px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 1rem; background: #f1f5f9; color: #64748b; cursor: not-allowed; outline: none; box-sizing: border-box;">
            </div>
        </div>
        
        <div style="margin-bottom: 16px;">
            <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Program Pitching</label>
            <select class="ntb-modal-input" style="margin-bottom: 0;">
                <option value="solitaire">Solitaire Program (Recommended)</option>
                <option value="privy_plus">Privy Plus Program</option>
                <option value="privy">Privy Program</option>
                <option value="asset">Asset Program</option>
            </select>
        </div>
        
        <div style="display: flex; gap: 12px; margin-bottom: 24px;">
            <div style="flex: 1;">
                <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Total Investment</label>
                <select class="ntb-modal-input" style="margin-bottom: 0;">
                    <option value="<10L">&lt; ₹10 Lakh</option>
                    <option value="10L-30L">₹10 Lakh - ₹30 Lakh</option>
                    <option value="30L-75L">₹30 Lakh - ₹75 Lakh</option>
                    <option value="75L+">₹75 Lakh +</option>
                </select>
            </div>
            <div style="flex: 1;">
                <label style="display: block; font-size: 0.85rem; font-weight: 600; color: #475569; margin-bottom: 6px;">Total Asset Value</label>
                <select class="ntb-modal-input" style="margin-bottom: 0;">
                    <option value="<10L">&lt; ₹10 Lakh</option>
                    <option value="10L-30L">₹10 Lakh - ₹30 Lakh</option>
                    <option value="30L-75L">₹30 Lakh - ₹75 Lakh</option>
                    <option value="75L+">₹75 Lakh +</option>
                </select>
            </div>
        </div>
        
        <button class="ntb-modal-btn" onclick="handleCreateLead(this)">Create Lead</button>
    </div>
</div>
"""

# Insert modals right before the script tag containing handleSendDeck
pos = content.find("function handleSendDeck")
if pos != -1:
    # Find the <script> preceding it
    script_pos = content.rfind("<script", 0, pos)
    if script_pos != -1:
        new_content = (
            content[:script_pos] + modals_html + "\n" + content[script_pos:]
        )

        # Also fix resetting the email in handleSendDeck to ashishkumar@gmail.com
        new_content = new_content.replace(
            "document.getElementById('send-deck-email').value = \"\";",
            "document.getElementById('send-deck-email').value = \"ashishkumar@gmail.com\";",
        )

        try:
            open("customer_overview_solitaire.html", "r", encoding="utf-16").read()
            with open("customer_overview_solitaire.html", "w", encoding="utf-16") as out:
                out.write(new_content)
            print("Wrote customer_overview_solitaire.html as UTF-16")
        except Exception:
            with open("customer_overview_solitaire.html", "w", encoding="utf-8") as out:
                out.write(new_content)
            print("Wrote customer_overview_solitaire.html as UTF-8")
    else:
        print("Could not find <script> preceding handleSendDeck")
else:
    print("Could not find handleSendDeck function in customer_overview_solitaire.html")
