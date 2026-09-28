with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find investments panel
search_str = 'id="panel-investments"'
idx2 = html.find(search_str)
print('panel-investments idx:', idx2)
print(html[idx2:idx2+500])
print()
# Check what's after it
search_str2 = 'id="panel-forex"'
idx3 = html.find(search_str2)
print('panel-forex idx:', idx3)
print('content between investments and forex:')
print(html[idx2:idx3][:2000])
