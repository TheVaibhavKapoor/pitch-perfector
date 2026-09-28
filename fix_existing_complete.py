import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The file has orphaned business content after </html>
# Structure is:
# ... individual panels ...
# <script>... lots of scripts including investment calculator ...</script>
# </main>   <- WRONG: scripts should be outside main
# </div></body>
# </html>
# <div id="segment-business-content"...>  <- ORPHANED BUSINESS SECTION
# ... business panels, more scripts ...
# </body> (or end of file?)

html_end = text.find('</html>')
orphaned_business = text[html_end + len('</html>'):].strip()
before_html = text[:html_end + len('</html>')]

print('Orphaned business section starts with:')
print(orphaned_business[:200])
print()
print('Orphaned business section ends with:')
print(repr(orphaned_business[-500:]))
