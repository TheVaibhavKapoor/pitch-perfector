import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Issue 1: Line 1012: </div><div class="info-panel" id="panel-other"> - panel-other div open is not on its own line
# Issue 2: Line 1046: </div></div> - double close
# Issue 3: Lines 1400-1402: calculate button div is not closed, and there's extra closing structure

# Fix: the calculate button div at line 1396 is opened with </div> but not closed
# Also the main section has unclosed divs problem

# Let's check: calculate button area
# Line 1396: <div style="margin-top: 48px; text-align: center;">
# Line 1400: </div> ... wait is that the button close?
# Actually looking again:
# 1397: <button ...> - opens button
# 1398: CALCULATE OVERALL BENEFIT
# 1399: </button>
# 1400: (space) - nothing
# 1401: (blank)
# 1402: (space) - nothing
# So the <div style="margin-top:..."> at 1396 is never closed!

# Fix 1: Add missing </div> after calculate button close
# Fix 2: Fix the double close at line 1046

# Show context at line 1046
print('Line 1046:', repr(lines[1045]))
print('Line 1047:', repr(lines[1046]))

# Check main section div balance
main_start = text.find('<main class="main-content">')
main_end = text.find('</main>')
inner = text[main_start:main_end]
oc = len(re.findall(r'<div[\s>]', inner))
cc = len(re.findall(r'</div>', inner))
print(f'Main section: opens={oc}, closes={cc}, diff={oc-cc}')

# Need to add (oc-cc) closing divs before </main>
# and remove any extras
if oc != cc:
    diff = oc - cc
    print(f'Need to add {diff} closing divs before </main>')
    
    # Find </main> and add missing divs before it
    main_close_pos = text.find('</main>')
    missing_divs = '</div>\n' * abs(diff) if diff > 0 else ''
    
    if diff > 0:
        text = text[:main_close_pos] + missing_divs + text[main_close_pos:]
    
    with open('experience_solitaire_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Fixed and saved')
