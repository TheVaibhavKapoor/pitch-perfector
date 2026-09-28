import os
import re

dash_file = 'experience_solitaire_dashboard_new.html'

if not os.path.exists(dash_file):
    print("File not found")
    exit()

with open(dash_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Hero Summary Card
content = re.sub(r'(\.hero-summary-card\s*\{[^}]*)padding:\s*40px;', r'\1padding: 24px;', content)
content = re.sub(r'(\.hero-summary-card\s*\{[^}]*)border-radius:\s*24px;', r'\1border-radius: 16px;', content)
content = re.sub(r'(\.hero-summary-card\s*\{[^}]*)margin-bottom:\s*40px;', r'\1margin-bottom: 24px;', content)

# Hero Badge
content = re.sub(r'(\.hero-badge\s*\{[^}]*)margin-bottom:\s*20px;', r'\1margin-bottom: 12px;', content)
content = re.sub(r'(\.hero-badge\s*\{[^}]*)padding:\s*6px 16px;', r'\1padding: 4px 12px;', content)
content = re.sub(r'(\.hero-badge\s*\{[^}]*)font-size:\s*0\.82rem;', r'\1font-size: 0.75rem;', content)

# Hero Title Row
content = re.sub(r'(\.hero-title-row\s*\{[^}]*)gap:\s*24px;', r'\1gap: 16px;', content)

# Hero Main Title H1
content = re.sub(r'(\.hero-main-title\s*h1\s*\{[^}]*)font-size:\s*1\.9rem;', r'\1font-size: 1.4rem;', content)
content = re.sub(r'(\.hero-main-title\s*h1\s*\{[^}]*)margin:\s*0 0 8px 0;', r'\1margin: 0 0 4px 0;', content)

# Hero Value Box
content = re.sub(r'(\.hero-value-box\s*\{[^}]*)padding:\s*20px 32px;', r'\1padding: 12px 20px;', content)
content = re.sub(r'(\.hero-value-box\s*\{[^}]*)border-radius:\s*20px;', r'\1border-radius: 12px;', content)

# Hero Value Amount
content = re.sub(r'(\.hero-value-amount\s*\{[^}]*)font-size:\s*2\.1rem;', r'\1font-size: 1.5rem;', content)
content = re.sub(r'(\.hero-value-label\s*\{[^}]*)font-size:\s*0\.85rem;', r'\1font-size: 0.75rem;', content)

# Bento Grid
content = re.sub(r'(\.bento-grid\s*\{[^}]*)gap:\s*20px;', r'\1gap: 16px;', content)

# Bento Card
content = re.sub(r'(\.bento-card\s*\{[^}]*)padding:\s*28px;', r'\1padding: 20px;', content)
content = re.sub(r'(\.bento-card\s*\{[^}]*)border-radius:\s*20px;', r'\1border-radius: 16px;', content)

# Bento Icon Wrapper
content = re.sub(r'(\.bento-icon-wrapper\s*\{[^}]*)width:\s*48px;', r'\1width: 40px;', content)
content = re.sub(r'(\.bento-icon-wrapper\s*\{[^}]*)height:\s*48px;', r'\1height: 40px;', content)
content = re.sub(r'(\.bento-icon-wrapper\s*\{[^}]*)font-size:\s*1\.5rem;', r'\1font-size: 1.2rem;', content)

# Bento Tag
content = re.sub(r'(\.bento-tag\s*\{[^}]*)font-size:\s*0\.75rem;', r'\1font-size: 0.65rem;', content)
content = re.sub(r'(\.bento-tag\s*\{[^}]*)padding:\s*4px 12px;', r'\1padding: 2px 8px;', content)

# Bento Card Title & Desc
content = re.sub(r'(\.bento-card-title\s*\{[^}]*)font-size:\s*1\.05rem;', r'\1font-size: 0.95rem;', content)
content = re.sub(r'(\.bento-card-desc\s*\{[^}]*)font-size:\s*0\.9rem;', r'\1font-size: 0.82rem;', content)
content = re.sub(r'(\.bento-card-desc\s*\{[^}]*)margin-bottom:\s*20px;', r'\1margin-bottom: 12px;', content)

# Bento List
content = re.sub(r'(\.bento-list\s*li\s*\{[^}]*)font-size:\s*0\.9rem;', r'\1font-size: 0.82rem;', content)
content = re.sub(r'(\.bento-list\s*li\s*\{[^}]*)margin-bottom:\s*10px;', r'\1margin-bottom: 6px;', content)

# Bento Value Tag
content = re.sub(r'(\.bento-value-tag\s*\{[^}]*)font-size:\s*0\.88rem;', r'\1font-size: 0.8rem;', content)
content = re.sub(r'(\.bento-value-tag\s*\{[^}]*)padding:\s*8px 16px;', r'\1padding: 6px 12px;', content)
content = re.sub(r'(\.bento-value-tag\s*\{[^}]*)border-radius:\s*12px;', r'\1border-radius: 8px;', content)

# Email Section
content = re.sub(r'(\.email-section-card\s*\{[^}]*)padding:\s*40px;', r'\1padding: 24px;', content)
content = re.sub(r'(\.email-section-card\s*\{[^}]*)border-radius:\s*24px;', r'\1border-radius: 16px;', content)

with open(dash_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated CSS sizes in {dash_file}")
