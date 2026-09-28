import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function showPanel')
end = text.find('}', idx+100)
print(text[idx:end+100])
