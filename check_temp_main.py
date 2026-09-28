import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Main count:', text.count('</main>'))
print('Main pos:', text.find('</main>'))
print()
# Show context around the main close
pos = text.find('</main>')
print(text[pos-200:pos+200])
