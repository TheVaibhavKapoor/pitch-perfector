import os

file_path = 'program_type_selection.html'

if not os.path.exists(file_path):
    print("File not found")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace dashboardETB for solitaire
content = content.replace(
    "dashboardETB: 'experience_solitaire_dashboard.html',",
    "dashboardETB: 'customer_overview_solitaire.html',"
)
content = content.replace(
    "window.location.href='experience_solitaire_dashboard.html'",
    "window.location.href='customer_overview_solitaire.html'"
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated program_type_selection.html routing successfully!")
