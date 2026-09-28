with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

panels = ['panel-dc', 'panel-cc', 'panel-assets', 'assets-new-grid', 'panel-investments', 'panel-forex', 'panel-other', 
          'panel-business-dc', 'panel-business-cc', 'panel-business-assets', 'panel-business-investments', 'panel-business-forex', 'panel-business-other']

for i in range(len(panels) - 1):
    start_name = panels[i]
    end_name = panels[i+1]
    
    start_idx = html.find(f'id="{start_name}"')
    end_idx = html.find(f'id="{end_name}"')
    
    if start_idx == -1 or end_idx == -1:
        continue
        
    segment = html[start_idx:end_idx]
    opens = segment.count('<div')
    closes = segment.count('</div')
    
    depth = opens - closes
    needed = depth + 1
    
    if needed > 0:
        print(f"Fixing {start_name}: inserting {needed} closing divs before {end_name}")
        insertion = '    </div>\n' * needed
        html = html[:end_idx] + insertion + html[end_idx:]

with open('experience_solitaire_dashboard_new.html', 'w', encoding='utf-8') as f:
    f.write(html)
