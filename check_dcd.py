import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('debit_card_details.html', 'r', encoding='utf-8') as f:
    text = f.read()

print(text[:400])
