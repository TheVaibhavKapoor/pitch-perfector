import re
with open('temp_check.html', 'r', encoding='utf-8') as f:
    text = f.read()
matches = re.findall(r'id="(panel-[^"]*)"', text)
print(matches)
