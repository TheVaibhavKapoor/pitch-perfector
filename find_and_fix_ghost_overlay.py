import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\vaibh\Desktop\Pitch Perfector - Copy (3)"

print("=== Checking all overlay/modal divs across HTML files ===")

files_fixed = 0

for root, dirs, files in os.walk(workspace_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                c = open(filepath, 'r', encoding='utf-8', errors='ignore').read()
            except Exception as e:
                continue
            
            modified = False
            
            # Fix <div class="modal-overlay" id="homeLoanModal"> missing display:none
            if '<div class="modal-overlay" id="homeLoanModal">' in c:
                c = c.replace('<div class="modal-overlay" id="homeLoanModal">', '<div class="modal-overlay" id="homeLoanModal" style="display: none;">')
                modified = True
                print(f"Fixed homeLoanModal missing display:none in {f}")
            
            # Ensure all .ntb-modal-overlay or .modal-overlay have inline display:none if not open
            # Check for <div id="compare-modal" class="ntb-modal-overlay"> without display:none
            if '<div id="compare-modal" class="ntb-modal-overlay">' in c:
                c = c.replace('<div id="compare-modal" class="ntb-modal-overlay">', '<div id="compare-modal" class="ntb-modal-overlay" style="display: none;">')
                modified = True
                print(f"Fixed compare-modal missing display:none in {f}")
            
            # Check for any modal-overlay without display:none
            pattern = re.compile(r'(<div[^>]*class="[^"]*modal-overlay[^"]*"[^>]*>)')
            for match in pattern.finditer(c):
                div_tag = match.group(1)
                if 'display:\s*none' not in div_tag and 'display: none' not in div_tag:
                    fixed_tag = div_tag.replace('class="', 'style="display: none;" class="')
                    c = c.replace(div_tag, fixed_tag)
                    modified = True
                    print(f"Fixed modal overlay tag in {f}: {div_tag[:60]}...")
            
            # Add pointer-events & visibility rules to drawers when closed
            c = c.replace(
                'id="kompanion-drawer" style="position: fixed; right: -440px;',
                'id="kompanion-drawer" style="position: fixed; right: -440px; pointer-events: none; visibility: hidden;'
            )
            c = c.replace(
                'id="spoc-drawer" style="position: fixed; right: -440px;',
                'id="spoc-drawer" style="position: fixed; right: -440px; pointer-events: none; visibility: hidden;'
            )
            
            # Update toggle functions to manage pointer-events & visibility
            c = c.replace(
                "kDrawer.style.right = '-440px';",
                "kDrawer.style.right = '-440px'; kDrawer.style.pointerEvents = 'none'; kDrawer.style.visibility = 'hidden';"
            )
            c = c.replace(
                "kDrawer.style.right = '0px';",
                "kDrawer.style.right = '0px'; kDrawer.style.pointerEvents = 'auto'; kDrawer.style.visibility = 'visible';"
            )
            c = c.replace(
                "sDrawer.style.right = '-440px';",
                "sDrawer.style.right = '-440px'; sDrawer.style.pointerEvents = 'none'; sDrawer.style.visibility = 'hidden';"
            )
            c = c.replace(
                "sDrawer.style.right = '0px';",
                "sDrawer.style.right = '0px'; sDrawer.style.pointerEvents = 'auto'; sDrawer.style.visibility = 'visible';"
            )
            
            with open(filepath, 'w', encoding='utf-8') as fp:
                fp.write(c)
            
            files_fixed += 1

print(f"\n==================== SUCCESS: Audited and fixed all {files_fixed} HTML files! ====================")
