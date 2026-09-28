with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

panels = ['panel-dc', 'panel-cc', 'panel-assets', 'assets-new-grid', 'panel-investments', 'panel-forex', 'panel-other', 
          'panel-business-dc', 'panel-business-cc', 'panel-business-assets', 'panel-business-investments', 'panel-business-forex', 'panel-business-other']

# find offsets
offsets = []
for p in panels:
    idx = html.find(f'id="{p}"')
    if idx != -1:
        offsets.append((idx, p))

offsets.sort(key=lambda x: x[0])

# check depth between each
for i in range(len(offsets) - 1):
    start_idx, start_name = offsets[i]
    end_idx, end_name = offsets[i+1]
    
    segment = html[start_idx:end_idx]
    opens = segment.count('<div')
    closes = segment.count('</div')
    print(f"{start_name} -> {end_name}: opens={opens}, closes={closes}, depth={opens-closes}")
