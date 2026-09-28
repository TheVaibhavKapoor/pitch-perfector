from bs4 import BeautifulSoup
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

calc = soup.find(id='reward-calculator')
import sys
sys.stdout.reconfigure(encoding='utf-8')
print(str(calc)[-200:])
