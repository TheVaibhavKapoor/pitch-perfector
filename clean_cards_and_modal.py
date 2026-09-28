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

# ─────────────────────────────────────────────────────────────────────────────
# EXACT CLEAN 7 COMPACT CARDS GRID (INCLUDING COMPARE PROGRAM)
# ─────────────────────────────────────────────────────────────────────────────
CLEAN_7_CARDS_GRID = """<div class="products-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 14px; margin-bottom: 24px;">

    <div class="product-card active" onclick="showPanel('intro', this)">
        <div class="product-content">
            <span class="product-subtitle">Overview</span>
            <h3 class="product-title">Introduction</h3>
            <span class="product-timestamp">RM & Program intro</span>
        </div>
        <div class="product-icon">👋</div>
    </div>

    <div class="product-card" onclick="showPanel('lifestyle', this)">
        <div class="product-content">
            <span class="product-subtitle">Exclusive Privileges</span>
            <h3 class="product-title">Lifestyle benefits</h3>
            <span class="product-timestamp">Travel, dining, concierge</span>
        </div>
        <div class="product-icon">✈️</div>
    </div>

    <div class="product-card" onclick="showPanel('cc', this)">
        <div class="product-content">
            <span class="product-subtitle">Metal Card</span>
            <h3 class="product-title">Credit Card</h3>
            <span class="product-timestamp">Travel & lounge benefits</span>
        </div>
        <div class="product-icon">💎</div>
    </div>

    <div class="product-card" onclick="showPanel('assets', this)">
        <div class="product-content">
            <span class="product-subtitle">Lending & Credit</span>
            <h3 class="product-title">Loans</h3>
            <span class="product-timestamp">HL, LAP, LAS, OD lines</span>
        </div>
        <div class="product-icon">🏦</div>
    </div>

    <div class="product-card" onclick="showPanel('investments', this)">
        <div class="product-content">
            <span class="product-subtitle">Wealth Growth</span>
            <h3 class="product-title">Investment</h3>
            <span class="product-timestamp">Demat, MFs, IPO, MTF</span>
        </div>
        <div class="product-icon">📈</div>
    </div>

    <div class="product-card" onclick="showPanel('summary', this)">
        <div class="product-content">
            <span class="product-subtitle">Value Analysis</span>
            <h3 class="product-title">Summary</h3>
            <span class="product-timestamp">Annual ₹2-3L+ value</span>
        </div>
        <div class="product-icon">📋</div>
    </div>

    <!-- 7. COMPARE PROGRAM CARD -->
    <div class="product-card" onclick="openCompareModal()" style="border: 1.5px solid #3b82f6; background: #eff6ff;">
        <div class="product-content">
            <span class="product-subtitle" style="color: #2563eb;">Program Audit</span>
            <h3 class="product-title" style="color: #1e3a8a;">Compare Program</h3>
            <span class="product-timestamp" style="color: #3b82f6;">Benchmark vs other banks</span>
        </div>
        <div class="product-icon" style="background: #dbeafe; border-color: #bfdbfe;">⚖️</div>
    </div>

</div>"""

# JS Function for openCompareModal, openSendDeckModal, openCreateLeadModal
JS_MODAL_FUNCTIONS = """
function openCompareModal() {
    const modal = document.getElementById('compare-modal');
    if (modal) modal.style.display = 'flex';
}
function openSendDeckModal() {
    const modal = document.getElementById('send-deck-modal');
    if (modal) modal.style.display = 'flex';
}
function openCreateLeadModal() {
    const modal = document.getElementById('create-lead-modal');
    if (modal) modal.style.display = 'flex';
}
"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Cleaning Cards Grid in {fname} ====================")

# Replace the entire region containing product cards/grid before <!-- Info Panels -->
pos_container_start = c.find('<!-- Products Grid -->')
if pos_container_start == -1:
    pos_container_start = c.find('<div class="product-card')
    div_start = c.rfind('<div', 0, pos_container_start)
    pos_container_start = div_start

pos_info_panels = c.find('<!-- Info Panels -->')

if pos_container_start != -1 and pos_info_panels != -1:
    c = c[:pos_container_start] + CLEAN_7_CARDS_GRID + "\n" + c[pos_info_panels:]
    print("Replaced all cards with clean 7 cards grid!")

# Inject JS modal functions before </body>
if "function openCompareModal" not in c:
    pos_body = c.find('</body>')
    if pos_body != -1:
        c = c[:pos_body] + f'\n<script>\n{JS_MODAL_FUNCTIONS}\n</script>\n' + c[pos_body:]
        print("Injected JS modal functions before </body>!")

save(fname, c)
print("Successfully cleaned cards grid and injected modal functions!")
