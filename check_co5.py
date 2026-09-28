import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('customer_overview.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'href=\"(.*?\.html)\"', text)
print(set(matches))
