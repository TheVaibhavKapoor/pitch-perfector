import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# === REBUILD experience_solitaire_dashboard.html ===
# 
# Current broken structure:
#   <head>...</head>
#   <body>
#     <div class="app-layout">
#       <aside>...</aside>
#       <main class="main-content">
#         segment tabs
#         <div content-body>
#           <div segment-individual-content>  (duplicated twice!)
#             product-grid + individual panels
#           </div>
#         </div>
#         <SCRIPTS>       <- wrong position
#       </main>
#       </div></body>
#     </html>
#     <orphaned business panels>  <- orphaned after </html>
#
# TARGET structure:
#   <head>...</head>
#   <body>
#     <div class="app-layout">
#       <aside>...</aside>
#       <main class="main-content">
#         segment tabs
#         <div content-body>
#           <div segment-individual-content>
#             product-grid + individual panels
#           </div>
#           <div segment-business-content>
#             business product-grid + business panels
#           </div>
#           Calculate button
#         </div>
#       </main>
#     </div>
#     <SCRIPTS>
#   </body>
# </html>

# === Step 1: Extract pieces ===

# The part before scripts (includes individual panels and their close)
main_pos = text.find('<main class="main-content">')
first_script_abs = main_pos + text[main_pos:].find('<script>')
before_scripts = text[:first_script_abs]

# All scripts up to </main>
main_close = text.find('</main>')
scripts_section = text[first_script_abs:main_close]

# The orphaned business content (after </html>)
html_end_pos = text.find('</html>')
orphaned = text[html_end_pos + len('</html>'):].strip()

# === Step 2: Calculate button (from temp_check reference) ===
calculate_btn = '''
                <!-- Calculate Benefit Button -->
                <div style="margin-top: 48px; text-align: center;">
                    <button onclick="window.open('calculate_benefit.html', '_blank')" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; border: none; padding: 16px 32px; border-radius: 8px; font-weight: 600; font-size: 1.1rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                        CALCULATE OVERALL BENEFIT
                    </button>
                </div>
'''

# === Step 3: Fix before_scripts - need to close it properly ===
# before_scripts ends with: </div>\n</div>\n</div></div>\n</div>\n
# after panel-other closes:
# The structure should be:
# </div> <- close panel-other
# ... 
# </div> <- close segment-individual-content
# Then we add business + button + close content-body + close main

# Let's see what the end of before_scripts looks like after removing trailing whitespace
before_scripts_trimmed = before_scripts.rstrip()
print('End of before_scripts (trimmed):')
print(repr(before_scripts_trimmed[-300:]))
print()

# The individual content should be wrapped properly - let's count
# Look for segment-individual-content
seg_ind = before_scripts.find('id="segment-individual-content"')
# How many times?
all_seg = [m.start() for m in re.finditer(r'id="segment-individual-content"', before_scripts)]
print('segment-individual-content in before_scripts:', len(all_seg))

# === Step 4: Assemble correct file ===
# We'll reconstruct:
# before_scripts content (individual panels) 
# + proper closing of segment-individual-content
# + orphaned business content
# + calculate button
# + close content-body and main
# + scripts
# + close body html

# Fix: before_scripts currently ends with panel-other content and some divs
# Then we need:
# </div> (content-body close)

# Actually, let's look at the real end of individual content
print()
print('Orphaned content (business) starts with:')
print(orphaned[:300])
print()
print('Scripts section length:', len(scripts_section))
