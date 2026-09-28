import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The structure should be:
# <div class="app-layout"> <- depth goes to 1
#   <aside>...</aside>
#   <main>...</main>
# </div> <- back to 0

# But currently at line 1340 we have </main> at depth 0 (main wasn't counted since it's not a div)
# Then </div> at line 1341 goes to -1
# This means the </div> at 1341 is the app-layout close
# AND we need the total divs to be depth=1 when we hit </main> (one app-layout div open)

# Check: where does depth hit 1 for the last time before the button?
depth = 0
lines = text.split('\n')
last_1_line = -1
for i, line in enumerate(lines, start=1):
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    depth += opens - closes
    if depth == 1 and i < 1330:
        last_1_line = i

print(f'Last time depth=1 (before line 1330): line {last_1_line}')
print('Lines around it:')
for i in range(max(0, last_1_line-3), min(len(lines), last_1_line+5)):
    print(f'  Line {i+1}: {repr(lines[i][:100])}')
