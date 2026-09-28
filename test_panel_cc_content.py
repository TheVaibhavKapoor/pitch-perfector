with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="panel-cc"')
end_idx = text.find('id="panel-assets"')

panel_cc = text[idx:end_idx]
print(panel_cc[:500].encode('ascii', 'replace').decode('ascii'))
print("...")
print(panel_cc[-500:].encode('ascii', 'replace').decode('ascii'))
