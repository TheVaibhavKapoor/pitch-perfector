import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


def save(f, c):
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)


CLEAN_SCRIPT = r"""<script>
(function(){
var PRODUCTS=['Savings Account','Credit Card','Home Loan','Auto Loan','Personal Loan','Demat & Trading','Fixed Deposit','Insurance','Forex Card','Current Account'];
var REASONS=['High interest rate','Already has product','No current need','Eligibility concern','Budget constraints','Will think about it','Other'];
var rowCount=0;

function prodOpts(){
    return PRODUCTS.map(function(p){return '<option value="'+p+'">'+p+'</option>';}).join('');
}
function reasonOpts(){
    return '<option value="">Select reason...</option>'+REASONS.map(function(r){return '<option>'+r+'</option>';}).join('');
}

window.addProductRow=function(){
    var list=document.getElementById('product-disp-list');
    if(!list)return;
    var idx=rowCount++;
    var rowId='prod-row-'+idx;
    var intId='prod-int-'+idx;
    var rwId='prod-rw-'+idx;
    var div=document.createElement('div');
    div.id=rowId;
    div.style.cssText='background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:12px;margin-bottom:8px;';
    div.innerHTML='<div style="display:grid;grid-template-columns:1fr 1fr auto;gap:8px;align-items:end;">'
        +'<div><label style="font-size:0.78rem;font-weight:600;color:#64748b;display:block;margin-bottom:4px;">Product</label>'
        +'<select style="width:100%;padding:8px 10px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.88rem;outline:none;font-family:inherit;box-sizing:border-box;">'+prodOpts()+'</select></div>'
        +'<div><label style="font-size:0.78rem;font-weight:600;color:#64748b;display:block;margin-bottom:4px;">Response</label>'
        +'<select id="'+intId+'" style="width:100%;padding:8px 10px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.88rem;outline:none;font-family:inherit;box-sizing:border-box;">'
        +'<option value="interested">Interested</option><option value="not_interested">Not Interested</option></select></div>'
        +'<button style="background:none;border:none;color:#ef4444;font-size:1.3rem;cursor:pointer;padding:8px 6px;line-height:1;">&times;</button>'
        +'</div>'
        +'<div id="'+rwId+'" style="display:none;margin-top:8px;">'
        +'<label style="font-size:0.78rem;font-weight:600;color:#64748b;display:block;margin-bottom:4px;">Reason</label>'
        +'<select style="width:100%;padding:8px 10px;border:1.5px solid #cbd5e1;border-radius:7px;font-size:0.88rem;outline:none;font-family:inherit;box-sizing:border-box;">'+reasonOpts()+'</select>'
        +'</div>';
    var removeBtn=div.querySelector('button');
    removeBtn.onclick=function(){div.remove();};
    var intSel=div.querySelector('#'+intId);
    var rwDiv=div.querySelector('#'+rwId);
    intSel.onchange=function(){rwDiv.style.display=this.value==='not_interested'?'block':'none';};
    list.appendChild(div);
};

window.toggleProgramReason=function(){
    var sel=document.getElementById('disp-program-interest');
    var wrap=document.getElementById('disp-program-reason-wrap');
    if(sel&&wrap) wrap.style.display=sel.value==='not_interested'?'block':'none';
};

window.openDispositionModal=function(){
    var nameEl=document.getElementById('sidebarCustName');
    var emailEl=document.getElementById('send-deck-email');
    var nf=document.getElementById('disp-name-field');
    var pf=document.getElementById('disp-phone-field');
    var ef=document.getElementById('disp-email-field');
    if(nf) nf.value=(nameEl?nameEl.textContent.trim():'')||'N/A';
    if(pf) pf.value='N/A';
    if(ef) ef.value=(emailEl?emailEl.value:'')||'N/A';
    var list=document.getElementById('product-disp-list');
    if(list&&list.children.length===0) window.addProductRow();
    var m=document.getElementById('create-lead-modal');
    if(m) m.style.display='flex';
};

window.handleSendDeck=function(btn){
    btn.innerText='Sending...';btn.style.opacity='0.7';
    setTimeout(function(){
        btn.innerText='Sent Successfully!';btn.style.background='#10b981';btn.style.opacity='1';
        setTimeout(function(){
            var m=document.getElementById('send-deck-modal');
            if(m) m.style.display='none';
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
            if(m) m.style.display='none';
            btn.innerText='Save Disposition';btn.style.background='#1e3a8a';
            var list=document.getElementById('product-disp-list');
            if(list) list.innerHTML='';
            rowCount=0;
        },1500);
    },900);
};

})();
</script>
"""

content = get('customer_overview_solitaire.html')

# Remove ALL existing IIFEs
iife_pat = re.compile(r'<script>\s*\(function\(\)\{.*?\}\)\(\);\s*</script>', re.DOTALL)
count = len(iife_pat.findall(content))
print(f"Found {count} IIFE(s) in ETB file")
content = iife_pat.sub('', content)

# Also remove standalone script blocks that define these functions
alt_pat = re.compile(r'<script>\s*(?:window\.)?(?:openDispositionModal|handleDisposition|handleSendDeck|addProductRow)\s*=.*?</script>', re.DOTALL)
count2 = len(alt_pat.findall(content))
print(f"Found {count2} standalone function script(s)")
content = alt_pat.sub('', content)

# Inject before </body>
content = content.replace('</body>', CLEAN_SCRIPT + '\n</body>', 1)
print("Injected clean script")

save('customer_overview_solitaire.html', content)
print("Saved!")

# Verify
c2 = get('customer_overview_solitaire.html')
body2 = c2.find('</body>')
html2 = c2.find('</html>')
disp_fn = c2.find('openDispositionModal=function')
send_fn = c2.find('handleSendDeck=function')
print(f"\n</body>: {body2}, </html>: {html2}")
print(f"openDispositionModal fn at: {disp_fn}, after </html>: {disp_fn > html2}")
print(f"handleSendDeck fn at: {send_fn}, after </html>: {send_fn > html2}")
print(f"send-deck-modal div: {'id=\"send-deck-modal\"' in c2}")
print(f"create-lead-modal div: {'id=\"create-lead-modal\"' in c2}")
