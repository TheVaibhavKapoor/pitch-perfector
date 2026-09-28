import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Count div opens vs closes
opens = len(re.findall(r'<div[\s>]', text))
closes = len(re.findall(r'</div>', text))
print(f'<div> opens: {opens}, </div> closes: {closes}, diff: {opens - closes}')

# The mismatch is at line 1339 </div> vs expecting </main>
# and 1340 </main> vs expecting </div>
# This means the content-body div was NOT closed before </main>
# and main closes without content-body being closed first

# The fix: the structure should have proper nesting
# We need to add the missing </div> before </main>

# Find the area around line 1339-1341
lines = text.split('\n')
print()
print('Lines 1336-1345:')
for i, l in enumerate(lines[1335:1345], start=1336):
    print(f'{i}: {repr(l)}')
