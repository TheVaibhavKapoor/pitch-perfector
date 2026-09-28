import os
import re

files_to_update = [
    'customer_overview_solitaire.html',
    'experience_solitaire_dashboard_new.html'
]

for file_path in files_to_update:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern for alert('Open Reliability feature coming soon')
        content = content.replace(
            '''onclick="alert('Open Reliability feature coming soon')"''',
            '''onclick="window.location.href='reliability.html'"'''
        )
        
        # If there's an anchor tag or other type of button without the alert, we can also try a regex
        # specifically for the "Open Reliability" text if the above didn't catch it.
        # But looking at grep results, the alert was exactly what was there.

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated links in {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
