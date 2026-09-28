import re

def fix_all_depths(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    panels = ['panel-dc', 'panel-cc', 'panel-assets', 'assets-new-grid', 'panel-investments', 'panel-forex', 'panel-other', 
              'panel-business-dc', 'panel-business-cc', 'panel-business-assets', 'panel-business-investments', 'panel-business-forex', 'panel-business-other']
    
    # find offsets
    offsets = []
    for p in panels:
        idx = html.find(f'id="{p}"')
        if idx != -1:
            offsets.append((idx, p))
            
    # Also we need an end marker for the LAST panel. The last panel is 'panel-business-other'.
    # We can find where 'business-other' is supposed to end by looking for a recognizable string after it,
    # or just checking the end of the file.
    
    offsets.sort(key=lambda x: x[0])
    
    # We insert from bottom to top to preserve earlier indices
    for i in range(len(offsets) - 1, 0, -1):
        start_idx, start_name = offsets[i-1]
        end_idx, end_name = offsets[i]
        
        segment = html[start_idx:end_idx]
        opens = segment.count('<div')
        closes = segment.count('</div')
        
        depth = opens - closes
        needed = depth + 1
        
        if needed > 0:
            print(f"Fixing {start_name}: inserting {needed} closing divs before {end_name}")
            # Insert right before end_idx
            # But wait! What if there's a comment `<!-- close ... -->` right before end_idx?
            # Let's just insert before end_idx. The browser doesn't care.
            # To be slightly cleaner, we can insert before any trailing whitespace of the segment
            insertion = '</div>\n' * needed
            html = html[:end_idx] + insertion + html[end_idx:]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_all_depths('experience_solitaire_dashboard_new.html')
print("Done fixing all depths!")
