import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


c = get('experience_solitaire_dashboard_new.html')

# Find all inner-tabs-containers and print their button order
pat = re.compile(r'inner-tabs-container[^>]*>(.*?)</div>', re.DOTALL)
containers = list(pat.finditer(c))
for i, m in enumerate(containers):
    tabs = re.findall(r"switchInnerTab\(this,\s*'(\w+)'\)", m.group(1))
    print(f'Container {i+1}: {tabs}')

# Check active btn class
active_in_c = list(re.finditer(r'class="inner-tab-btn active"[^>]*>([^<]+)<', c))
print(f"\nActive buttons ({len(active_in_c)}):")
for m in active_in_c:
    print(f"  '{m.group(1).strip()}'")

# Content div display states
feats_b = len(re.findall(r'inner-tab-content-features" style="display: block', c))
calcs_b = len(re.findall(r'inner-tab-content-calculator" style="display: block', c))
pit_b = len(re.findall(r'inner-tab-content-pitches" style="display: block', c))
print(f'\nfeatures display:block: {feats_b}')
print(f'calculator display:block: {calcs_b}')
print(f'pitches display:block: {pit_b}')
