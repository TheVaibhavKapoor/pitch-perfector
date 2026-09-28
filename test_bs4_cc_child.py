from bs4 import BeautifulSoup
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

panel_cc = soup.find(id='panel-cc')
children = list(panel_cc.find_all(recursive=False))
if children:
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(str(children[-1])[:200])
