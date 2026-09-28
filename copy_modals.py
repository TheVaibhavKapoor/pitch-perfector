import os

src_file = 'experience_solitaire_dashboard_new.html'
dst_file = 'customer_overview_solitaire.html'

if not os.path.exists(src_file) or not os.path.exists(dst_file):
    print("Files not found.")
    exit(1)

with open(src_file, 'r', encoding='utf-8') as f:
    src_content = f.read()

# Modals start at <div id="compare-modal"
# And we can just take everything up to the <script> block or the closing body tag.
import re

modals_match = re.search(r'(<div id="compare-modal".*?)(<script>|</body>)', src_content, re.DOTALL)
if modals_match:
    modals_html = modals_match.group(1)
else:
    print("Could not extract modals from src.")
    exit(1)

# Now we need to also extract the modal CSS rules so it styles correctly.
css_match = re.search(r'(/\* NTB Dashboard Modals \*/.*?)(</style>)', src_content, re.DOTALL)
if css_match:
    modals_css = css_match.group(1)
else:
    print("Could not extract modal CSS from src.")
    exit(1)

# Now inject into dst_file
with open(dst_file, 'r', encoding='utf-8') as f:
    dst_content = f.read()

# 1. Inject CSS right before </style> or at the end of <head>
if '</style>' in dst_content:
    dst_content = dst_content.replace('</style>', modals_css + '\n    </style>')
else:
    # insert before </head>
    dst_content = dst_content.replace('</head>', '<style>\n' + modals_css + '\n</style>\n</head>')

# 2. Inject HTML right before </body> or <script>
if '<script src="app.js"></script>' in dst_content:
    dst_content = dst_content.replace('<script src="app.js"></script>', modals_html + '\n    <script src="app.js"></script>')
else:
    dst_content = dst_content.replace('</body>', modals_html + '\n</body>')

with open(dst_file, 'w', encoding='utf-8') as f:
    f.write(dst_content)

print("Injected modals HTML and CSS into customer_overview_solitaire.html")
