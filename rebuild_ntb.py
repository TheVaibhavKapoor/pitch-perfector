import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    temp = f.read()

# Get everything from temp_check EXCEPT the content body - use it for the correct panels
# The correct main section in temp_check is from the SECOND (last) </main>
main_positions = [m.start() for m in re.finditer(r'</main>', temp)]
second_main_close = main_positions[-1]

# What comes between first and second </main>?
first_main_close = main_positions[0]
between = temp[first_main_close + len('</main>'): second_main_close]
print('Content between first and last </main>:')
print(between[:500])
print('...')
print(between[-500:])
