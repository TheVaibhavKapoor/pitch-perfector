import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The existing dashboard has the script tags INSIDE </main></div> at the very end
# This is wrong. The scripts should be before </body>
# Also there's a duplicate segment-individual-content div

# Check: what's the correct structure?
# Line 1174: </script>
# Line 1175: </main>  <- THIS WRAPS SCRIPTS - BAD
# Line 1176: </div></body>

# Correct would be:
# </div> <- close content-body
# </main>
# </div> <- close app-layout
# <scripts>
# </body>

# Find the main open
main_open = text.find('<main class="main-content">')
print('main opens at:', text.find('<main'), '(approx line', text[:text.find('<main')].count('\n'), ')')
print('main_close pos:', text.find('</main>'))

# Lines around line 56099 (the only </main>)
lines = text.split('\n')
main_line_num = text[:text.find('</main>')].count('\n')
print('</main> at line:', main_line_num)
print('Lines around it:')
for i in range(max(0, main_line_num - 3), min(len(lines), main_line_num + 5)):
    print(f'{i+1}: {repr(lines[i][:100])}')
