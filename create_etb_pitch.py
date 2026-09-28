import os
import re

ntb_file = 'experience_solitaire_dashboard_new.html'
etb_file = 'customer_overview_solitaire.html'
new_file = 'etb_pitch.html'

with open(ntb_file, 'r', encoding='utf-8') as f:
    ntb_content = f.read()

with open(etb_file, 'r', encoding='utf-8') as f:
    etb_content = f.read()

# We want to create etb_pitch.html.
# It should have:
# 1. The <head> and overall structure from NTB (since it contains all the bento CSS and logic).
# 2. The left sidebar from ETB (customer_overview_solitaire.html).
# 3. The top header from ETB (which we just updated with the 4 buttons).
# 4. The main content (product grid + bento) from NTB.
# 5. All Modals from ETB or NTB (they should be identical now).

# Extract ETB sidebar
sidebar_match = re.search(r'(<aside class="sidebar customer-mode-sidebar" id="sidebar">.*?</aside>)', etb_content, re.DOTALL)
if sidebar_match:
    etb_sidebar = sidebar_match.group(1)
else:
    print("Could not find ETB sidebar")
    exit(1)

# Extract ETB top-header
header_match = re.search(r'(<header class="top-header".*?</header>)', etb_content, re.DOTALL)
if header_match:
    etb_header = header_match.group(1)
else:
    print("Could not find ETB top-header")
    exit(1)

# Now, we take NTB content and replace its sidebar and top-header
new_content = ntb_content

# Replace NTB sidebar
# NTB sidebar is <aside class="sidebar" id="sidebar"> ... </aside>
ntb_sidebar_match = re.search(r'(<aside class="sidebar".*?</aside>)', new_content, re.DOTALL)
if ntb_sidebar_match:
    new_content = new_content.replace(ntb_sidebar_match.group(1), etb_sidebar)
else:
    print("Could not find NTB sidebar to replace")

# Replace NTB top-header (in NTB it is <div class="top-header-combined" ... </div>)
ntb_header_match = re.search(r'(<div class="top-header-combined".*?</div>\s*</div>)', new_content, re.DOTALL)
if ntb_header_match:
    # Actually NTB header might be just the top-header-combined div
    pass # Wait, it's easier to just use string replacement on the known NTB header, or regex
    
# Let's use a more robust replacement for NTB header.
# In NTB, the header is right after <main class="main-content">
ntb_main_match = re.search(r'(<main class="main-content"[^>]*>)\s*(<div class="top-header-combined".*?</div>\s*</div>)', new_content, re.DOTALL)
if ntb_main_match:
    new_content = new_content.replace(ntb_main_match.group(2), etb_header)
else:
    # Fallback if structure differs
    ntb_header_match2 = re.search(r'(<div class="top-header-combined".*?</div>\s*</div>)', new_content, re.DOTALL)
    if ntb_header_match2:
        new_content = new_content.replace(ntb_header_match2.group(1), etb_header)

# In the ETB sidebar, there's a "Exit Customer Account" which goes to index.html.
# We should probably add a "Back to Dashboard" button in the ETB sidebar for this pitch page.
# Or just let them use the browser back button. Let's add a back button.
back_btn_html = """
                <a href="customer_overview_solitaire.html" class="nav-item" style="color: #64748b; margin-top: auto; margin-bottom: 8px;">
                    <div class="nav-left">
                        <svg class="nav-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                        <span style="font-weight: 600;">Back to Dashboard</span>
                    </div>
                </a>
"""
# Insert right before the exit-customer-item
new_content = new_content.replace('<a href="index.html" class="nav-item exit-customer-item"', back_btn_html + '\n                <a href="index.html" class="nav-item exit-customer-item"')

with open(new_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Created etb_pitch.html successfully!")
