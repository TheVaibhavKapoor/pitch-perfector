import os

file_path = 'app.js'

if not os.path.exists(file_path):
    print("File not found")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the routing logic
old_routing = """        recentItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.stopPropagation();
                const type = item.getAttribute('data-type');
                if (type === 'privy') {
                    window.location.href = 'customer_overview_privy.html';
                } else if (type === 'ntb') {
                    window.location.href = 'experience_solitaire.html';
                } else {
                    window.location.href = 'customer_overview_solitaire.html';
                }
            });
        });"""

new_routing = """        recentItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.stopPropagation();
                const type = item.getAttribute('data-type');
                if (type === 'ntb') {
                    window.location.href = 'experience_solitaire_dashboard_new.html';
                } else {
                    // For Solitaire, Privy, Privy+ (all ETB)
                    window.location.href = 'customer_overview_solitaire.html';
                }
            });
        });"""

content = content.replace(old_routing, new_routing)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js ETB routing successfully!")
