with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

index = text.find('Home Loan')
if index != -1:
    print('Found Home Loan at index', index)
    print(text[index-50:index+100])
else:
    print('Not found')
