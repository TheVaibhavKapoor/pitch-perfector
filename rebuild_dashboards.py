import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    temp = f.read()

# temp_check.html has 2 </main> tags - the first is the bad/duplicate, second is correct
# Let's find where each one is
main_positions = [m.start() for m in re.finditer(r'</main>', temp)]
print('</main> positions in temp_check:', main_positions)

# The panels should all be inside the ONE main block
# Let's extract the region from <main to the LAST </main>
main_open = temp.find('<main class="main-content">')
main_close = main_positions[-1]  # Last (correct) one

print('Main opens at:', main_open)
print('Main closes at:', main_close)

inner = temp[main_open: main_close + len('</main>')]
print('Inner length:', len(inner))
print()
print('First 500 chars of inner:')
print(inner[:500])
print()
print('Last 200 chars of inner:')
print(inner[-200:])
