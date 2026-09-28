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
# 2-ROW GRID: UPPER 4, LOWER 3 (HEADINGS ONLY, NO OTHER WRITEUPS)
# ─────────────────────────────────────────────────────────────────────────────
HEADINGS_ONLY_4_3_GRID_HTML = """<div class="products-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 24px;">

    <!-- UPPER ROW (4 BOXES) -->
    <div class="product-card active" onclick="showPanel('intro', this)" style="padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem;">Introduction</h3>
        </div>
        <div class="product-icon">👋</div>
    </div>

    <div class="product-card" onclick="showPanel('lifestyle', this)" style="padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem;">Lifestyle benefits</h3>
        </div>
        <div class="product-icon">✈️</div>
    </div>

    <div class="product-card" onclick="showPanel('cc', this)" style="padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem;">Credit Card</h3>
        </div>
        <div class="product-icon">💎</div>
    </div>

    <div class="product-card" onclick="showPanel('assets', this)" style="padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem;">Loans</h3>
        </div>
        <div class="product-icon">🏦</div>
    </div>

    <!-- LOWER ROW (3 BOXES) -->
    <div class="product-card" onclick="showPanel('investments', this)" style="padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem;">Investment</h3>
        </div>
        <div class="product-icon">📈</div>
    </div>

    <div class="product-card" onclick="showPanel('summary', this)" style="padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem;">Summary</h3>
        </div>
        <div class="product-icon">📋</div>
    </div>

    <div class="product-card" onclick="openCompareModal()" style="border: 1.5px solid #3b82f6; background: #eff6ff; padding: 14px 16px;">
        <div class="product-content">
            <h3 class="product-title" style="margin: 0; font-size: 1.05rem; color: #1e3a8a;">Compare Program</h3>
        </div>
        <div class="product-icon" style="background: #dbeafe; border-color: #bfdbfe;">⚖️</div>
    </div>

</div>"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Updating Main Cards to Headings Only in {fname} ====================")

pos_grid_start = c.find('<div class="products-grid"')
if pos_grid_start != -1:
    pos_info_panels = c.find('<!-- Info Panels -->')
    c = c[:pos_grid_start] + HEADINGS_ONLY_4_3_GRID_HTML + "\n" + c[pos_info_panels:]
    print("Replaced products-grid with headings-only upper 4 / lower 3 grid layout!")

save(fname, c)
print("Successfully saved headings-only main cards grid in experience_solitaire_dashboard_new.html!")
