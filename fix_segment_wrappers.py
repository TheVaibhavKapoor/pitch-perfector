import re, codecs

def fix_ntb():
    with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Close segment-individual-content right after calculate benefit button
    # line near </main>
    text = text.replace('<!-- Calculate Benefit Button -->', '</div> <!-- close segment-individual-content -->\n\n                <!-- Calculate Benefit Button -->')
    with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
        f.write(text)

def fix_etb():
    with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # In ETB, segment-business-content needs to close after panel-business-other
    text = text.replace('<!-- Calculate Benefit Button -->', '</div> <!-- close segment-business-content -->\n\n                <!-- Calculate Benefit Button -->')
    with open('experience_solitaire_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(text)

fix_ntb()
fix_etb()
