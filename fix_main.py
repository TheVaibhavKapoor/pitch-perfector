import re

files = ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Count how many </main> there are
    print(f'{filepath} has {text.count("</main>")} </main> tags')
    
    # Remove all </main> tags
    text = text.replace('</main>', '')
    
    # The actual end of the content should have </main> before </div></div></body>
    # Let's see the end of the file
    end_idx = text.rfind('</body>')
    # Actually, <main> is inside some div?
    # Let's find <main class="main-content">
    # We will just inject </main> right before the footer scripts or </body>
    # Wait, the structure is:
    # <body>
    #   <div class="sidebar">...</div>
    #   <main class="main-content"> ... </main>
    # </body>
    
    text = text.replace('</body>', '</main>\n</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print('Fixed', filepath)
