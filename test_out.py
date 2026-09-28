with open('out.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print('Has </main>:', '</main>' in text)
import sys
sys.stdout.reconfigure(encoding='utf-8')
print(text)
