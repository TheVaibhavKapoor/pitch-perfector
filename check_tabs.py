import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# print the script block at the end
start = text.rfind('<script>')
end = text.rfind('</script>')
print(text[start:end+9])
