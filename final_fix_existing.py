import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# DOM errors according to HTMLParser:
# Line 1012: </div> expected </main> - this means there's an unclosed div from line 178 open inside main 
# Line 1047: </div> expected </body> - extra div close after body
# Line 1403: </main> expected </div> from line 1396 - the <div> at 1396 is unclosed
# Line 1732: </body> expected </div> from 1348 - the business content has unclosed divs

# The structure inside main according to our parser is correct (0 div diff)
# BUT HTMLParser finds issues in MIXED content structure (main inside app-layout div)

# The actual issue is deeper - the body/html checker is tracking all elements
# Let's do a more targeted analysis

# Find the <div at line 1396 (the calculate button div)
# and check if it's closed
print('Lines 1395-1405:')
for i in range(1394, min(len(lines), 1405)):
    print(f'{i+1}: {repr(lines[i])}')
