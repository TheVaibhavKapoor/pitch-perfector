import os
import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the EXISTING CUSTOMER COMPARISON TABLE sections
    # It starts with <!-- EXISTING CUSTOMER COMPARISON TABLE -->
    # and ends with the </div> that closes the outer wrapper.
    # We can use a regex that matches up to the next known marker, or we can parse it carefully.
    
    # Since there are 4 types: assets, investments, forex, other
    # Let's match the block
    pattern = r'<!-- EXISTING CUSTOMER COMPARISON TABLE -->\s*<div id="[a-z]+-existing-table" style="display: none;">.*?</table>\s*</div>\s*</div>\s*</div>'
    
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)

    # Also remove the javascript that toggles it.
    js_pattern = r'const existEl = document.getElementById\(p \+ \'-existing-table\'\);\s*if \(type === \'Existing\'\) \{\s*if \(newEl\) newEl.style.display = \'none\';\s*if \(existEl\) existEl.style.display = \'block\';\s*\} else \{\s*if \(newEl\) newEl.style.display = \'block\';\s*if \(existEl\) existEl.style.display = \'none\';\s*\}'
    
    new_js = r'''if (type === 'Existing') {
                    if (newEl) newEl.style.display = 'none';
                } else {
                    if (newEl) newEl.style.display = 'block';
                }'''
    
    new_content = re.sub(js_pattern, new_js, new_content, flags=re.DOTALL)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {file}")
