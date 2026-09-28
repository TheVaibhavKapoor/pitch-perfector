import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Count dc-new-grid ids (should only be 1 inside panel-dc)
matches = list(re.finditer(r'id="dc-new-grid"', text))
print(f'Found {len(matches)} dc-new-grid divs')
for m in matches:
    print(f'  pos: {m.start()}, context: {text[m.start()-100:m.start()+200]}')
    print()
