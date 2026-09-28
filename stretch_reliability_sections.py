import os
import re

file_path = 'reliability.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to close the top grid (left and right panel) before charts section.
    # Currently:
    # <div class="container">
    #     <div class="left-panel"> ... </div>
    #     <div class="right-panel">
    #         <div> Relationship Details ... </div>
    #         <div style="margin-top: 10px;"> Loan Off-Us Details ... </div>
    #         <!-- Charts Section -->
    
    # We want to change the layout.
    # Replace `<div class="container">` with `<div class="container">` (keep it, but container will just be a wrapper with padding/gap if we want, or we change .container CSS)
    # Actually, .container currently is:
    # .container {
    #     display: grid;
    #     grid-template-columns: 380px 1fr;
    #     gap: 20px;
    #     padding: 20px;
    # }
    
    # We should change .container CSS to just padding.
    # And wrap the first part in a new div with the grid layout.
    
    # 1. Update CSS
    content = content.replace(
        """.container {
            display: grid;
            grid-template-columns: 380px 1fr;
            gap: 20px;
            padding: 20px;
        }""",
        """.container {
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .top-grid {
            display: grid;
            grid-template-columns: 380px 1fr;
            gap: 20px;
        }"""
    )
    
    # 2. Update HTML structure
    content = content.replace(
        '<!-- Main Container -->\n    <div class="container">',
        '<!-- Main Container -->\n    <div class="container">\n        <div class="top-grid">'
    )
    
    content = content.replace(
        '            <!-- Charts Section -->',
        '        </div> <!-- End right-panel -->\n        </div> <!-- End top-grid -->\n\n        <!-- Charts Section -->'
    )
    
    # We also need to remove the closing div of right-panel at the very end
    # The end of the file is:
    #         </div>
    #     </div>
    # </body>
    # </html>
    
    # Let's just fix the end of the file:
    content = content.replace(
        '        </div>\n    </div>\n</body>\n</html>',
        '    </div>\n</body>\n</html>'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully restructured layout to make charts and cues full width.")
except Exception as e:
    print(f"Error: {e}")
