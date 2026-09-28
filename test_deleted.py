with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

index = text.find('Home Loan')
if index != -1:
    print(text[max(0, index-200):index+200])
