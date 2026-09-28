with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# We can count divs in segment-business-content
idx1 = text.find('id="segment-business-content"')
idx2 = text.find('CALCULATE OVERALL BENEFIT', idx1)
business = text[idx1:idx2]

print('business <div:', business.count('<div'))
print('business </div:', business.count('</div'))

idx3 = text.find('id="panel-business-cc"')
idx4 = text.find('id="panel-business-assets"')
bus_cc = text[idx3:idx4]
print('business cc <div:', bus_cc.count('<div'))
print('business cc </div:', bus_cc.count('</div'))
