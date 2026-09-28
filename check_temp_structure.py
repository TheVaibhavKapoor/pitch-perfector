import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Show what's around the end of all panels
other_start = text.find('id="panel-other"')
print('=== END OF TEMP_CHECK (after panel-other) ===')
print(text[other_start:other_start+1000])
