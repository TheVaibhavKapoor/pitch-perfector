import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def save_content(fpath, content):
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


content = get_content("experience_solitaire_dashboard_new.html")

# We need to reorder: Features | Calculator | Pitches → Features | Pitches | Calculator
# Each inner-tabs-container has 3 buttons in a specific order.
# We'll use regex to find and reorder each inner-tabs-container block.

# Current pattern (for each section):
# <div class="inner-tabs-container"...>
#   <button ... onclick="switchInnerTab(this, 'features')" ...>Features</button>
#   <button ... onclick="switchInnerTab(this, 'calculator')" ...>Calculator</button>
#   <button ... onclick="switchInnerTab(this, 'pitches')" ...>Pitches</button>
# </div>

# New order: Features | Pitches | Calculator
# Also need to reorder the content divs:
# inner-tab-content-features (display:block) | inner-tab-content-calculator (display:none) | inner-tab-content-pitches (display:none)
# → features (block) | pitches (none) | calculator (none)

# Strategy: find each inner-tabs-container and its 3 buttons, reorder them.
# Then find associated content divs and reorder.

def reorder_tabs_in_block(block):
    """Reorder tab buttons from Features|Calculator|Pitches to Features|Pitches|Calculator"""
    # Extract the 3 button tags
    btn_pat = re.compile(r'<button[^>]*onclick="switchInnerTab\(this,\s*\'(\w+)\'\)"[^>]*>[^<]*</button>', re.DOTALL)
    btns = btn_pat.findall(block)
    print(f"  Found tabs: {btns}")
    if set(btns) != {'features', 'calculator', 'pitches'}:
        print(f"  Skipping - unexpected tabs: {btns}")
        return block

    # Find all 3 button full elements
    btn_elements = {}
    for m in btn_pat.finditer(block):
        btn_elements[m.group(1)] = m.group(0)

    # Rebuild with new order: features, pitches, calculator
    new_order = ['features', 'pitches', 'calculator']

    # Replace the buttons in place - find the container div
    # The container is: <div class="inner-tabs-container"...> buttons </div>
    container_pat = re.compile(
        r'(<div class="inner-tabs-container"[^>]*>)(.*?)(</div>)',
        re.DOTALL
    )
    def replace_container(m):
        open_tag = m.group(1)
        buttons_html = m.group(2)
        close_tag = m.group(3)

        # Build new buttons html preserving original button styles but in new order
        # We need to preserve styles — features is 'active' (white bg), others are transparent
        # But let's extract each button's full element and reorder
        btn_full_pat = re.compile(r'<button[^>]*onclick="switchInnerTab\(this,\s*\'(\w+)\'\)"[^>]*>[^<]*</button>', re.DOTALL)
        full_btns = {m2.group(1): m2.group(0) for m2 in btn_full_pat.finditer(buttons_html)}

        if set(full_btns.keys()) != {'features', 'calculator', 'pitches'}:
            return m.group(0)

        # Ensure features stays active, others inactive
        def make_active(btn_html):
            btn_html = btn_html.replace("color: #475569;", "color: #0f172a;")
            btn_html = btn_html.replace("background: transparent;", "background: white;")
            if 'box-shadow' not in btn_html:
                btn_html = btn_html.replace("border-radius: 8px;", "border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);")
            if 'class="inner-tab-btn"' in btn_html:
                btn_html = btn_html.replace('class="inner-tab-btn"', 'class="inner-tab-btn active"')
            return btn_html

        def make_inactive(btn_html):
            btn_html = btn_html.replace("color: #0f172a;", "color: #475569;")
            btn_html = btn_html.replace("background: white;", "background: transparent;")
            btn_html = re.sub(r'box-shadow:[^;]+;', '', btn_html)
            btn_html = btn_html.replace('class="inner-tab-btn active"', 'class="inner-tab-btn"')
            return btn_html

        new_buttons = []
        for i, tab_name in enumerate(new_order):
            btn = full_btns[tab_name]
            if i == 0:
                btn = make_active(btn)
            else:
                btn = make_inactive(btn)
            new_buttons.append(btn)

        return open_tag + '\n' + '\n'.join(new_buttons) + '\n' + close_tag

    return container_pat.sub(replace_container, block, count=1)


