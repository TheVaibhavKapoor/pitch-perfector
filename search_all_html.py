import os
import glob

# Search EVERY html file on the Desktop for the features
desktop = r'C:\Users\vaibh\Desktop'
all_files = glob.glob(os.path.join(desktop, '**', '*.html'), recursive=True)

print(f'Searching {len(all_files)} HTML files...\n')

for f in sorted(all_files):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            html = fp.read()
        has_cues = 'cues-expanded' in html
        has_intro_solitaire = 'intro' in html and 'solitaire' in html.lower()
        has_pitches_section = 'pitches' in html and 'info-panel' in html
        if has_cues or has_intro_solitaire or has_pitches_section:
            size = os.path.getsize(f)
            print(f'INTERESTING: {f} ({size} bytes)')
            for term in ['cues', 'cues-expanded', 'intro', 'pitches', 'SIP', 'NTB', 'ETB']:
                count = html.count(term)
                print(f'  {term}: {count}')
            print()
    except Exception as e:
        pass
