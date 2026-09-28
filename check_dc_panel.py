import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<div class=\"info-panel\" id=\"panel-dc\">.*?</p>)\s*<div style=\"display: grid;(.*?)(<div class=\"product-features-grid\".*?</div>\s*<!-- 4. Important Notes -->.*?</ul>\s*</div>\s*</div>)', text, re.DOTALL)
if match:
    print('Found panel-dc!')
    print('group 1:', match.group(1)[:50], '...')
    print('group 3 ends with:', match.group(3)[-50:])
else:
    print('Could not find panel-dc with this regex.')
