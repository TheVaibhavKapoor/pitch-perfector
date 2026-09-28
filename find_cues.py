import glob
files = glob.glob('*.html')
for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    has_cues = 'cues' in html
    has_viewmore = 'View More' in html
    has_expanded = 'cues-expanded' in html
    if has_cues or has_viewmore or has_expanded:
        print(f'FOUND in {f}')
        print(f'  cues: {html.count("cues")}')
        print(f'  View More: {html.count("View More")}')
        print(f'  cues-expanded: {html.count("cues-expanded")}')
