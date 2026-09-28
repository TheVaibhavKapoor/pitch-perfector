import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find <main> line number
main_line = None
for i, line in enumerate(lines, start=1):
    if '<main class=' in line:
        main_line = i
        break

# Track depth relative to main (starting at 0 inside main)
# main opens on line main_line, depth starts at 0
depth = 0
for i in range(main_line, len(lines)):
    line = lines[i]
    oc = len(re.findall(r'<div[\s>]', line))
    cc = len(re.findall(r'</div>', line))
    
    if '</main>' in line:
        print(f"At </main> (line {i+1}), div depth inside main = {depth}")
        if depth != 0:
            print(f"  PROBLEM: Expected depth 0, got {depth}")
        break
    
    prev = depth
    depth += oc - cc
    
    # Show every time depth reaches 0 from positive (potential segment boundary)
    if depth == 0 and prev > 0 and i+1 > main_line + 5:
        print(f"Line {i+1}: depth returns to 0 (from {prev}): {repr(line[:80])}")
    # Show every time depth goes from 0 to positive (new segment opening)  
    if depth > 0 and prev == 0 and i+1 > main_line + 5:
        print(f"Line {i+1}: depth goes positive ({prev}->{depth}): {repr(line[:80])}")
