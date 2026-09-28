import os
import re

with open('program_type_selection.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add id="submit-btn" to the EXPERIENCE SOLITAIRE button
if 'id="submit-btn"' not in content:
    content = content.replace('<button onclick="submitWalkthrough()" style="', '<button id="submit-btn" onclick="submitWalkthrough()" style="')

# 2. Update JS config to include button text and color
js_new_config = """        // Dynamic Program Config
        const programConfig = {
            'solitaire': {
                name: 'Kotak Solitaire',
                subtitle: 'Crafted exclusively for the select few.',
                gradient: 'linear-gradient(135deg, #CDA4A1 0%, #AA7774 25%, #814D4B 50%, #552B2A 75%, #E3CDCC 100%)',
                filter: 'drop-shadow(0 8px 12px rgba(129, 77, 75, 0.25))',
                btnText: 'EXPERIENCE SOLITAIRE',
                btnBg: '#814D4B',
                dashboardETB: 'experience_solitaire_dashboard.html',
                dashboardNTB: 'experience_solitaire_dashboard_new.html'
            },
            'privy': {
                name: 'Kotak Privy',
                subtitle: 'Premium banking for your lifestyle.',
                gradient: 'linear-gradient(135deg, #182545 0%, #263863 50%, #182545 100%)',
                filter: 'sepia(1) hue-rotate(180deg) saturate(3) brightness(0.8) drop-shadow(0 8px 12px rgba(30, 58, 138, 0.25))',
                btnText: 'EXPERIENCE PRIVY',
                btnBg: '#182545',
                dashboardETB: 'customer_overview_privy.html',
                dashboardNTB: 'customer_overview_privy.html'
            },
            'privy_plus': {
                name: 'Kotak Privy +',
                subtitle: 'Exclusive privileges. Elevated.',
                gradient: 'linear-gradient(135deg, #182545 0%, #263863 50%, #182545 100%)',
                filter: 'sepia(1) hue-rotate(180deg) saturate(3) brightness(0.8) drop-shadow(0 8px 12px rgba(30, 58, 138, 0.25))',
                btnText: 'EXPERIENCE PRIVY +',
                btnBg: '#182545',
                dashboardETB: 'customer_overview_privy.html',
                dashboardNTB: 'customer_overview_privy.html'
            },
            'asset': {
                name: 'Kotak Asset',
                subtitle: 'Grow and protect your wealth.',
                gradient: 'linear-gradient(135deg, #991b1b 0%, #dc2626 50%, #991b1b 100%)',
                filter: 'sepia(1) hue-rotate(320deg) saturate(5) brightness(0.9) drop-shadow(0 8px 12px rgba(214, 31, 38, 0.25))',
                btnText: 'EXPERIENCE ASSET',
                btnBg: '#991b1b',
                dashboardETB: 'index.html',
                dashboardNTB: 'index.html'
            }
        };"""

content = re.sub(r'// Dynamic Program Config\s+const programConfig = \{.*?\n        \};\n', js_new_config + '\n', content, flags=re.DOTALL)

# 3. Update DOMContentLoaded to set button text and background
js_update_btn = """                document.getElementById('program-subtitle').innerText = config.subtitle;
                document.getElementById('program-logo').style.filter = config.filter;
                
                const submitBtn = document.getElementById('submit-btn');
                if (submitBtn) {
                    submitBtn.innerText = config.btnText;
                    submitBtn.style.background = config.btnBg;
                    // Reset hover effect for the dynamic color
                    submitBtn.onmouseover = function() { this.style.opacity = '0.9'; this.style.transform='translateY(-2px)'; };
                    submitBtn.onmouseout = function() { this.style.opacity = '1'; this.style.transform='none'; };
                }"""

content = re.sub(r"document\.getElementById\('program-subtitle'\)\.innerText = config\.subtitle;\n\s*document\.getElementById\('program-logo'\)\.style\.filter = config\.filter;", js_update_btn, content)

# 4. Update submitWalkthrough() to use dynamic URLs
js_submit = """        function submitWalkthrough() {
            const selectedType = document.querySelector('input[name="customerType"]:checked');
            const type = selectedType ? selectedType.value : 'Existing';
            
            const urlParams = new URLSearchParams(window.location.search);
            const currentProgram = urlParams.get('program') || 'solitaire';
            const config = programConfig[currentProgram];
            
            localStorage.setItem(currentProgram + '_type', type);
            
            if (type === 'Existing') {
                const searchVal = document.getElementById('input-search').value;
                const dummyName = document.getElementById('dummy-name') ? document.getElementById('dummy-name').innerText : 'Vaibhav K';
                const dummyCrn = document.getElementById('dummy-crn') ? document.getElementById('dummy-crn').innerText : '987654321';
                
                localStorage.setItem(currentProgram + '_customer_name', dummyName);
                localStorage.setItem(currentProgram + '_customer_crn', dummyCrn);
                
                window.location.href = config.dashboardETB;
            } else {
                const name = document.getElementById('input-name').value || 'New Customer';
                
                localStorage.setItem(currentProgram + '_customer_name', name);
                localStorage.setItem(currentProgram + '_customer_crn', 'NEW-' + Math.floor(1000 + Math.random() * 9000));
                
                window.location.href = config.dashboardNTB;
            }
        }"""

content = re.sub(r'function submitWalkthrough\(\) \{.*?\n        \}', js_submit, content, flags=re.DOTALL)

with open('program_type_selection.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated button text, colors, and routing!")
