from bs4 import BeautifulSoup
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

panel_cc = soup.find(id='panel-cc')
# Let's see what the last element inside panel-cc is
children = list(panel_cc.find_all(recursive=False))
print('Last child of panel-cc:', children[-1].name if children else 'None')
if children:
    print('Class of last child:', children[-1].get('class'))
