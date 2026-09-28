import re

# Read index.html for base template
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract everything up to the <div class="content-body"> tag
match = re.search(r'(.*?<div class="content-body">)', html, re.DOTALL)
if not match:
    print("Could not find content-body in index.html")
    exit(1)

head_and_sidebar = match.group(1)
# Update title
head_and_sidebar = re.sub(r'<title>.*?</title>', '<title>Cloud Bank - Program Selection</title>', head_and_sidebar)

# New content
new_content = """
                <!-- Dynamic Program Header -->
                <section class="card" style="margin-bottom: 28px; background: transparent; border: none; padding: 0; box-shadow: none;">
                    <div class="card-section-title" style="margin-bottom: 12px;">
                        <div class="section-indicator"></div>
                        <h2 style="font-size: 1.2rem; font-weight: 800; color: #0f172a; margin: 0;">Program Selection</h2>
                    </div>
                    <div style="background: linear-gradient(135deg, #132247 0%, #0a1329 100%); color: #ffffff; border-radius: 18px; padding: 24px 28px; box-shadow: 0 8px 24px rgba(19,34,71,0.25);">
                        <span style="background: rgba(255,255,255,0.18); color: #ffffff; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 12px; text-transform: uppercase; letter-spacing: 0.5px;">PITCH PERFECTOR</span>
                        <h3 id="programNameDisplay" style="font-size: 1.6rem; font-weight: 800; margin: 12px 0 0 0; color: #ffffff;">Loading Program...</h3>
                        <p style="margin: 8px 0 0 0; color: #cbd5e1; font-size: 0.95rem;">Please select the client relationship type to continue.</p>
                    </div>
                </section>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
                    <!-- ETB Card -->
                    <div class="card" onclick="handleEtbClick()" style="cursor: pointer; transition: transform 0.2s ease, box-shadow 0.2s ease; border: 2px solid transparent;" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 12px 30px rgba(0,0,0,0.1)'; this.style.borderColor='#d61f26';" onmouseout="this.style.transform='none'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.05)'; this.style.borderColor='transparent';">
                        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;">
                            <div style="background: #fee2e2; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center;">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#d61f26" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="12" cy="7" r="4"></circle>
                                </svg>
                            </div>
                            <div>
                                <h3 style="margin: 0; font-size: 1.25rem; font-weight: 700; color: #0f172a;">ETB Client</h3>
                                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: #64748b; font-weight: 600;">Existing to Bank</p>
                            </div>
                        </div>
                        <p style="color: #475569; font-size: 0.95rem; line-height: 1.5; margin: 0 0 20px 0;">
                            Client already has an existing relationship with Cloud Bank. Proceed to search their CRN or account details.
                        </p>
                        <div style="display: flex; justify-content: flex-end;">
                            <span style="color: #d61f26; font-weight: 700; font-size: 0.9rem; display: flex; align-items: center; gap: 6px;">
                                Search Customer 
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <line x1="5" y1="12" x2="19" y2="12"></line>
                                    <polyline points="12 5 19 12 12 19"></polyline>
                                </svg>
                            </span>
                        </div>
                    </div>

                    <!-- NTB Card -->
                    <div class="card" onclick="handleNtbClick()" style="cursor: pointer; transition: transform 0.2s ease, box-shadow 0.2s ease; border: 2px solid transparent;" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 12px 30px rgba(0,0,0,0.1)'; this.style.borderColor='#1e3a8a';" onmouseout="this.style.transform='none'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.05)'; this.style.borderColor='transparent';">
                        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;">
                            <div style="background: #e0e7ff; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center;">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1e3a8a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="8.5" cy="7" r="4"></circle>
                                    <line x1="20" y1="8" x2="20" y2="14"></line>
                                    <line x1="23" y1="11" x2="17" y2="11"></line>
                                </svg>
                            </div>
                            <div>
                                <h3 style="margin: 0; font-size: 1.25rem; font-weight: 700; color: #0f172a;">NTB Client</h3>
                                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: #64748b; font-weight: 600;">New to Bank</p>
                            </div>
                        </div>
                        <p style="color: #475569; font-size: 0.95rem; line-height: 1.5; margin: 0 0 20px 0;">
                            Client does not have an existing relationship. Proceed to the new customer onboarding walkthrough.
                        </p>
                        <div style="display: flex; justify-content: flex-end;">
                            <span style="color: #1e3a8a; font-weight: 700; font-size: 0.9rem; display: flex; align-items: center; gap: 6px;">
                                Start Walkthrough
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <line x1="5" y1="12" x2="19" y2="12"></line>
                                    <polyline points="12 5 19 12 12 19"></polyline>
                                </svg>
                            </span>
                        </div>
                    </div>
                </div>

                <script>
                    const urlParams = new URLSearchParams(window.location.search);
                    const program = urlParams.get('program') || 'solitaire';
                    
                    const programNames = {
                        'solitaire': 'Solitaire Program',
                        'privy': 'Privy League Program',
                        'privy_plus': 'Privy Plus Program',
                        'asset': 'Asset Program'
                    };
                    
                    document.getElementById('programNameDisplay').innerText = programNames[program] || 'Pitch Perfector';
                    
                    function handleEtbClick() {
                        // Normally ETB takes you to the customer search dashboard, but if we want to bypass search for prototype:
                        // window.location.href = `customer_overview_${program}.html`;
                        // Default to index.html for searching
                        window.location.href = 'index.html?program=' + program;
                    }
                    
                    function handleNtbClick() {
                        if (program === 'solitaire') {
                            window.location.href = 'experience_solitaire.html';
                        } else {
                            // Default fallback NTB
                            window.location.href = 'experience_solitaire.html';
                        }
                    }
                </script>
            </div>
        </main>
        
        <!-- Right Side Floating Kompanion Tab -->
        <div class="kompanion-tab">
            <span>Kompanion</span>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>
"""

full_html = head_and_sidebar + "\n" + new_content

with open('program_type_selection.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print("Created program_type_selection.html")
