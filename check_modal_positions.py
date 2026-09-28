import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


c = get('experience_solitaire_dashboard_new.html')

# Check position of IIFE script blocks and send-deck-modal/create-lead-modal
# relative to </body>
body_end = c.find('</body>')
html_end = c.find('</html>')

# Find IIFE
iife_pos = c.find('(function(){')
if iife_pos == -1:
    iife_pos = c.find('(function() {')
print(f"IIFE at: {iife_pos}, after </body>: {iife_pos > body_end if iife_pos != -1 else 'N/A'}")

# Find send-deck-modal div
sdm_pos = c.find('id="send-deck-modal"')
print(f"send-deck-modal div at: {sdm_pos}, after </body>: {sdm_pos > body_end}")

# Find create-lead-modal div
clm_pos = c.find('id="create-lead-modal"')
print(f"create-lead-modal div at: {clm_pos}, after </body>: {clm_pos > body_end}")

# Find openSendDeckModal function definition
fn_pos = c.find('openSendDeckModal=function')
print(f"openSendDeckModal fn at: {fn_pos}, after </body>: {fn_pos > body_end if fn_pos != -1 else 'N/A'}")

fn_pos2 = c.find('window.openSendDeckModal')
print(f"window.openSendDeckModal at: {fn_pos2}, after </body>: {fn_pos2 > body_end if fn_pos2 != -1 else 'N/A'}")

print(f"\n</body> at: {body_end}")
print(f"</html> at: {html_end}")
print(f"File length: {len(c)}")

# Print what's 1000 chars before </body>
print(f"\nLast 500 chars before </body>:")
print(c[body_end-500:body_end])
