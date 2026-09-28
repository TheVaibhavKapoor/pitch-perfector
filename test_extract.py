import re
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find where panels start and end
start_idx = text.find('<div id="panel-dc"')
end_idx = text.find('<button', start_idx)

panels = text[start_idx:end_idx]
print(len(panels))
