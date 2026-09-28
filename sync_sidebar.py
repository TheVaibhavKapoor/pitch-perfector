import re

def update_sidebar():
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Extract nav-menu from index.html
    nav_match = re.search(r'(<nav class="nav-menu">)(.*?)(</nav>)', index_content, re.DOTALL)
    if not nav_match:
        print("Could not find nav-menu in index.html")
        return
    nav_content = nav_match.group(2)

    files_to_update = ['program_type_selection.html']

    for filepath in files_to_update:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace nav-menu in the target file
        new_content, count = re.subn(r'(<nav class="nav-menu">)(.*?)(</nav>)', r'\1' + nav_content + r'\3', content, flags=re.DOTALL)
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath} sidebar.")
        else:
            print(f"Could not update {filepath} sidebar.")

update_sidebar()
