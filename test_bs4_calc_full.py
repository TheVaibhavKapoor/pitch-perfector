from bs4 import BeautifulSoup
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

calc = soup.find(id='reward-calculator')
import sys
sys.stdout.reconfigure(encoding='utf-8')
html = str(calc)
print("Length:", len(html))
print("Contains Accor?", "Accor" in html)
print("Contains Air India?", "Air India" in html)
