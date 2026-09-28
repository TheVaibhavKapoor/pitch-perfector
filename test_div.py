import re

for filename in ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    match = re.search(r'(<div id="panel-business-cc".*?)(?=<div id="panel-business-assets")', html, flags=re.DOTALL)
    if match:
        cc_html = match.group(1)
        open_divs = len(re.findall(r'<div\b[^>]*>', cc_html))
        close_divs = len(re.findall(r'</div>', cc_html))
        print(f"{filename} Business CC: Open divs: {open_divs}, Close divs: {close_divs}, Missing: {open_divs - close_divs}")
