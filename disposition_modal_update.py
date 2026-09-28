import re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def save_content(fpath, content):
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


DISPOSITION_MODAL = '''<!-- Disposition Modal -->
<div id="create-lead-modal" class="ntb-modal-overlay" onclick="if(event.target===this) this.style.display='none'">
    <div class="ntb-modal" style="max-width: 620px; max-height: 90vh; overflow-y: auto;">
        <button class="ntb-modal-close" onclick="document.getElementById('create-lead-modal').style.display='none'">&times;</button>
        <h3 style="margin-bottom: 4px;">Customer Disposition</h3>
        <p style="margin-bottom: 20px; color:#64748b; font-size:0.92rem;">Record outcome of this interaction. Locked fields are pre-filled from the customer profile.</p>

        <!-- Client Details -->
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px; margin-bottom:20px;">
            <div style="font-size:0.78rem; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:.5px; margin-bottom:12px;">Client Details</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                <div>
                    <label style="display:block; font-size:0.8rem; font-weight:600; color:#475569; margin-bottom:4px;">Customer Name</label>
                    <input type="text" id="disp-name-field" readonly style="width:100%; padding:9px 12px; border:1.5px solid #cbd5e1; border-radius:7px; font-size:0.9rem; background:#f1f5f9; color:#64748b; cursor:not-allowed; outline:none; box-sizing:border-box;">
                </div>
                <div>
                    <label style="display:block; font-size:0.8rem; font-weight:600; color:#475569; margin-bottom:4px;">Phone Number</label>
                    <input type="text" id="disp-phone-field" readonly style="width:100%; padding:9px 12px; border:1.5px solid #cbd5e1; border-radius:7px; font-size:0.9rem; background:#f1f5f9; color:#64748b; cursor:not-allowed; outline:none; box-sizing:border-box;">
                </div>
                <div style="grid-column:1/-1;">
                    <label style="display:block; font-size:0.8rem; font-weight:600; color:#475569; margin-bottom:4px;">Email Address</label>
                    <input type="text" id="disp-email-field" readonly style="width:100%; padding:9px 12px; border:1.5px solid #cbd5e1; border-radius:7px; font-size:0.9rem; background:#f1f5f9; color:#64748b; cursor:not-allowed; outline:none; box-sizing:border-box;">
                </div>
            </div>
        </div>

        <!-- Program Pitched -->
        <div style="margin-bottom:20px;">
            <div style="font-size:0.78rem; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:.5px; margin-bottom:12px;">Program Pitched</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                <div>
                    <label style="display:block; font-size:0.8rem; font-weight:600; color:#475569; margin-bottom:4px;">Program</label>
                    <select class="ntb-modal-input" id="disp-program" style="margin-bottom:0;">
                        <option value="solitaire">Solitaire</option>
                        <option value="privy_plus">Privy Plus</option>
                        <option value="privy">Privy</option>
                        <option value="asset">Asset Program</option>
                    </select>
                </div>
                <div>
                    <label style="display:block; font-size:0.8rem; font-weight:600; color:#475569; margin-bottom:4px;">Customer Response</label>
                    <select class="ntb-modal-input" id="disp-program-interest" onchange="toggleProgramReason()" style="margin-bottom:0;">
                        <option value="interested">Interested</option>
                        <option value="not_interested">Not Interested</option>
                    </select>
                </div>
            </div>
            <div id="disp-program-reason-wrap" style="display:none; margin-top:10px;">
                <label style="display:block; font-size:0.8rem; font-weight:600; color:#475569; margin-bottom:4px;">Reason for Disinterest</label>
                <select class="ntb-modal-input" id="disp-program-reason" style="margin-bottom:0;">
                    <option value="">Select reason...</option>
                    <option value="high_charges">High charges / fees</option>
                    <option value="already_has">Already has similar program</option>
                    <option value="no_need">No immediate need</option>
                    <option value="budget">Budget constraints</option>
                    <option value="will_think">Will think about it</option>
                    <option value="other">Other</option>
                </select>
            </div>
        </div>

        <!-- Product Disposition -->
        <div style="margin-bottom:24px;">
            <div style="font-size:0.78rem; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:.5px; margin-bottom:12px;">Product-wise Disposition</div>
            <div id="product-disp-list" style="display:flex; flex-direction:column; gap:10px;">
                <!-- rows injected by JS -->
            </div>
            <button onclick="addProductRow()" style="margin-top:10px; background:transparent; border:1.5px dashed #cbd5e1; border-radius:8px; padding:8px 16px; color:#64748b; font-size:0.85rem; font-weight:600; cursor:pointer; width:100%; transition:all 0.2s;" onmouseover="this.style.borderColor='#1e3a8a';this.style.color='#1e3a8a'" onmouseout="this.style.borderColor='#cbd5e1';this.style.color='#64748b'">+ Add Product</button>
        </div>

        <button class="ntb-modal-btn" onclick="handleDisposition(this)">Save Disposition</button>
    </div>
</div>

<script>
(function() {
    const PRODUCTS = ['Savings Account','Credit Card','Home Loan','Auto Loan','Personal Loan','Demat & Trading','Fixed Deposit','Insurance','Forex Card','Current Account'];
    const REASONS = ['High interest rate','Already has product','No current need','Eligibility concern','Budget constraints','Will think about it','Other'];

    function createProductRow(idx) {
        const rowId = 'prod-row-' + idx;
        const selectId = 'prod-sel-' + idx;
        const interestId = 'prod-int-' + idx;
        const reasonWrapId = 'prod-reason-wrap-' + idx;
        const reasonId = 'prod-reason-' + idx;
        const opts = PRODUCTS.map(p => `<option value="${p}">${p}</option>`).join('');
        const rOpts = REASONS.map(r => `<option value="${r}">${r}</option>`).join('');
        return `<div id="${rowId}" style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px;">
            <div style="display:grid; grid-template-columns:1fr 1fr auto; gap:8px; align-items:end;">
                <div>
                    <label style="font-size:0.78rem; font-weight:600; color:#64748b; display:block; margin-bottom:4px;">Product</label>
                    <select id="${selectId}" class="ntb-modal-input" style="margin-bottom:0; font-size:0.88rem;">${opts}</select>
                </div>
                <div>
                    <label style="font-size:0.78rem; font-weight:600; color:#64748b; display:block; margin-bottom:4px;">Response</label>
                    <select id="${interestId}" class="ntb-modal-input" onchange="toggleProductReason('${reasonWrapId}')" style="margin-bottom:0; font-size:0.88rem;">
                        <option value="interested">Interested</option>
                        <option value="not_interested">Not Interested</option>
                    </select>
                </div>
                <button onclick="document.getElementById('${rowId}').remove()" style="background:none; border:none; color:#ef4444; font-size:1.2rem; cursor:pointer; padding:8px 6px; line-height:1;">&times;</button>
            </div>
            <div id="${reasonWrapId}" style="display:none; margin-top:8px;">
                <label style="font-size:0.78rem; font-weight:600; color:#64748b; display:block; margin-bottom:4px;">Reason for Disinterest</label>
                <select id="${reasonId}" class="ntb-modal-input" style="margin-bottom:0; font-size:0.88rem;"><option value="">Select reason...</option>${rOpts}</select>
            </div>
        </div>`;
    }

    let rowCount = 0;

    window.addProductRow = function() {
        const list = document.getElementById('product-disp-list');
        if (list) {
            const div = document.createElement('div');
            div.innerHTML = createProductRow(rowCount++);
            list.appendChild(div.firstChild);
        }
    };

    window.toggleProgramReason = function() {
        const sel = document.getElementById('disp-program-interest');
        const wrap = document.getElementById('disp-program-reason-wrap');
        if (sel && wrap) wrap.style.display = sel.value === 'not_interested' ? 'block' : 'none';
    };

    window.toggleProductReason = function(wrapId) {
        const wrap = document.getElementById(wrapId);
        const interestId = wrapId.replace('reason-wrap', 'int');
        const sel = document.getElementById(interestId);
        if (wrap && sel) wrap.style.display = sel.value === 'not_interested' ? 'block' : 'none';
    };

    window.openDispositionModal = function() {
        // Pre-fill client details from DOM
        const name = document.getElementById('disp-name') || document.getElementById('cust-name') || document.getElementById('disp-name-field');
        const phone = document.getElementById('disp-phone') || document.getElementById('cust-phone') || document.getElementById('disp-phone-field');
        const email = document.getElementById('disp-email') || document.getElementById('cust-email') || document.getElementById('disp-email-field');

        const nameVal = (document.getElementById('disp-name') || {textContent:''}).textContent ||
                        (document.getElementById('cust-name') || {textContent:''}).textContent ||
                        localStorage.getItem('solitaire_name') || 'N/A';
        const phoneVal = (document.getElementById('disp-phone') || {textContent:''}).textContent ||
                         localStorage.getItem('solitaire_phone') || 'N/A';
        const emailVal = (document.getElementById('disp-email') || {textContent:''}).textContent ||
                         localStorage.getItem('solitaire_email') || 'N/A';

        const nf = document.getElementById('disp-name-field');
        const pf = document.getElementById('disp-phone-field');
        const ef = document.getElementById('disp-email-field');
        if (nf) nf.value = nameVal;
        if (pf) pf.value = phoneVal;
        if (ef) ef.value = emailVal;

        // Add one default product row if list is empty
        const list = document.getElementById('product-disp-list');
        if (list && list.children.length === 0) window.addProductRow();

        document.getElementById('create-lead-modal').style.display = 'flex';
    };

    window.handleDisposition = function(btn) {
        btn.innerText = 'Saving...';
        btn.style.opacity = '0.7';
        setTimeout(() => {
            btn.innerText = 'Disposition Saved!';
            btn.style.background = '#10b981';
            btn.style.opacity = '1';
            setTimeout(() => {
                document.getElementById('create-lead-modal').style.display = 'none';
                btn.innerText = 'Save Disposition';
                btn.style.background = '#1e3a8a';
                // Reset list
                const list = document.getElementById('product-disp-list');
                if (list) list.innerHTML = '';
                rowCount = 0;
            }, 1500);
        }, 900);
    };
})();
</script>
<!-- END DISPOSITION MODAL -->'''


