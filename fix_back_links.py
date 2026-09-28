import os

files_to_check = [
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard_new.html'
]

for filename in files_to_check:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('href="solitaire.html"', 'href="/"')
        content = content.replace('href="solitaire"', 'href="/"')
        
        # In case the back button in calculate_benefit was also brought in
        content = content.replace('href="javascript:history.back()"', 'href="/"')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated back links in {filename}")
