import os

file_path = 'reliability.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_html = """<div class="section-header" style="font-size: 1.1rem;">&#128221; Offers</div>
                    <div style="font-weight: 700; margin-bottom: 12px; margin-top: 16px;">Cues</div>"""

    new_html = """<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 12px; margin-top: 16px;">
                        <div>
                            <div class="section-header" style="font-size: 1.1rem; margin-bottom: 8px;">&#128221; Offers</div>
                            <div style="font-weight: 700;">Cues</div>
                        </div>
                        <button onclick="window.location.href='experience_solitaire_dashboard_new.html'" style="background: #fbbf24; border: none; color: #78350f; padding: 6px 14px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">✨ View Pitches</button>
                    </div>"""

    if old_html in content:
        content = content.replace(old_html, new_html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added View Pitches button.")
    else:
        print("Could not find the target HTML to replace.")
except Exception as e:
    print(f"Error: {e}")