def process_file(fpath, product_label="Solitaire Program"):
    content = get_content(fpath)

    # 1. Rename button from "Create Lead" -> "Disposition" and update onclick
    content = content.replace(
        "onclick=\"document.getElementById('create-lead-modal').style.display='flex'\" style=\"background: #1e3a8a; border: none; padding: 9px 20px; border-radius: 8px; font-weight: 600; color: white; cursor: pointer; box-shadow: 0 4px 12px rgba(30,58,138,0.2); transition: all 0.2s;\" onmouseover=\"this.style.transform='translateY(-2px)'\" onmouseout=\"this.style.transform='translateY(0)'\">Create Lead</button>",
        "onclick=\"openDispositionModal()\" style=\"background: #1e3a8a; border: none; padding: 9px 20px; border-radius: 8px; font-weight: 600; color: white; cursor: pointer; box-shadow: 0 4px 12px rgba(30,58,138,0.2); transition: all 0.2s;\" onmouseover=\"this.style.transform='translateY(-2px)'\" onmouseout=\"this.style.transform='translateY(0)'\">Disposition</button>"
    )

    # Also handle ETB version (customer_overview_solitaire.html has slightly different button)
    content = content.replace(
        "onclick=\"document.getElementById('create-lead-modal').style.display='flex'\" style=\"background: #1e3a8a;",
        "onclick=\"openDispositionModal()\" style=\"background: #1e3a8a;"
    )
    # Replace button text if it still says Create Lead for Disposition button
    content = content.replace(">Create Lead</button>", ">Disposition</button>")

    # 2. Remove old create-lead-modal block if present
    # Find it and strip until </div>\n</div>
    old_lead_pattern = re.compile(
        r'<!-- Create Lead Modal -->.*?<!-- END MODALS -->',
        re.DOTALL
    )
    if old_lead_pattern.search(content):
        content = old_lead_pattern.sub(DISPOSITION_MODAL, content)
    else:
        # Try to find just the old modal div and replace
        old_div_pat = re.compile(
            r'<!-- Create Lead Modal -->.*?(?=<!-- |\Z)',
            re.DOTALL
        )
        if old_div_pat.search(content):
            content = old_div_pat.sub('', content, count=1)

        # Remove old handleCreateLead script if present
        old_script_pat = re.compile(
            r'function handleCreateLead\(btn\)\s*\{.*?\}\s*\}?\s*</script>',
            re.DOTALL
        )
        content = old_script_pat.sub('</script>', content, count=1)

        # Append disposition modal before </body> or at end
        if '</body>' in content:
            content = content.replace('</body>', DISPOSITION_MODAL + '\n</body>', 1)
        else:
            content += '\n' + DISPOSITION_MODAL

    save_content(fpath, content)
    print(f"Updated: {fpath}")


process_file("customer_overview_solitaire.html")
process_file("experience_solitaire_dashboard_new.html")
print("Done!")
