import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def save_content(fpath, content):
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


# ─────────────────────────────────────────────────────────────────────────────
# The shared modal HTML (send-deck + disposition) to inject into NTB file
# ─────────────────────────────────────────────────────────────────────────────
MODALS_BLOCK = '''
<!-- Send Deck Modal -->
<div id="send-deck-modal" style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);display:none;align-items:center;justify-content:center;z-index:9999;backdrop-filter:blur(4px);" onclick="if(event.target===this) this.style.display='none'">
    <div style="background:white;border-radius:16px;padding:32px;width:100%;max-width:500px;box-shadow:0 20px 40px rgba(0,0,0,0.1);position:relative;max-height:90vh;overflow-y:auto;">
        <button onclick="document.getElementById('send-deck-modal').style.display='none'" style="position:absolute;top:24px;right:24px;cursor:pointer;color:#64748b;font-size:1.5rem;line-height:1;border:none;background:none;padding:0;">&times;</button>
        <h3 style="font-size:1.4rem;font-weight:800;color:#0f172a;margin-bottom:8px;margin-top:0;">Send Program Deck</h3>
        <p style="color:#64748b;font-size:0.95rem;margin-bottom:24px;">Send the exclusive Solitaire program benefits deck to the client's registered email address.</p>
        <div style="margin-bottom:20px;">
            <label style="display:block;font-size:0.85rem;font-weight:600;color:#475569;margin-bottom:6px;">Registered Email Address</label>
            <input type="email" id="send-deck-email-ntb" class="ntb-modal-input" value="N/A" readonly style="background:#f1f5f9;color:#64748b;cursor:not-allowed;border-color:#cbd5e1;">
        </div>
        <button class="ntb-modal-btn" onclick="handleSendDeckNTB(this)">Send Email</button>
    </div>
</div>

<!-- Disposition Modal -->
<div id="create-lead-modal" style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);display:none;align-items:center;justify-content:center;z-index:9999;backdrop-filter:blur(4px);" onclick="if(event.target===this) this.style.display='none'">
    <div style="background:white;border-radius:16px;padding:32px;width:100%;max-width:620px;box-shadow:0 20px 40px rgba(0,0,0,0.1);position:relative;max-height:90vh;overflow-y:auto;">
        <button onclick="document.getElementById('create-lead-modal').style.display='none'" style="position:absolute;top:24px;right:24px;cursor:pointer;color:#64748b;font-size:1.5rem;line-height:1;border:none;background:none;padding:0;">&times;</button>
        <h3 style="font-size:1.4rem;font-weight:800;color:#0f172a;margin-bottom:4px;margin-top:0;">Customer Disposition</h3>
        <p style="color:#64748b;font-size:0.92rem;margin-bottom:20px;">Record the outcome of this interaction. Locked fields are pre-filled.</p>

        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:20px;">
            <div style="font-size:0.78rem;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px;">Client Details</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                <div>
                    <label style="display:block;font-size:0.8rem;font-weight:600;color:#475569;margin-bottom:4px;">Name</label>
                    <input type="text" id="disp-name-field" readonly style="width:100%;padding:9px 12px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.9rem;background:#f1f5f9;color:#64748b;cursor:not-allowed;outline:none;box-sizing:border-box;">
                </div>
                <div>
                    <label style="display:block;font-size:0.8rem;font-weight:600;color:#475569;margin-bottom:4px;">Phone</label>
                    <input type="text" id="disp-phone-field" readonly style="width:100%;padding:9px 12px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.9rem;background:#f1f5f9;color:#64748b;cursor:not-allowed;outline:none;box-sizing:border-box;">
                </div>
                <div style="grid-column:1/-1;">
                    <label style="display:block;font-size:0.8rem;font-weight:600;color:#475569;margin-bottom:4px;">Email</label>
                    <input type="text" id="disp-email-field" readonly style="width:100%;padding:9px 12px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.9rem;background:#f1f5f9;color:#64748b;cursor:not-allowed;outline:none;box-sizing:border-box;">
                </div>
            </div>
        </div>

        <div style="margin-bottom:20px;">
            <div style="font-size:0.78rem;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px;">Program Pitched</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                <div>
                    <label style="display:block;font-size:0.8rem;font-weight:600;color:#475569;margin-bottom:4px;">Program</label>
                    <select id="disp-program" style="width:100%;padding:10px 12px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:0.9rem;outline:none;font-family:inherit;box-sizing:border-box;">
                        <option value="solitaire">Solitaire</option>
                        <option value="privy_plus">Privy Plus</option>
                        <option value="privy">Privy</option>
                        <option value="asset">Asset Program</option>
                    </select>
                </div>
                <div>
                    <label style="display:block;font-size:0.8rem;font-weight:600;color:#475569;margin-bottom:4px;">Response</label>
                    <select id="disp-program-interest" onchange="toggleProgramReason()" style="width:100%;padding:10px 12px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:0.9rem;outline:none;font-family:inherit;box-sizing:border-box;">
                        <option value="interested">Interested</option>
                        <option value="not_interested">Not Interested</option>
                    </select>
                </div>
            </div>
            <div id="disp-program-reason-wrap" style="display:none;margin-top:10px;">
                <label style="display:block;font-size:0.8rem;font-weight:600;color:#475569;margin-bottom:4px;">Reason for Disinterest</label>
                <select id="disp-program-reason" style="width:100%;padding:10px 12px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:0.9rem;outline:none;font-family:inherit;box-sizing:border-box;">
                    <option value="">Select reason...</option>
                    <option>High charges / fees</option>
                    <option>Already has similar program</option>
                    <option>No immediate need</option>
                    <option>Budget constraints</option>
                    <option>Will think about it</option>
                    <option>Other</option>
                </select>
            </div>
        </div>

        <div style="margin-bottom:24px;">
            <div style="font-size:0.78rem;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px;">Product-wise Disposition</div>
            <div id="product-disp-list" style="display:flex;flex-direction:column;gap:10px;"></div>
            <button onclick="addProductRow()" style="margin-top:10px;background:transparent;border:1.5px dashed #cbd5e1;border-radius:8px;padding:8px 16px;color:#64748b;font-size:0.85rem;font-weight:600;cursor:pointer;width:100%;transition:all 0.2s;" onmouseover="this.style.borderColor='#1e3a8a';this.style.color='#1e3a8a'" onmouseout="this.style.borderColor='#cbd5e1';this.style.color='#64748b'">+ Add Product</button>
        </div>

        <button onclick="handleDisposition(this)" style="width:100%;padding:14px;background:#1e3a8a;color:white;border:none;border-radius:8px;font-weight:700;font-size:1rem;cursor:pointer;transition:background 0.2s;">Save Disposition</button>
    </div>
</div>

<script>
(function(){
    var PRODUCTS=['Savings Account','Credit Card','Home Loan','Auto Loan','Personal Loan','Demat & Trading','Fixed Deposit','Insurance','Forex Card','Current Account'];
    var REASONS=['High interest rate','Already has product','No current need','Eligibility concern','Budget constraints','Will think about it','Other'];
    var rowCount=0;

    function prodOpts(){return PRODUCTS.map(function(p){return '<option value="'+p+'">'+p+'</option>';}).join('');}
    function reasonOpts(){return '<option value="">Select reason...</option>'+REASONS.map(function(r){return '<option>'+r+'</option>';}).join('');}

    window.addProductRow=function(){
        var list=document.getElementById('product-disp-list');
        if(!list)return;
        var idx=rowCount++;
        var rowId='prod-row-'+idx;
        var intId='prod-int-'+idx;
        var rwId='prod-rw-'+idx;
        var html='<div id="'+rowId+'" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:12px;">'
            +'<div style="display:grid;grid-template-columns:1fr 1fr auto;gap:8px;align-items:end;">'
            +'<div><label style="font-size:0.78rem;font-weight:600;color:#64748b;display:block;margin-bottom:4px;">Product</label>'
            +'<select style="width:100%;padding:8px 10px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.88rem;outline:none;font-family:inherit;box-sizing:border-box;">'+prodOpts()+'</select></div>'
            +'<div><label style="font-size:0.78rem;font-weight:600;color:#64748b;display:block;margin-bottom:4px;">Response</label>'
            +'<select id="'+intId+'" onchange="toggleProductReason(\''+rwId+'\',\''+intId+'\')" style="width:100%;padding:8px 10px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.88rem;outline:none;font-family:inherit;box-sizing:border-box;">'
            +'<option value="interested">Interested</option><option value="not_interested">Not Interested</option></select></div>'
            +'<button onclick="document.getElementById(\''+rowId+'\').remove()" style="background:none;border:none;color:#ef4444;font-size:1.3rem;cursor:pointer;padding:8px 6px;line-height:1;">&times;</button>'
            +'</div>'
            +'<div id="'+rwId+'" style="display:none;margin-top:8px;">'
            +'<label style="font-size:0.78rem;font-weight:600;color:#64748b;display:block;margin-bottom:4px;">Reason</label>'
            +'<select style="width:100%;padding:8px 10px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.88rem;outline:none;font-family:inherit;box-sizing:border-box;">'+reasonOpts()+'</select>'
            +'</div></div>';
        var div=document.createElement('div');
        div.innerHTML=html;
        list.appendChild(div.firstChild);
    };

    window.toggleProgramReason=function(){
        var sel=document.getElementById('disp-program-interest');
        var wrap=document.getElementById('disp-program-reason-wrap');
        if(sel&&wrap) wrap.style.display=sel.value==='not_interested'?'block':'none';
    };

    window.toggleProductReason=function(wrapId,intId){
        var wrap=document.getElementById(wrapId);
        var sel=document.getElementById(intId);
        if(wrap&&sel) wrap.style.display=sel.value==='not_interested'?'block':'none';
    };

    window.openDispositionModal=function(){
        var nameVal=localStorage.getItem('solitaire_name')||
            (document.getElementById('disp-name')||{textContent:''}).textContent||'N/A';
        var phoneVal=localStorage.getItem('solitaire_phone')||
            (document.getElementById('disp-phone')||{textContent:''}).textContent||'N/A';
        var emailVal=localStorage.getItem('solitaire_email')||
            (document.getElementById('disp-email')||{textContent:''}).textContent||'N/A';
        var nf=document.getElementById('disp-name-field');
        var pf=document.getElementById('disp-phone-field');
        var ef=document.getElementById('disp-email-field');
        if(nf)nf.value=nameVal;
        if(pf)pf.value=phoneVal;
        if(ef)ef.value=emailVal;
        var list=document.getElementById('product-disp-list');
        if(list&&list.children.length===0) window.addProductRow();
        var m=document.getElementById('create-lead-modal');
        if(m){m.style.display='flex';}
    };

    window.openSendDeckModal=function(){
        var emailVal=localStorage.getItem('solitaire_email')||
            (document.getElementById('disp-email')||{textContent:''}).textContent||'N/A';
        var ef=document.getElementById('send-deck-email-ntb');
        if(ef)ef.value=emailVal;
        var m=document.getElementById('send-deck-modal');
        if(m){m.style.display='flex';}
    };

    window.handleSendDeckNTB=function(btn){
        btn.innerText='Sending...';btn.style.opacity='0.7';
        setTimeout(function(){
            btn.innerText='Sent Successfully!';btn.style.background='#10b981';btn.style.opacity='1';
            setTimeout(function(){
                var m=document.getElementById('send-deck-modal');
                if(m)m.style.display='none';
                btn.innerText='Send Email';btn.style.background='#1e3a8a';
            },1500);
        },1000);
    };

    window.handleDisposition=function(btn){
        btn.innerText='Saving...';btn.style.opacity='0.7';
        setTimeout(function(){
            btn.innerText='Disposition Saved!';btn.style.background='#10b981';btn.style.opacity='1';
            setTimeout(function(){
                var m=document.getElementById('create-lead-modal');
                if(m)m.style.display='none';
                btn.innerText='Save Disposition';btn.style.background='#1e3a8a';
                var list=document.getElementById('product-disp-list');
                if(list)list.innerHTML='';
                rowCount=0;
            },1500);
        },900);
    };
})();
</script>
'''


