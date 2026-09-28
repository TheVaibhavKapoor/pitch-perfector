import os
import re

src_file = 'experience_solitaire_dashboard_new.html'
dst_file = 'customer_overview_solitaire.html'

with open(src_file, 'r', encoding='utf-8') as f:
    src_content = f.read()

# Find all modal CSS (everything from .ntb-modal-overlay down to before </style>)
css_match = re.search(r'(\.ntb-modal-overlay\s*\{.*?</style>)', src_content, re.DOTALL)
if css_match:
    modals_css = css_match.group(1).replace('</style>', '')
else:
    # Just grab all the CSS and we will inject it
    print("Could not find specific modal CSS, extracting all CSS from src")
    all_css_match = re.search(r'<style>(.*?)</style>', src_content, re.DOTALL)
    if all_css_match:
        modals_css = all_css_match.group(1)
    else:
        modals_css = ""

# Find all Modal HTML (from <!-- MODALS --> to <!-- END MODALS -->)
html_match = re.search(r'(<!-- MODALS -->.*?<!-- END MODALS -->)', src_content, re.DOTALL)
if html_match:
    modals_html = html_match.group(1)
else:
    # try another way
    modals_html_match = re.search(r'(<div id="compare-modal".*?)</body>', src_content, re.DOTALL)
    if modals_html_match:
        modals_html = modals_html_match.group(1)
        modals_html = modals_html.replace('<script src="app.js"></script>', '')
    else:
        print("Could not find HTML")
        exit(1)


with open(dst_file, 'r', encoding='utf-8') as f:
    dst_content = f.read()

# Inject CSS
if '</style>' in dst_content:
    dst_content = dst_content.replace('</style>', modals_css + '\n</style>')
else:
    dst_content = dst_content.replace('</head>', '<style>\n' + modals_css + '\n</style>\n</head>')

# Inject HTML
if '</body>' in dst_content:
    dst_content = dst_content.replace('</body>', modals_html + '\n</body>')

with open(dst_file, 'w', encoding='utf-8') as f:
    f.write(dst_content)

print("Modals copied successfully!")
