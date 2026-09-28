import os

pp_best_new = r'C:\Users\vaibh\Desktop\PP BEST\experience_solitaire_dashboard_new.html'
with open(pp_best_new, 'r', encoding='utf-8') as f:
    html = f.read()

terms = ['cues', 'View More', 'cues-expanded', 'intro', 'pitches', 'SIP', 'ETB', 'NTB', 'calcul', 'Opportunity', 'opp-']
print('=== PP BEST experience_solitaire_dashboard_new.html ===')
for term in terms:
    count = html.count(term)
    print(f'  {term}: {count}')

print(f'Total lines: {len(html.splitlines())}')
print(f'Total bytes: {len(html)}')
