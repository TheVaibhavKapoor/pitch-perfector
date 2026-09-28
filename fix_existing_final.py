import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# === THE PROBLEM ===
# The file has: ...scripts... </script>\n</main>\n</div></body>\n</html>
# Then AFTER </html>: orphaned business panels
# Scripts are inside <main> which is wrong

# === THE FIX ===
# We need:
# 1. Business panels moved BEFORE the scripts
# 2. </main> closed AFTER all content (individual + business panels + calculate button)  
# 3. Scripts stay AFTER </main> but BEFORE </body>

# Extract orphaned business section
html_end_pos = text.find('</html>')
orphaned = text[html_end_pos + len('</html>'):].strip()
print('Orphaned business starts with:', orphaned[:100])

# Find the first <script> inside main
main_pos = text.find('<main class="main-content">')
main_close_pos = text.find('</main>')
# Find ALL <script> tags inside the main
inner = text[main_pos:main_close_pos]
first_script_in_main = inner.find('<script>')
if first_script_in_main == -1:
    print('No script inside main - good')
    first_script_abs = None
else:
    first_script_abs = main_pos + first_script_in_main
    print('First script inside main at abs pos:', first_script_abs)

# Find content_body end and where individual panels end
# The segment-individual-content div needs to be properly closed, then business content added, then button, then close content-body and main

# Strategy: 
# - Take text from start up to where scripts start inside main
# - Insert: business content wrapper + panels + button  
# - Add proper closing: </div> (content-body) </main> </div> (app-layout)
# - Then add all scripts
# - Then </body></html>

if first_script_abs:
    before_scripts = text[:first_script_abs]
    # Remove trailing whitespace at end of before_scripts but keep structure
    # The before_scripts should end with: ...calculate button... </div></div></div> 
    # (panel close, content-body close, segment-individual close)
    
    scripts_section = text[first_script_abs:main_close_pos]
    
    # Check what before_scripts ends with
    print('End of before_scripts:')
    print(repr(before_scripts[-500:]))
    print()
    print('Scripts section starts with:')
    print(scripts_section[:300])
