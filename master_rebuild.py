import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

# Step 1: Read temp_check.html (the reference with correct structure)
with open('temp_check.html', 'r', encoding='utf-8') as f:
    temp = f.read()

# Step 2: Get the CORRECT main section from temp_check
# temp_check has 2 </main> tags - the structure is:
# <main> ... CC panel ... </main> [orphaned: assets/investments/forex/other panels] </main>
# We need to FIX this by merging everything into ONE main section

main_positions = [m.start() for m in re.finditer(r'</main>', temp)]
first_main_close = main_positions[0]  # End of CC
second_main_close = main_positions[-1]  # Real end

# The correct main body = from <main> to first </main> MINUS the accidental early close
# Plus all the orphaned panels after first </main> and before second </main>
# Then properly closed with </main></div>

main_open_pos = temp.find('<main class="main-content">')
good_before_first_main = temp[main_open_pos:first_main_close]  # includes CC
orphaned_panels = temp[first_main_close + len('</main>') : second_main_close]  # panel-assets through other + button

# In good_before_first_main, the structure incorrectly closes early.
# It looks like:
#   ...CC content...
#   </div>  <- close point-system-footer
#   </div>  <- close panel-cc  
# </div>   <- close content-body
# </main>  <- THIS IS THE FIRST PREMATURE CLOSE
# 
# In orphaned panels: 
#   </div>  <- stray close div
#   <div id="panel-assets"...
#   ...
#   CALCULATE OVERALL BENEFIT button
#   </div>  <- close content-body
# (end of second </main>)

# Fix: Remove the premature content-body close and main close from before
# The </div>\n</main> at the end of good_before_first_main should actually be:
# (just leave the panel-cc naturally closed)
# Then append orphaned_panels but remove the leading stray </div>

# Clean up good_before_first_main: remove the trailing </div> and </main>
# It ends with: ...       </div>\n        \n\n\n
# Before that is:         </div>\n            </div>\n        \n\n\n (segment-individual-content, content-body, main)
# We need to KEEP the panel divs open and just end with panel-cc close

# Find the last </div> cluster before </main>
# good_before_first_main ends before </main>
# We want it to end after panel-cc closes naturally
# The content body should stay open

# The orphaned_panels starts with '\n\n                </div>\n\n                <div id="panel-assets"'
# That first '</div>' closes segment-individual-content or content-body prematurely

# New approach: reconstruct the full main section cleanly
clean_main = good_before_first_main
# Remove trailing whitespace closings
# The content-body div and segment-individual-content should remain open
# Find where panel-cc actually properly closes
# Look for the pattern at the end of clean_main

print('End of good_before_first_main:')
print(repr(clean_main[-300:]))
print()
print('Start of orphaned_panels:')
print(repr(orphaned_panels[:300]))
