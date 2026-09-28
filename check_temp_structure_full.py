import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== temp_check.html structure ===')
print('File size:', len(text))
print('</main> count:', text.count('</main>'))

panels = re.findall(r'id=\"panel-[^\"]+\"', text)
print('Panels:', panels)

# Show the segment structure
seg = text.find('id="segment-individual-content"')
print('segment-individual-content at:', seg)

grid = text.find('class="product-grid"')
print('product-grid at:', grid)
