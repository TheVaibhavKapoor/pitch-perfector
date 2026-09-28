import os
import re
import glob

# The old nav item to find (Project Velocity)
# We will use regex to find the whole <a href="#" class="nav-item"> ... Project Velocity ... </a> block
nav_regex = re.compile(
    r'<a href="#" class="nav-item">\s*<div class="nav-left">\s*<!-- Project Velocity.*?</svg>\s*<span>Project Velocity</span>\s*</div>\s*</a>',
    re.DOTALL | re.IGNORECASE
)

new_pitch_perfector_html = """<!-- Pitch Perfector -->
                <div class="nav-group">
                    <div class="nav-item has-dropdown dropdown-trigger">
                        <div class="nav-left">
                            <svg class="nav-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M3 21h18M3 10h18M5 10v11M9 10v11M15 10v11M19 10v11M12 3L2 10h20L12 3z"></path>
                            </svg>
                            <span>Pitch Perfector</span>
                        </div>
                        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </div>
                    <div class="submenu">
                        <a href="program_type_selection.html?program=solitaire" class="submenu-item">Solitaire</a>
                        <a href="program_type_selection.html?program=privy" class="submenu-item">Privy</a>
                        <a href="program_type_selection.html?program=privy_plus" class="submenu-item">Privy Plus</a>
                        <a href="program_type_selection.html?program=asset" class="submenu-item">Asset</a>
                    </div>
                </div>"""

# Get all html files
html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Project Velocity" in content and "Pitch Perfector" not in content:
        # replace it
        new_content, subs = nav_regex.subn(new_pitch_perfector_html, content)
        if subs > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            count += 1
            
print(f"Update complete. Modified {count} files.")