# Process each info-panel separately
panel_pat = re.compile(r'(<div class="info-panel"[^>]*>)(.*?)((?=<div class="info-panel")|(?=</div>\s*</div>\s*</section>))', re.DOTALL)

count_reordered = 0
# Simpler approach: directly manipulate tab order in the full content for each info-panel
# Find all inner-tabs-container blocks and reorder buttons

# Step 1: Reorder the tab buttons
tab_container_pat = re.compile(
    r'(<div class="inner-tabs-container"[^>]*>)(.*?)(</div>)',
    re.DOTALL
)

def replace_tabs(m):
    global count_reordered
    open_tag = m.group(1)
    inner = m.group(2)
    close_tag = m.group(3)

    btn_pat = re.compile(r'<button[^>]*onclick="switchInnerTab\(this,\s*\'(\w+)\'\)"[^>]*>(?:[^<]*)</button>')
    found = list(btn_pat.finditer(inner))
    if len(found) != 3:
        return m.group(0)
    tab_names = [f.group(1) for f in found]
    if set(tab_names) != {'features', 'calculator', 'pitches'}:
        return m.group(0)

    btn_map = {f.group(1): f.group(0) for f in found}

    # Make features active, others not
    def set_active(btn_html, active):
        if active:
            btn_html = re.sub(r'color:\s*#475569', 'color: #0f172a', btn_html)
            btn_html = re.sub(r'background:\s*transparent', 'background: white', btn_html)
            btn_html = btn_html.replace('class="inner-tab-btn"', 'class="inner-tab-btn active"')
            if 'box-shadow' not in btn_html:
                btn_html = btn_html.replace('cursor: pointer;', 'cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1);')
        else:
            btn_html = re.sub(r'color:\s*#0f172a', 'color: #475569', btn_html)
            btn_html = re.sub(r'background:\s*white', 'background: transparent', btn_html)
            btn_html = re.sub(r'box-shadow:[^;]*;', '', btn_html)
            btn_html = btn_html.replace('class="inner-tab-btn active"', 'class="inner-tab-btn"')
        return btn_html

    new_order = ['features', 'pitches', 'calculator']
    new_inner = inner
    # Replace old buttons region with new ordered buttons
    # Find start of first button and end of last button
    start = found[0].start()
    end = found[-1].end()
    new_btns = '\n'.join([set_active(btn_map[t], i == 0) for i, t in enumerate(new_order)])
    new_inner = inner[:start] + new_btns + inner[end:]

    count_reordered += 1
    print(f"  Reordered tab container #{count_reordered}")
    return open_tag + new_inner + close_tag

content = tab_container_pat.sub(replace_tabs, content)
print(f"Total tab containers reordered: {count_reordered}")

# Step 2: Also reorder the content divs (features | calculator | pitches → features | pitches | calculator)
# The content divs appear in order after the tab buttons container.
# We need to swap the order of inner-tab-content-pitches and inner-tab-content-calculator divs.
# Also set features display:block, rest display:none

# Find all consecutive triples of inner-tab-content divs
# Pattern: inner-tab-content-features, inner-tab-content-calculator, inner-tab-content-pitches
# → swap to: features, pitches, calculator

# This is complex to do with regex on nested HTML.
# Instead, let's just ensure the display attributes are correct and note that
# browsers use CSS class-based show/hide via switchInnerTab JS, so order in DOM doesn't matter
# for functionality — but we should set features as active (display:block) and others none.

# Fix display attributes: ensure features=block, calculator=none, pitches=none
content = re.sub(
    r'(inner-tab-content-features)" style="display: none;"',
    r'\1" style="display: block;"',
    content
)
content = re.sub(
    r'(inner-tab-content-calculator)" style="display: block;"',
    r'\1" style="display: none;"',
    content
)
content = re.sub(
    r'(inner-tab-content-pitches)" style="display: block;"',
    r'\1" style="display: none;"',
    content
)

save_content("experience_solitaire_dashboard_new.html", content)
print("Done! Saved.")
