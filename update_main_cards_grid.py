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
# NEW SMALL PRODUCT CARDS GRID HTML (INCLUDES COMPARE PROGRAM CARD)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PRODUCT_CARDS_GRID_HTML = """<div class="product-card active" onclick="showPanel('intro', this)">
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
"""

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Updating Main Cards Grid & CSS in {fname} ====================")

# 1. Update CSS for compact cards and grid
css_pattern = re.compile(r'\.product-card \{.*?height: 100%;\s*\}', re.DOTALL)
new_card_css = """.product-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 10px 14px;
            min-height: 68px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
            position: relative;
            overflow: hidden;
            transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
            cursor: pointer;
            height: 100%;
        }"""

c = css_pattern.sub(new_card_css, c)
print("Updated .product-card CSS to compact padding and min-height 68px!")

# Update icon CSS
icon_pattern = re.compile(r'\.product-icon \{.*?\}', re.DOTALL)
new_icon_css = """.product-icon {
            font-size: 1.25rem;
            width: 36px;
            height: 36px;
            min-width: 36px;
            border-radius: 10px;
            background: #f8fafc;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #f1f5f9;
        }"""

c = icon_pattern.sub(new_icon_css, c)
print("Updated .product-icon CSS to compact 36px icon box!")

# Update grid layout from repeat(3, 1fr) to repeat(auto-fit, minmax(170px, 1fr))
grid_css_pattern = re.compile(r'grid-template-columns: repeat\(3, 1fr\);')
c = grid_css_pattern.sub('grid-template-columns: repeat(auto-fit, minmax(165px, 1fr));', c)
print("Updated cards grid layout to responsive auto-fit 165px!")

# 2. Replace the HTML grid cards
cards_start = c.find('<div class="product-card"')
if cards_start != -1:
    cards_end = c.find('<!-- Info Panels -->', cards_start)
    if cards_end != -1:
        c = c[:cards_start] + NEW_PRODUCT_CARDS_GRID_HTML + "\n" + c[cards_end:]
        print("Replaced cards grid HTML with 7 compact cards (including Compare Program)!")

# 3. Remove top right "Compare Program" button to prevent redundancy
c = c.replace('<button onclick="openCompareModal()" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background=\'#f1f5f9\'" onmouseout="this.style.background=\'white\'">Compare Program</button>', '')
print("Removed redundant top right Compare Program button!")

save(fname, c)
print("Successfully saved updated experience_solitaire_dashboard_new.html!")
