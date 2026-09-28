"""Move #reward-calculator div to the top of #panel-cc (after title/description, before features grid)"""

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The calculator block to move:
CALC_START = '<div id="reward-calculator"'
CALC_END_MARKER = '</div>\n                </div>\n            </div>\n<div class="info-panel" id="panel-assets">'

# We want to extract the calculator block and re-insert it
# Strategy: find the calculator start and its matching closing structure

# Find position of reward-calculator div
calc_start_pos = content.find(CALC_START)
if calc_start_pos == -1:
    print("ERROR: Could not find reward-calculator div")
    exit(1)

# The calculator ends just before the panel-assets div
# From our reading, after the calculator there are closing tags then panel-assets starts
# Let's find panel-assets and work backwards

PANEL_ASSETS_MARKER = '<div class="info-panel" id="panel-assets">'
panel_assets_pos = content.find(PANEL_ASSETS_MARKER)
if panel_assets_pos == -1:
    print("ERROR: Could not find panel-assets")
    exit(1)

# The calculator block ends somewhere before panel-assets
# Let's find the exact end: it should be </div>\n            </div>\n<div class="info-panel"
# We'll scan backwards from panel_assets_pos to find the calc end
# Based on file structure: the calc ends at line 683/684 with </div>\n                </div>\n            </div>

# Extract the calculator block
calc_block = content[calc_start_pos:panel_assets_pos]
# Trim trailing whitespace/newlines that are part of the panel container closings
# The calc block should end with </div> (close of reward-calculator)
# Then there are </div> </div> which close the cc panel and segment wrapper

# Let's be precise: find the closing </div> of reward-calculator
# reward-calculator div opened at calc_start_pos
# count open/close divs from there
depth = 0
pos = calc_start_pos
in_tag = False
end_pos = calc_start_pos
i = calc_start_pos
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
        i += 4
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            end_pos = i + 6
            break
        i += 6
    else:
        i += 1

calc_block = content[calc_start_pos:end_pos]
print(f"Calculator block: chars {calc_start_pos} to {end_pos}, length {end_pos - calc_start_pos}")
print(f"First 80 chars: {calc_block[:80]}")
print(f"Last 80 chars: {calc_block[-80:]}")

# Now find where to insert it in the CC panel
# The CC panel starts with:
CC_PANEL_START = '<div class="info-panel active" id="panel-cc">'
cc_start = content.find(CC_PANEL_START)
if cc_start == -1:
    print("ERROR: Could not find panel-cc")
    exit(1)

# After the title h2 and description p, before the feature grid div
# Target insert point: after the <p style="...">Experience unparalleled...</p>
CC_INSERT_AFTER = '<p style="color: #4b5563; line-height: 1.6; margin-bottom: 24px;">Experience unparalleled luxury and rewards with our premium metallic Solitaire Credit Card, designed exclusively for our most esteemed clients.</p>'
insert_marker_pos = content.find(CC_INSERT_AFTER, cc_start)
if insert_marker_pos == -1:
    print("ERROR: Could not find CC description paragraph")
    exit(1)

insert_pos = insert_marker_pos + len(CC_INSERT_AFTER)
print(f"Insert position: {insert_pos}")

# Remove the calculator block from its current position (add a small margin style adjustment)
# We need to adjust the margin on the calculator since it'll be at top now
calc_block_adjusted = calc_block.replace(
    'style="margin-top: 40px; margin-bottom: 40px;"',
    'style="margin-top: 24px; margin-bottom: 32px;"'
)

# Build new content: remove old calculator, insert at new position
content_without_calc = content[:calc_start_pos] + content[end_pos:]

# Find the new insert position in the modified content
new_insert_marker_pos = content_without_calc.find(CC_INSERT_AFTER, cc_start)
new_insert_pos = new_insert_marker_pos + len(CC_INSERT_AFTER)

new_content = (
    content_without_calc[:new_insert_pos] +
    '\n' + calc_block_adjusted + '\n' +
    content_without_calc[new_insert_pos:]
)

with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! Calculator moved to top of CC panel.")
