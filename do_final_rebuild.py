import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# ===  Extract all sections ===
main_pos = text.find('<main class="main-content">')
first_script_abs = main_pos + text[main_pos:].find('<script>')
main_close = text.find('</main>')
html_end_pos = text.find('</html>')

# Section 1: Everything before scripts (head, sidebar, main open, individual panels)
before_scripts = text[:first_script_abs]

# Section 2: All scripts
scripts_section = text[first_script_abs:main_close]

# Section 3: Orphaned business content (after </html>)
orphaned_business = text[html_end_pos + len('</html>'):].strip()

# === Fix before_scripts: it has duplicate segment-individual-content ===
# Fix: remove one duplicate  
dup_pattern = re.compile(r'(<div class="segment-wrapper active" id="segment-individual-content">)\s*\1')
before_scripts_fixed = re.sub(
    r'id="segment-individual-content">[\s\n]*<div[^>]+id="segment-individual-content">', 
    'id="segment-individual-content">',
    before_scripts
)

# === Build complete correct end of main ===
# The before_scripts ends with panel-other content. We need to:
# 1. Close panel-other properly (it currently has some stray divs at end)
# 2. Close segment-individual-content
# 3. Add business content
# 4. Add calculate button
# 5. Close content-body and main

# Looking at the end of before_scripts_fixed:
# ...locker feature card...</div></div></div></div></div></div>\n</div>  <- this is the end
# Let's count: should close panel-other(1) + product-features-grid(2) + grid-col div(3) + outer-grid(4) + panel-other(5) + segment(6) + content-body(7)

calculate_btn = '''
                <!-- Calculate Benefit Button -->
                <div style="margin-top: 48px; text-align: center;">
                    <button onclick="window.open('calculate_benefit.html', '_blank')" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; border: none; padding: 16px 32px; border-radius: 8px; font-weight: 600; font-size: 1.1rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                        CALCULATE OVERALL BENEFIT
                    </button>
                </div>
'''

# Assemble the correct file
rebuilt = (
    before_scripts_fixed.rstrip() +
    '\n' +  # close segment-individual-content  
    '\n' + orphaned_business + '\n' +  # business content
    calculate_btn +
    '\n            </div>' +  # close content-body
    '\n        </main>' +
    '\n    </div>' +
    '\n\n' + scripts_section.strip() +
    '\n\n</body>\n</html>\n'
)

with open('experience_solitaire_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(rebuilt)

print('Rebuilt experience_solitaire_dashboard.html')
print('Size:', len(rebuilt))

# Verify
panels = re.findall(r'id=\"panel-[^\"]+\"', rebuilt)
print('Panels found:', panels)
main_positions = [m.start() for m in re.finditer(r'</main>', rebuilt)]
print('</main> count:', len(main_positions))
