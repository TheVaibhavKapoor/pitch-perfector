import os
import re

with open('temp_exp.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add an ID to the elements we want to modify dynamically
content = content.replace('<img src="solitaire_3d_logo.png"', '<img id="program-logo" src="solitaire_3d_logo.png"')
content = content.replace('id="dummy-name">Vaibhav K</div>', 'id="dummy-name">Ashish Kumar</div>')
content = content.replace('Kotak Solitaire</h1>', 'Kotak Solitaire</h1>', 1)
content = re.sub(r'<h1 style="[^"]*">Kotak Solitaire</h1>', '<h1 id="program-title" style="font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #CDA4A1 0%, #AA7774 25%, #814D4B 50%, #552B2A 75%, #E3CDCC 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 12px; letter-spacing: -0.5px; transition: all 0.3s;">Kotak Solitaire</h1>', content)

content = re.sub(r'<p style="[^"]*">Crafted exclusively for the select few.</p>', '<p id="program-subtitle" style="color: #64748b; font-size: 1.15rem; margin-bottom: 48px; transition: all 0.3s;">Crafted exclusively for the select few.</p>', content)

# Inject JS before </body>
js_logic = """
        // Dynamic Program Config
        const programConfig = {
            'solitaire': {
                name: 'Kotak Solitaire',
                subtitle: 'Crafted exclusively for the select few.',
                gradient: 'linear-gradient(135deg, #CDA4A1 0%, #AA7774 25%, #814D4B 50%, #552B2A 75%, #E3CDCC 100%)',
                filter: 'drop-shadow(0 8px 12px rgba(129, 77, 75, 0.25))'
            },
            'privy': {
                name: 'Kotak Privy',
                subtitle: 'Premium banking for your lifestyle.',
                gradient: 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #1e3a8a 100%)',
                filter: 'sepia(1) hue-rotate(180deg) saturate(3) brightness(0.8) drop-shadow(0 8px 12px rgba(30, 58, 138, 0.25))'
            },
            'privy_plus': {
                name: 'Kotak Privy +',
                subtitle: 'Exclusive privileges. Elevated.',
                gradient: 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #1e3a8a 100%)',
                filter: 'sepia(1) hue-rotate(180deg) saturate(3) brightness(0.8) drop-shadow(0 8px 12px rgba(30, 58, 138, 0.25))'
            },
            'asset': {
                name: 'Kotak Asset',
                subtitle: 'Grow and protect your wealth.',
                gradient: 'linear-gradient(135deg, #991b1b 0%, #dc2626 50%, #991b1b 100%)',
                filter: 'sepia(1) hue-rotate(320deg) saturate(5) brightness(0.9) drop-shadow(0 8px 12px rgba(214, 31, 38, 0.25))'
            }
        };

        document.addEventListener('DOMContentLoaded', () => {
            const urlParams = new URLSearchParams(window.location.search);
            const currentProgram = urlParams.get('program') || 'solitaire';
            
            const config = programConfig[currentProgram];
            if (config) {
                document.getElementById('program-title').innerText = config.name;
                document.getElementById('program-title').style.background = config.gradient;
                document.getElementById('program-title').style.webkitBackgroundClip = 'text';
                document.getElementById('program-title').style.webkitTextFillColor = 'transparent';
                
                document.getElementById('program-subtitle').innerText = config.subtitle;
                document.getElementById('program-logo').style.filter = config.filter;
            }

            // Update sidebar active state
            const pitchHeader = document.getElementById('pitchPerfectorHeader');
            if (pitchHeader) {
                // Expand Pitch Perfector
                pitchHeader.classList.add('active-header');
                const submenu = pitchHeader.nextElementSibling;
                if (submenu) {
                    submenu.style.maxHeight = '200px';
                    submenu.style.opacity = '1';
                    pitchHeader.setAttribute('data-open', 'true');
                    
                    // Mark item as active
                    const items = submenu.querySelectorAll('.submenu-item');
                    items.forEach(item => {
                        if (item.getAttribute('href').includes('program=' + currentProgram)) {
                            item.classList.add('active');
                        }
                    });
                }
            }
            
            // Remove home active
            const homeLink = document.querySelector('.nav-menu > a.nav-item');
            if (homeLink) {
                homeLink.classList.remove('active');
                homeLink.style.backgroundColor = '';
                homeLink.style.color = '#64748b'; // default color
                const icon = homeLink.querySelector('.nav-icon');
                if (icon) icon.style.stroke = 'currentColor';
                const bar = homeLink.querySelector('.active-bar');
                if (bar) bar.remove();
            }
        });
"""

content = content.replace('</body>', js_logic + '\n</body>')

# Update title tag
content = re.sub(r'<title>.*?</title>', '<title>Cloud Bank - Program Selection</title>', content)

# Write to program_type_selection.html
with open('program_type_selection.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated program_type_selection.html")
