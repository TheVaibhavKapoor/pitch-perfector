import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The correct structure should be:
# <html>
#   <head>...</head>
#   <body>
#     <div class="app-layout">
#       <aside>...</aside>
#       <main>
#         segment tabs
#         <div content-body>
#           <div segment-individual-content>
#             product-grid + panels
#           </div>
#           <div segment-business-content>  <- currently ORPHANED after </html>
#             product-grid + panels
#           </div>
#           Calculate button
#         </div>
#       </main>
#     </div>
#     <scripts>
#   </body>
# </html>

# Step 1: Get the orphaned business section (after </html>)
html_end = text.find('</html>')
orphaned_business = text[html_end + len('</html>'):].strip()

# Step 2: Fix the main section
# Currently the </main></div></body></html> comes RIGHT AFTER the script block (incorrectly)
# We need the scripts to be OUTSIDE main
# Find the wrong </main> position
main_close_pos = text.find('</main>')
print('</main> at pos:', main_close_pos)
print('Context around </main>:')
print(repr(text[main_close_pos-100:main_close_pos+100]))
print()

# The structure before </main> should end with:
# </div>  <- close content-body  
# </main>
# </div>  <- close app-layout

# Find the scripts that come BEFORE the wrong </main>
# They should be moved to AFTER the closing div

# The text structure around the wrong end:
# </script>
# </main>
# </div></body>
# </html>

script_close = text.rfind('</script>', 0, main_close_pos)  
print('Last </script> before </main> at:', script_close)
print('Context:')
print(repr(text[script_close-20:script_close+200]))
