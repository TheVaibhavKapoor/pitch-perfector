import os

file_path = 'customer_overview_solitaire.html'

if not os.path.exists(file_path):
    print(f"File {file_path} not found.")
    exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the top header to include the 4 buttons
old_header = """            <header class="top-header">
                <div class="profile-avatar">VK</div>
            </header>"""

new_header = """            <header class="top-header" style="justify-content: flex-end; gap: 12px; align-items: center; padding: 12px 32px;">
                <div style="display: flex; gap: 12px; align-items: center; margin-right: auto;">
                    <!-- Optional left side content, leaving blank for now -->
                </div>
                <div style="display: flex; gap: 12px; align-items: center;">
                    <button onclick="document.getElementById('compare-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Compare Program</button>
                    <button onclick="document.getElementById('send-deck-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Send Deck</button>
                    <button onclick="document.getElementById('create-lead-modal').style.display='flex'" style="background: white; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #475569; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">Create Lead</button>
                    <button onclick="alert('Open Reliability feature coming soon')" style="background: #1e3a8a; border: none; padding: 9px 20px; border-radius: 8px; font-weight: 600; color: white; cursor: pointer; box-shadow: 0 4px 12px rgba(30,58,138,0.2); transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">Open Reliability</button>
                </div>
                <div class="profile-avatar" style="margin-left: 16px;">VK</div>
            </header>"""

content = content.replace(old_header, new_header)


# 2. Remove the Exclusive Offers Section
# Finding the exact block
start_marker = "<!-- Exclusive offers for Solitaire Client Header (Photo Style) -->"
end_marker = "<!-- 1. Top Summary Cards Grid (Photo 1) -->"

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    # Extract everything before start and everything from end
    content = content[:start_idx] + content[end_idx:]
else:
    print("Could not find the start or end marker for the exclusive offers section.")


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated customer_overview_solitaire.html header and removed offers section.")
