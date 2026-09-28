with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

privy_lines = [(i+1, line.strip()) for i, line in enumerate(lines) if 'Privy' in line]
for lineno, line in privy_lines[:30]:
    print(f'Line {lineno}: {line[:120]}')
