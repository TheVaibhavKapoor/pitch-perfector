import os

file_path = 'customer_overview_solitaire.html'

if not os.path.exists(file_path):
    print("File not found.")
    exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The button in customer_overview_solitaire.html currently looks like:
# <button class="btn-opp-translucent">✨ View Pitch</button>

content = content.replace(
    '<button class="btn-opp-translucent">✨ View Pitch</button>',
    '<button class="btn-opp-translucent" onclick="window.location.href=\'etb_pitch.html\'">✨ View Pitch</button>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated View Pitch button to link to etb_pitch.html")
