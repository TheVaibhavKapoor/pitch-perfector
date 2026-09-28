import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
# Find segment-individual-content start
pos_ind = c.find('id="segment-individual-content"')
pos_bus = c.find('id="segment-business-content"')

ind_block = c[pos_ind:pos_bus]

panels = re.findall(r'<div class="info-panel[^"]*" id="([^"]+)"', ind_block)
print(f"Info panels inside segment-individual-content ({len(panels)}):")
for p in panels:
    print("  #", p)

# Check all info panels in full file
all_panels = re.findall(r'<div class="info-panel[^"]*" id="([^"]+)"', c)
print(f"\nAll info panels in file ({len(all_panels)}):")
for p in all_panels:
    print("  #", p)
