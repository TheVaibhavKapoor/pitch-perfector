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
# New self-contained script block for customer_overview_solitaire.html
# Replaces the old openDispositionModal + handleDisposition functions
# ─────────────────────────────────────────────────────────────────────────────
NEW_SCRIPT = '''<script>
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
        var nameEl=document.getElementById('sidebarCustName');
        var nameVal=(nameEl?nameEl.textContent.trim():'') || 'N/A';
        var nf=document.getElementById('disp-name-field');
        var pf=document.getElementById('disp-phone-field');
        var ef=document.getElementById('disp-email-field');
        if(nf)nf.value=nameVal;
        if(pf)pf.value='N/A';
        if(ef)ef.value=document.getElementById('send-deck-email')?document.getElementById('send-deck-email').value:'N/A';
        var list=document.getElementById('product-disp-list');
        if(list&&list.children.length===0) window.addProductRow();
        var m=document.getElementById('create-lead-modal');
        if(m){m.style.display='flex';}else{alert('Modal not found');}
    };

    window.handleSendDeck=function(btn){
        var email=document.getElementById('send-deck-email');
        if(!email||!email.value){alert('Please enter an email address.');return;}
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
</script>'''


def fix_etb_file(fpath):
    content = get_content(fpath)

    # Remove old scripts that define these functions (the IIFE block injected before)
    old_iife_pat = re.compile(
        r'<script>\s*\(function\(\)\s*\{.*?\}\)\(\);\s*</script>',
        re.DOTALL
    )
    content = old_iife_pat.sub('', content)

    # Remove old handleSendDeck/handleCreateLead/handleDisposition inline script if present
    old_fns_pat = re.compile(
        r'<script>\s*function handle(?:SendDeck|CreateLead|Disposition).*?</script>',
        re.DOTALL
    )
    content = old_fns_pat.sub('', content)

    # Inject new script before </body>
    if '</body>' in content:
        content = content.replace('</body>', NEW_SCRIPT + '\n</body>', 1)
    elif '</html>' in content:
        content = content.replace('</html>', NEW_SCRIPT + '\n</html>', 1)
    else:
        content += '\n' + NEW_SCRIPT

    save_content(fpath, content)
    print(f"Fixed: {fpath}")


fix_etb_file("customer_overview_solitaire.html")
print("Done!")
