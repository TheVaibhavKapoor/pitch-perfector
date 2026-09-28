import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

# Read the existing customer dashboard
with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    existing = f.read()

print('=== experience_solitaire_dashboard.html analysis ===')
print('File size:', len(existing))
main_positions = [m.start() for m in re.finditer(r'</main>', existing)]
print('</main> count:', len(main_positions), 'at positions:', main_positions)

panels = re.findall(r'id=\"panel-[^\"]+\"', existing)
print('Panels:', panels)

main_pos = existing.find('</main>')
panel_assets_pos = existing.find('id="panel-assets"')
print('panel-assets before </main>:', panel_assets_pos < main_pos)
