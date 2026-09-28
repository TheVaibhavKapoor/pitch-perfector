# -*- coding: utf-8 -*-
import os
import re

directory = r'c:\Users\vaibh\Desktop\Pitch Perfector'

# We replace solitaire_cc.html and solitaire_dc.html with experience_solitaire_dashboard.html
files_to_check = ['solitaire.html', 'customer_overview.html', 'credit_card_details.html']

for filename in files_to_check:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace links
        content = content.replace('solitaire_cc.html', 'experience_solitaire_dashboard.html')
        content = content.replace('solitaire_dc.html', 'experience_solitaire_dashboard.html')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

