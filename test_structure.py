import bs4
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

panels = soup.find_all(class_='info-panel')
for p in panels:
    print(f"Panel ID: {p.get('id')}")
    # print the parent ID to see if it's nested wrong
    print(f"  Parent: {p.parent.get('id')}")
