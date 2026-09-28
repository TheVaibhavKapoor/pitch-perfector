import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== LAST 2000 CHARS ===')
print(text[-2000:])
