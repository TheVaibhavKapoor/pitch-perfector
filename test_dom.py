from bs4 import BeautifulSoup

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

el = soup.find(id='panel-assets')
if el:
    parent = el.parent
    print('Parent of panel-assets is:', parent.name, parent.get('id', 'no-id'), parent.get('class', 'no-class'))
else:
    print('Not found')
