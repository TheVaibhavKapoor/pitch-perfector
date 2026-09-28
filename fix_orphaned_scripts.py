import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def save_content(fpath, content):
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


content = get_content("experience_solitaire_dashboard_new.html")
print(f"File length: {len(content)}")

body_end_pos = content.find('</body>')
html_end_pos = content.find('</html>')
print(f"</body> at: {body_end_pos}, </html> at: {html_end_pos}")

# Everything between </html> and end of file is the injected content that's broken
orphaned = content[html_end_pos + 7:]  # +7 for len('</html>')
print(f"Orphaned content length: {len(orphaned)}")
print(f"Orphaned content starts with: {orphaned[:100]}")

# The content inside </body>...</html> should be empty (just newline)
between = content[body_end_pos + 7: html_end_pos]
print(f"Between </body> and </html>: '{between[:50]}'")

# The real valid HTML is content[:body_end_pos]
# We need to:
# 1. Take valid HTML up to </body>
# 2. Append the orphaned scripts/modals
# 3. Close </body></html>

# Extract the valid body content
valid_html = content[:body_end_pos]

# Extract scripts/modals from orphaned block to move inside body
# The orphaned block should contain our modal divs + scripts

print(f"\nValid HTML ends at: {body_end_pos}")
print(f"Reconstructing file...")

new_content = valid_html + '\n' + orphaned.strip() + '\n</body>\n</html>'
save_content("experience_solitaire_dashboard_new.html", new_content)
print(f"New file length: {len(new_content)}")

# Verify
c2 = get_content("experience_solitaire_dashboard_new.html")
body2 = c2.find('</body>')
html2 = c2.find('</html>')
switch2 = c2.find('function switchInnerTab')
disp2 = c2.find('openDispositionModal')
send2 = c2.find('openSendDeckModal')
print(f"\n=== After fix ===")
print(f"</body> at: {body2}")
print(f"</html> at: {html2}")
print(f"switchInnerTab at: {switch2}, after </html>: {switch2 > html2}")
print(f"openDispositionModal at: {disp2}, after </html>: {disp2 > html2}")
print(f"openSendDeckModal at: {send2}, after </html>: {send2 > html2}")
print(f"send-deck-modal div: {'id=\"send-deck-modal\"' in c2}")
print(f"create-lead-modal div: {'id=\"create-lead-modal\"' in c2}")
