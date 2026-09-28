import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

def fix_file(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Count divs in main section
    main_start = text.find('<main class="main-content">')
    main_end = text.find('</main>')
    main_inner = text[main_start:main_end]
    oc = len(re.findall(r'<div[\s>]', main_inner))
    cc = len(re.findall(r'</div>', main_inner))
    diff = oc - cc
    print(f'{fname}: main section divs: opens={oc}, closes={cc}, diff={diff}')
    
    if diff == 0:
        print('  -> OK, no fix needed')
        return
    
    # If diff < 0, there are extra closing divs. Remove them from the end of main section.
    # They'll be right before </main>
    if diff < 0:
        extra_closes = abs(diff)
        # Remove extra </div> tags from the text right before </main>
        # Find the </main> and look backward for </div> tags to remove
        count = 0
        pos = main_end - 1
        text_list = list(text)
        removed = 0
        while removed < extra_closes and pos > main_start:
            # Find the previous </div> before main_end
            prev_close = text.rfind('</div>', main_start, main_end - removed)
            if prev_close == -1:
                break
            # Check if removing this </div> makes sense - check context
            ctx = text[prev_close-5:prev_close+15]
            # Remove this </div>
            text = text[:prev_close] + text[prev_close+6:]
            main_end -= 6  # Update main_end position
            removed += 1
            print(f'  Removed </div> at pos {prev_close}')
        
        # Verify
        main_inner2 = text[text.find('<main class="main-content">'): text.find('</main>')]
        oc2 = len(re.findall(r'<div[\s>]', main_inner2))
        cc2 = len(re.findall(r'</div>', main_inner2))
        print(f'  After fix: opens={oc2}, closes={cc2}, diff={oc2-cc2}')
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'  Saved {fname}')

fix_file('experience_solitaire_dashboard_new.html')
fix_file('experience_solitaire_dashboard.html')
