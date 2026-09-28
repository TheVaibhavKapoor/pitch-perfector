import re

def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    panels = ['dc', 'cc', 'assets', 'investments', 'forex', 'other', 'business-dc', 'business-cc', 'business-assets', 'business-investments', 'business-forex', 'business-other']
    
    # We must process from right to left (bottom to top) to not mess up earlier indices
    
    # Find all start/end markers
    markers = []
    for p in panels:
        start_str = f'id="panel-{p}"'
        end_str = f'<!-- close panel-{p} -->'
        start = html.find(start_str)
        end = html.find(end_str)
        if start != -1 and end != -1:
            markers.append((start, end, p, end_str))
            
    markers.sort(key=lambda x: x[0], reverse=True)
    
    for start, end, p, end_str in markers:
        # segment from start to end
        segment = html[start:end]
        opens = segment.count('<div')
        closes = segment.count('</div')
        
        # We need closes = opens + 1
        needed_closes = (opens + 1) - closes
        
        if needed_closes > 0:
            print(f"Fixing {p}: inserting {needed_closes} closing divs")
            insertion = '    </div>\n' * needed_closes
            html = html[:end] + insertion + html[end:]
        elif needed_closes < 0:
            print(f"Panel {p} has TOO MANY closes by {-needed_closes}. Needs manual fix or deletion of extra closes.")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html('experience_solitaire_dashboard_new.html')
print("Done fixing HTML!")
