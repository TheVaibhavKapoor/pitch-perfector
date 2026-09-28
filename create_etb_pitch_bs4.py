from bs4 import BeautifulSoup

ntb_file = 'experience_solitaire_dashboard_new.html'
etb_file = 'customer_overview_solitaire.html'
new_file = 'etb_pitch.html'

with open(ntb_file, 'r', encoding='utf-8') as f:
    ntb_soup = BeautifulSoup(f.read(), 'html.parser')

with open(etb_file, 'r', encoding='utf-8') as f:
    etb_soup = BeautifulSoup(f.read(), 'html.parser')

# Get the ETB sidebar
etb_sidebar = etb_soup.find('aside', class_='sidebar')
if not etb_sidebar:
    print("Could not find ETB sidebar")
    exit(1)

# Get the ETB top header
etb_header = etb_soup.find('header', class_='top-header')
if not etb_header:
    print("Could not find ETB top header")
    exit(1)

# In the NTB document, replace the sidebar
ntb_sidebar = ntb_soup.find('aside', class_='sidebar')
if ntb_sidebar:
    ntb_sidebar.replace_with(etb_sidebar)
else:
    print("Could not find NTB sidebar")
    exit(1)

# In the NTB document, replace the top header. NTB header is <div class="top-header-combined">
ntb_header = ntb_soup.find('div', class_='top-header-combined')
if ntb_header:
    ntb_header.replace_with(etb_header)
else:
    print("Could not find NTB top header")
    exit(1)

# Add "Back to Dashboard" button in the ETB sidebar of the new doc
exit_btn = ntb_soup.find('a', class_='exit-customer-item')
if exit_btn:
    back_btn_soup = BeautifulSoup('''
    <a href="customer_overview_solitaire.html" class="nav-item" style="color: #64748b; margin-top: auto; margin-bottom: 8px;">
        <div class="nav-left">
            <svg class="nav-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            <span style="font-weight: 600;">Back to Dashboard</span>
        </div>
    </a>
    ''', 'html.parser')
    
    # We want to insert the back button right before the exit_btn
    # But we can just append it to the nav-menu, wait exit-customer-item has margin-top: auto
    # Let's just insert it before exit-customer-item
    exit_btn.insert_before(back_btn_soup)
    
    # Since exit_btn originally had margin-top: auto, we should move margin-top: auto to the back button
    if 'margin-top: auto' in exit_btn.get('style', ''):
        exit_btn['style'] = exit_btn['style'].replace('margin-top: auto;', '')
        exit_btn['style'] = exit_btn['style'].replace('margin-top: auto', '')

with open(new_file, 'w', encoding='utf-8') as f:
    f.write(str(ntb_soup))

print("Created etb_pitch.html successfully!")
