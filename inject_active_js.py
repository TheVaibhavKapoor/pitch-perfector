import sys

file_path = 'program_type_selection.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

script_to_add = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const homeLink = document.getElementById('homeLink');
            if (homeLink) {
                homeLink.classList.remove('active');
                const bar = homeLink.querySelector('.active-bar');
                if (bar) bar.remove();
            }

            const urlParamsLocal = new URLSearchParams(window.location.search);
            const currentProgram = urlParamsLocal.get('program');
            if (currentProgram) {
                const pitchHeader = document.getElementById('pitchPerfectorHeader');
                if (pitchHeader) {
                    pitchHeader.classList.add('active-header');
                    const submenu = pitchHeader.nextElementSibling;
                    if (submenu) {
                        submenu.style.maxHeight = '200px';
                        submenu.style.opacity = '1';
                        pitchHeader.setAttribute('data-open', 'true');
                        
                        const items = submenu.querySelectorAll('.submenu-item');
                        items.forEach(item => {
                            if (item.getAttribute('href').includes('program=' + currentProgram)) {
                                item.classList.add('active');
                            }
                        });
                    }
                }
            }
        });
    </script>
</body>
"""

new_content = content.replace('</body>', script_to_add)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Injected JS into program_type_selection.html")
