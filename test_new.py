with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('CALCULATE OVERALL BENEFIT')
print(text[max(0, idx-500):idx+200].encode('ascii', 'replace').decode('ascii'))
