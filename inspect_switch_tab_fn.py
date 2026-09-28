import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()

c = get_content("experience_solitaire_dashboard_new.html")

# Find switchInnerTab function
pos = c.find("function switchInnerTab")
if pos == -1:
    pos = c.find("switchInnerTab =")
print(f"switchInnerTab at: {pos}")
if pos != -1:
    print(c[pos:pos+600])

# Count how many inner tab sets exist
sets = len(re.findall(r'inner-tabs-container', c))
print(f"\ninner-tabs-container count: {sets}")

# Check what products have tabs
matches = re.findall(r'<div class="product-card[^>]*>.*?inner-tabs-container', c, re.DOTALL)
print(f"Products with tabs: {len(matches)}")
