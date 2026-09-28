import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

opens = len(re.findall(r'<div[\s>]', text))
closes = len(re.findall(r'</div>', text))
print(f'Opens: {opens}, Closes: {closes}, Diff: {opens-closes}')

# The structure around </main> is correct:
# depth=1 -> the ONE app-layout div is still open
# </main> closes main (not a div)
# </div> closes app-layout -> should go to 0, not -1

# If depth hits 0 before </main> but we need 1, then we have 1 extra </div> somewhere
# Find where depth hits 0 for the first time (too early)
depth = 0
lines = text.split('\n')
for i, line in enumerate(lines, start=1):
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    depth += oc - cc
    if depth == 0 and i < 990:
        print(f'Depth hits 0 early at line {i}: {repr(line[:80])}')
        break
