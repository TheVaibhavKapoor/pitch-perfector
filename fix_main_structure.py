import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    import re
    
    # Find all </main> positions
    main_positions = [m.start() for m in re.finditer(r'</main>', text)]
    print(f'{filename}: {len(main_positions)} </main> tags found at: {main_positions}')
    
    if len(main_positions) < 2:
        print('  -> Less than 2 </main> tags, skipping')
        return
    
    # The FIRST </main> (at ~line 41604) is the premature/wrong one - inside CC panel
    # The SECOND </main> (at end) is the correct one
    # We need to remove the first bad </main> and also fix its surrounding structure
    
    first_main_pos = main_positions[0]
    
    # Look at what's around the first </main>
    context = text[first_main_pos-300:first_main_pos+200]
    print('Context around FIRST </main>:')
    print(context)
    print()
    
    # The pattern is:
    #             </div>
    #         </main>             <- THIS IS WRONG
    #
    #                 </div>
    #
    #                 <div id="panel-assets" class="info-panel">
    
    # We need to remove this first </main> AND the </div>\n    </div> that follows it
    # because those extra divs were the app-layout and main wrappers that got closed early
    
    # The proper fix: remove the first </main>\n    </div> sequence
    bad_pattern = re.compile(r'\s*</main>\s*\n\s*</div>\s*\n+\s*(?=<div id="panel-assets")', re.DOTALL)
    
    if bad_pattern.search(text):
        text = bad_pattern.sub('\n\n', text, count=1)
        print('Fixed: removed premature </main></div>')
    else:
        # Try simpler approach: remove just the first </main> if it's inside the content
        bad_str = '\n        </main>\n    </div>\n\n                </div>\n\n                <div id="panel-assets"'
        good_str = '\n\n                </div>\n\n                <div id="panel-assets"'
        if bad_str in text:
            text = text.replace(bad_str, good_str, 1)
            print('Fixed: replaced using exact string match')
        else:
            print('WARNING: Could not find exact bad pattern')
            print('Trying character-by-character search...')
            pos_start = main_positions[0]
            # Find the start of '\n        </main>' around pos
            search_back = text[pos_start-20:pos_start+100]
            print('Chars:', repr(search_back))
    
    # Verify we fixed it
    main_positions_after = [m.start() for m in re.finditer(r'</main>', text)]
    print(f'After fix: {len(main_positions_after)} </main> tags')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Saved {filename}')
    print()

fix_file('experience_solitaire_dashboard_new.html')
fix_file('experience_solitaire_dashboard.html')
