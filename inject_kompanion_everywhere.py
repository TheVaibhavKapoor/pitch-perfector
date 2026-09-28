import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"

KOMPANION_COMPONENT_HTML = """
<!-- KOMPANION FLOATING SIDE TAB & DRAWER -->
<div id="kompanion-tab" onclick="toggleKompanionDrawer()" style="position: fixed; right: 0; top: 50%; transform: translateY(-50%); z-index: 9999; background: #da251c; color: white; padding: 18px 8px; border-radius: 10px 0 0 10px; font-weight: 700; font-size: 0.95rem; letter-spacing: 0.03em; cursor: pointer; box-shadow: -3px 4px 14px rgba(0,0,0,0.25); writing-mode: vertical-rl; text-orientation: mixed; user-select: none; transition: transform 0.2s ease, background 0.2s ease;" onmouseover="this.style.background='#b91c1c'" onmouseout="this.style.background='#da251c'">
    Kompanion
</div>

<!-- KOMPANION SLIDE-OUT DRAWER -->
<div id="kompanion-drawer" style="position: fixed; right: -420px; top: 0; width: 400px; height: 100vh; background: #ffffff; box-shadow: -5px 0 25px rgba(0,0,0,0.2); z-index: 10000; transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1); display: flex; flex-direction: column; font-family: system-ui, -apple-system, sans-serif;">
    <div style="background: #182545; color: white; padding: 18px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #da251c;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 32px; height: 32px; background: #da251c; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.9rem;">K</div>
            <div>
                <h3 style="margin: 0; font-size: 1.05rem; font-weight: 700;">Kotak Kompanion</h3>
                <span style="font-size: 0.72rem; color: #94a3b8;">AI Pitch & Product Assistant</span>
            </div>
        </div>
        <button onclick="toggleKompanionDrawer()" style="background: none; border: none; color: #94a3b8; font-size: 1.4rem; cursor: pointer; padding: 0 4px;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#94a3b8'">&times;</button>
    </div>
    
    <div style="flex: 1; padding: 20px; overflow-y: auto; background: #f8fafc;">
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <span style="font-size: 0.75rem; font-weight: 700; color: #da251c; text-transform: uppercase; letter-spacing: 0.05em;">RM Quick Pitch Assistant</span>
            <h4 style="margin: 6px 0 10px 0; color: #0f172a; font-size: 0.95rem;">Smart Solitaire Objections & Pitches</h4>
            <p style="font-size: 0.84rem; color: #475569; line-height: 1.5; margin-bottom: 12px;">Need quick answers during client calls? Select a product topic below to get instant talking points.</p>
            
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <button onclick="setKompanionMsg('What is the key pitch for Solitaire Credit Card?')" style="background: #eff6ff; border: 1px solid #bfdbfe; color: #1e40af; font-size: 0.78rem; padding: 6px 12px; border-radius: 20px; font-weight: 600; cursor: pointer;">Credit Card Pitch</button>
                <button onclick="setKompanionMsg('How to pitch Home Loan balance transfer to Kotak?')" style="background: #f0fdf4; border: 1px solid #bbf7d0; color: #166534; font-size: 0.78rem; padding: 6px 12px; border-radius: 20px; font-weight: 600; cursor: pointer;">Home Loan BT</button>
                <button onclick="setKompanionMsg('Why shift Mutual Fund portfolio to Kotak?')" style="background: #fefce8; border: 1px solid #fef08a; color: #854d0e; font-size: 0.78rem; padding: 6px 12px; border-radius: 20px; font-weight: 600; cursor: pointer;">Mutual Fund Shift</button>
                <button onclick="setKompanionMsg('Highlight ActivMoney auto-sweep benefits')" style="background: #faf5ff; border: 1px solid #e9d5ff; color: #6b21a8; font-size: 0.78rem; padding: 6px 12px; border-radius: 20px; font-weight: 600; cursor: pointer;">ActivMoney FD</button>
            </div>
        </div>

        <div id="kompanion-chat-log" style="display: flex; flex-direction: column; gap: 12px;">
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 14px; font-size: 0.85rem; color: #334155; line-height: 1.5;">
                👋 <strong>Hello RM!</strong> I am your <strong>Kompanion AI Assistant</strong>. Ask me anything about Kotak Solitaire privileges, lending rates, credit cards, or client objection handling!
            </div>
        </div>
    </div>

    <div style="padding: 16px 20px; background: white; border-top: 1px solid #e2e8f0; display: flex; gap: 10px;">
        <input type="text" id="kompanion-input" placeholder="Ask Kompanion a question..." style="flex: 1; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; font-size: 0.88rem; outline: none;" onkeypress="if(event.key==='Enter') sendKompanionMsg()">
        <button onclick="sendKompanionMsg()" style="background: #da251c; color: white; border: none; padding: 10px 16px; border-radius: 8px; font-weight: 700; font-size: 0.88rem; cursor: pointer;">Send</button>
    </div>
</div>

<script>
function toggleKompanionDrawer() {
    const drawer = document.getElementById('kompanion-drawer');
    if (!drawer) return;
    if (drawer.style.right === '0px') {
        drawer.style.right = '-420px';
    } else {
        drawer.style.right = '0px';
    }
}
function setKompanionMsg(msg) {
    const input = document.getElementById('kompanion-input');
    if (input) {
        input.value = msg;
        sendKompanionMsg();
    }
}
function sendKompanionMsg() {
    const input = document.getElementById('kompanion-input');
    const log = document.getElementById('kompanion-chat-log');
    if (!input || !log || !input.value.trim()) return;
    
    const query = input.value.trim();
    input.value = '';
    
    const uMsg = document.createElement('div');
    uMsg.style.cssText = 'background: #eff6ff; border: 1px solid #bfdbfe; color: #1e40af; border-radius: 12px; padding: 12px 14px; font-size: 0.85rem; align-self: flex-end; max-width: 85%; line-height: 1.4;';
    uMsg.innerHTML = '<strong>You:</strong> ' + query;
    log.appendChild(uMsg);
    
    setTimeout(() => {
        const aMsg = document.createElement('div');
        aMsg.style.cssText = 'background: white; border: 1px solid #e2e8f0; color: #0f172a; border-radius: 12px; padding: 14px; font-size: 0.85rem; line-height: 1.5; box-shadow: 0 1px 3px rgba(0,0,0,0.03);';
        
        let resp = "💡 <strong>Solitaire Insight:</strong> Kotak Solitaire offers exclusive family relationship banking, 0% Forex Markup on Credit Cards, pre-approved Home Loans up to ₹7.5 Cr with ~0.25% interest discount, and ActivMoney FD auto-sweep returns on idle savings.";
        
        if (query.toLowerCase().includes('credit card')) {
            resp = "💳 <strong>Kompanion Recommendation:</strong> Pitch the Kotak Solitaire Metal Credit Card highlighting <strong>10 Air Miles / ₹100</strong> via Kotak Unbox (1 Mile = ₹1 value), <strong>0% Forex Markup</strong> (saving ~₹14,000 per ₹4L international spend), and <strong>unlimited domestic & international lounge access</strong> for primary and add-on cardholders.";
        } else if (query.toLowerCase().includes('home loan') || query.toLowerCase().includes('bt')) {
            resp = "🏠 <strong>Kompanion Recommendation:</strong> Use Home Loan Pitch C: <em>'Sir/Ma'am, if you already have a Home Loan elsewhere, I can evaluate whether moving it to Kotak saves interest for you. At ~0.25% lower rate with zero processing fees, we can calculate your exact monthly EMI savings.'</em>";
        } else if (query.toLowerCase().includes('mutual fund')) {
            resp = "📈 <strong>Kompanion Recommendation:</strong> Start with financial objectives rather than fund names. Pitch SIP for long-term wealth or SWP for tax-efficient monthly income. Emphasize zero-AMC Demat and 0.10% delivery brokerage!";
        } else if (query.toLowerCase().includes('activmoney')) {
            resp = "⚡ <strong>Kompanion Recommendation:</strong> Highlight ActivMoney auto-sweep: idle funds above ₹25,000 are automatically converted to fixed deposits earning higher FD interest while remaining 100% liquid with zero penalty on withdrawals.";
        }
        
        aMsg.innerHTML = resp;
        log.appendChild(aMsg);
        log.scrollTop = log.scrollHeight;
    }, 400);
}
</script>
"""

count_updated = 0

for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                content = open(filepath, 'r', encoding='utf-8', errors='ignore').read()
            except Exception as e:
                print(f"Skipping {f}: {e}")
                continue
            
            # If already injected, remove old version first
            if 'id="kompanion-tab"' in content:
                content = re.sub(r'<!-- KOMPANION FLOATING SIDE TAB & DRAWER -->.*?<script>.*?</script>', '', content, flags=re.DOTALL)
            
            # Inject before </body> or at the end of file
            if '</body>' in content:
                content = content.replace('</body>', KOMPANION_COMPONENT_HTML + '\n</body>')
            else:
                content = content + '\n' + KOMPANION_COMPONENT_HTML
            
            with open(filepath, 'w', encoding='utf-8') as fp:
                fp.write(content)
            
            count_updated += 1
            print(f"Injected Kompanion tab into: {f}")

print(f"\n==================== SUCCESS: Injected Kompanion into all {count_updated} HTML pages! ====================")