def fix_ntb_file(fpath):
    content = get_content(fpath)

    # ── 1. Fix Send Deck button: change onclick to openSendDeckModal()
    content = content.replace(
        "onclick=\"document.getElementById('send-deck-modal').style.display='flex'\"",
        "onclick=\"openSendDeckModal()\""
    )

    # ── 2. Fix Disposition button: ensure it calls openDispositionModal()
    content = content.replace(
        "onclick=\"document.getElementById('create-lead-modal').style.display='flex'\"",
        "onclick=\"openDispositionModal()\""
    )

    # ── 3. Remove existing Disposition/create-lead-modal block if it exists
    old_modal_pat = re.compile(
        r'<!-- Disposition Modal -->.*?<!-- END DISPOSITION MODAL -->',
        re.DOTALL
    )
    content = old_modal_pat.sub('', content)

    # ── 4. Also remove any old handleDisposition/sendDeck scripts already injected
    old_script_pat = re.compile(
        r'<script>\s*\(function\(\)\{.*?handleDisposition.*?\}\)\(\);\s*</script>',
        re.DOTALL
    )
    content = old_script_pat.sub('', content)

    # ── 5. Inject clean modals block just before </body> or at end of </html>
    if '</body>' in content:
        content = content.replace('</body>', MODALS_BLOCK + '\n</body>', 1)
    elif '</html>' in content:
        content = content.replace('</html>', MODALS_BLOCK + '\n</html>', 1)
    else:
        content += '\n' + MODALS_BLOCK

    save_content(fpath, content)
    print(f"Fixed: {fpath}")


fix_ntb_file("experience_solitaire_dashboard_new.html")
print("Done!")
