import os
import glob
import re

# Regex to find the version selector
# It looks like:
# <select id="version-selector"...>...</select>
version_regex = re.compile(r'<select\s+id="version-selector".*?</select>', re.DOTALL | re.IGNORECASE)

# Regex to find Pitch Perfector submenu inside Pitch Perfector nav-group
# We find the nav-group that has Pitch Perfector, and replace its submenu.
nav_group_regex = re.compile(
    r'(<div class="nav-item has-dropdown dropdown-trigger"[^>]*>.*?<span>Pitch Perfector</span>.*?</div>\s*<div class="submenu">)(.*?)(</div>)',
    re.DOTALL | re.IGNORECASE
)

new_submenu = """
                        <a href="program_type_selection.html?program=solitaire" class="submenu-item">Solitaire</a>
                        <a href="program_type_selection.html?program=privy" class="submenu-item">Privy</a>
                        <a href="program_type_selection.html?program=privy_plus" class="submenu-item">Privy Plus</a>
                        <a href="program_type_selection.html?program=asset" class="submenu-item">Asset</a>
                    """

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Remove version selector
    if 'id="version-selector"' in content:
        content, n = version_regex.subn('', content)
        if n > 0:
            modified = True
            
    # 2. Update Pitch Perfector submenu
    if 'Pitch Perfector' in content:
        content, n = nav_group_regex.subn(r'\g<1>' + new_submenu + r'\g<3>', content)
        if n > 0:
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

# We'll update the main files
files_to_update = [
    'index.html',
    'experience_solitaire_dashboard.html',
    'program_type_selection.html',
    'customer_overview_privy.html',
    'customer_overview_solitaire.html',
    'customer_overview.html',
    'account_details.html',
    'account_more_details.html',
    'credit_card_details.html',
    'debit_card_details.html'
]

# Try all html files
for file in glob.glob('*.html'):
    if file not in ['index_v1.html', 'index_v2.html', 'index_v3.html', 'experience_solitaire_dashboard_v1.html', 'experience_solitaire_dashboard_v2.html', 'experience_solitaire_dashboard_v3.html']:
        update_file(file)

print("Update finished.")
