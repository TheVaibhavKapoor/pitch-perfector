import os
import re

files_to_update = [
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard_new.html'
]

button_html = """
        <button style="background: #f8fafc; border: 1.5px solid #cbd5e1; padding: 8px 16px; border-radius: 8px; font-weight: 600; color: #94a3b8; cursor: not-allowed; display: flex; align-items: center; gap: 6px;" title="Feature Locked">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            Open Reliability
        </button>"""

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Send Deck button and insert Open Reliability after it
    # We will search for Send Deck</button>
    pattern = r'(>Send Deck</button>)'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1' + button_html, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"Could not find Send Deck button in {file_path}")

print("All done.")
