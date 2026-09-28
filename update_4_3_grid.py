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
# EXACT 2-ROW GRID: 4 BOXES IN UPPER ROW, 3 BOXES IN LOWER ROW
# ─────────────────────────────────────────────────────────────────────────────
NEW_4_3_GRID_HTML = """<div class="products-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 24px;">

    <!-- UPPER ROW (4 BOXES) -->
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

    <!-- LOWER ROW (3 BOXES) -->
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

    <div class="product-card" onclick="openCompareModal()" style="border: 1.5px solid #3b82f6; background: #eff6ff;">
        <div class="product-content">
            <span class="product-subtitle" style="color: #2563eb;">Program Audit</span>
            <h3 class="product-title" style="color: #1e3a8a;">Compare Program</h3>
            <span class="product-timestamp" style="color: #3b82f6;">Benchmark vs other banks</span>
        </div>
        <div class="product-icon" style="background: #dbeafe; border-color: #bfdbfe;">⚖️</div>
    </div>

</div>"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Updating Grid to Upper 4 / Lower 3 in {fname} ====================")

pos_grid_start = c.find('<div class="products-grid"')
if pos_grid_start != -1:
    pos_info_panels = c.find('<!-- Info Panels -->')
    c = c[:pos_grid_start] + NEW_4_3_GRID_HTML + "\n" + c[pos_info_panels:]
    print("Replaced products-grid with upper 4 / lower 3 grid layout!")

save(fname, c)
print("Successfully saved updated experience_solitaire_dashboard_new.html!")
