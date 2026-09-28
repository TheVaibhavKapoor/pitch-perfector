import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

# Read both files
with open('temp_check.html', 'r', encoding='utf-8') as f:
    temp = f.read()

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    new = f.read()

# === STEP 1: Extract correctly structured main section from temp_check ===
# temp_check has 2 </main> tags due to the same bug
# We need to merge them into one correct main

main_positions = [m.start() for m in re.finditer(r'</main>', temp)]
first_main_close = main_positions[0]  # Position of first (premature) </main>
second_main_close = main_positions[-1]  # Position of last (correct) </main>

# Part A: Everything from <main> to first premature </main> - this is the CC panel etc
main_open_pos = temp.find('<main class="main-content">')
part_a = temp[main_open_pos:first_main_close]

# Part B: Everything AFTER first </main> and BEFORE second </main> - this is assets/investments/forex/other + button
# It starts with: \n\n                </div>\n\n                <div id="panel-assets"
# We need to remove that leading stray </div>
part_b_raw = temp[first_main_close + len('</main>') : second_main_close]
# Remove the leading stray </div>
part_b = re.sub(r'^\s*</div>\s*', '', part_b_raw, count=1)

# Part C: Proper closing
part_c = '\n\n        </main>\n    </div>'

# Combine: correct main = partA + partB + partC  
correct_main = part_a + '\n' + part_b + part_c

print('Correct main built. Length:', len(correct_main))
print()
print('First 300:', correct_main[:300])
print()
print('Last 300:', correct_main[-300:])

# === STEP 2: Find what to replace in experience_solitaire_dashboard_new.html ===
# Replace the current main section
new_main_open = new.find('<main class="main-content">')
new_main_close_pos = new.find('</main>')
new_after_main = new[new_main_close_pos + len('</main>'):].lstrip('\n ')
print()
print('After main in new file (first 200 chars):')
print(repr(new_after_main[:200]))

# Replace from <main> to </main>\n    </div> in new
new_main_end_full = new.find('</div>', new_main_close_pos) + len('</div>')
new_before_main = new[:new_main_open]
new_scripts_etc = new[new_main_close_pos + len('</main>'):].lstrip()
# Find start of scripts
scripts_pos = new_scripts_etc.find('<script>')

# Rebuild new file
rebuilt = new_before_main + correct_main + '\n\n    ' + new_scripts_etc

with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(rebuilt)

print()
print('experience_solitaire_dashboard_new.html rebuilt! Size:', len(rebuilt))
