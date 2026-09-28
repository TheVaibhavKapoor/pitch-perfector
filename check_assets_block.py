import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
pos_assets = c.find('id="panel-assets"')
pos_inv = c.find('id="panel-investments"')

block = c[pos_assets:pos_inv]

# Count div tags in block
opens = len(re.findall(r'<div[\s>]', block, re.IGNORECASE))
closes = len(re.findall(r'</div>', block, re.IGNORECASE))

print(f"Between panel-assets (pos {pos_assets}) and panel-investments (pos {pos_inv}):")
print(f"  <div count: {opens}")
print(f"  </div> count: {closes}")
print(f"  Net open divs: {opens - closes}")

# Print last 400 chars of block
print("\nLast 400 chars of panel-assets block:")
print(block[-400:])
