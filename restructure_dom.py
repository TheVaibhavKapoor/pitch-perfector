import sys
from bs4 import BeautifulSoup

def restructure_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    indiv_segment = soup.find(id='segment-individual-content')
    biz_segment = soup.find(id='segment-business-content')

    if not indiv_segment or not biz_segment:
        print("Segments not found in", filename)
        return

    indiv_panels = [
        'panel-dc', 'panel-cc', 'panel-assets', 
        'panel-investments', 'panel-forex', 'panel-other'
    ]
    
    biz_panels = [
        'panel-business-dc', 'panel-business-cc', 'panel-business-assets',
        'panel-business-investments', 'panel-business-forex', 'panel-business-other'
    ]

    for pid in indiv_panels:
        panel = soup.find(id=pid)
        if panel:
            panel.extract()
            indiv_segment.append(panel)

    for pid in biz_panels:
        panel = soup.find(id=pid)
        if panel:
            panel.extract()
            biz_segment.append(panel)

    html_out = str(soup)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print("Restructured successfully:", filename)

if len(sys.argv) > 1:
    restructure_html(sys.argv[1])
