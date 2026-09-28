import os
import re

files_to_update = [
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard_new.html'
]

combined_html = """<div class="top-header-combined" style="background: #ffffff; border-bottom: 1px solid #e5e7eb; padding: 0 32px; display: flex; justify-content: space-between; align-items: center;">
    <div style="display: flex; gap: 32px;">
        <div class="segment-tab active" onclick="setSegment('Individual', this)" style="padding: 16px 0; font-weight: 600; color: #d61f26; border-bottom: 2px solid #d61f26; cursor: pointer;">Individual</div>
        <div class="segment-tab" onclick="setSegment('Corporate Salary', this)" style="padding: 16px 0; font-weight: 600; color: #6b7280; border-bottom: 2px solid transparent; cursor: pointer;">Corporate Salary</div>
        <div class="segment-tab" onclick="setSegment('Business', this)" style="padding: 16px 0; font-weight: 600; color: #6b7280; border-bottom: 2px solid transparent; cursor: pointer;">Business</div>
    </div>
    <div style="display: flex; gap: 12px; align-items: center;">
        <button onclick="document.getElementById('compare-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Compare Program</button>
        <button onclick="document.getElementById('send-deck-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Send Deck</button>
        <button onclick="document.getElementById('create-lead-modal').style.display='flex'" style="background: #1e3a8a; border: none; padding: 9px 20px; border-radius: 8px; font-weight: 600; color: white; cursor: pointer; box-shadow: 0 4px 12px rgba(30,58,138,0.2); transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">Create Lead</button>
    </div>
</div>"""

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the <header class="top-header"> block
        # We know it spans a few lines and ends with </header>
        header_pattern = r'<header class="top-header"[\s\S]*?</header>'
        
        # Regex to find the segment tabs div block
        # It starts with <div style="background: #ffffff; border-bottom: 1px solid #e5e7eb; padding: 0 32px; display: flex; gap: 32px;">
        # and ends with </div> right before <div class="content-body"
        segment_pattern = r'<div style="background: #ffffff; border-bottom: 1px solid #e5e7eb; padding: 0 32px; display: flex; gap: 32px;">[\s\S]*?</div>\s*(?=<div class="content-body")'

        if re.search(header_pattern, content) and re.search(segment_pattern, content):
            # Remove the segment pattern first
            content = re.sub(segment_pattern, '', content)
            # Replace the header pattern with combined_html
            content = re.sub(header_pattern, combined_html, content)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Combined row in {filename}")
        else:
            print(f"Could not find exact patterns in {filename}")
