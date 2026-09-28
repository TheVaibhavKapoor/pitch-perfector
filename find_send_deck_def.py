import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")
# html ends at 171791 but file is 197441 - there's 25k chars after </html>!
# The send-deck-modal must be OUTSIDE the html document (at pos 159813 which is inside )
# Let's see what's at 159000-160500 to understand
pos_send_def = c.find("<!-- Send Deck Modal -->")
print(f"Send Deck Modal comment at: {pos_send_def}")
print(f"Compare modal at: {c.find('<div id=\"compare-modal\"')}")
print(f"</html> at: {c.find('</html>')}")
print(f"\nContext around send deck modal def:")
if pos_send_def != -1:
    print(c[pos_send_def:pos_send_def+500])
else:
    # Maybe it's defined differently - look for id="send-deck-modal"
    pos = c.find('id="send-deck-modal"')
    print(f"id=send-deck-modal at: {pos}")
    if pos != -1:
        print(c[pos-200:pos+500])
