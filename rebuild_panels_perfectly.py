import re, codecs

def fix_panel_isolation(filepath):
    print(f'=== Perfect Panel Isolation for {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Check panel-cc and reward-calculator
    # In experience_solitaire_dashboard_new.html:
    # panel-cc starts at <div id="panel-cc" class="info-panel">
    # reward-calculator is <div id="reward-calculator" ...>
    # panel-assets starts at <div id="panel-assets" class="info-panel">
    
    # Check if reward-calculator is inside panel-cc or if there are extra </div> tags closing panel-cc before reward-calculator
    cc_pos = text.find('id="panel-cc"')
    calc_pos = text.find('id="reward-calculator"')
    assets_pos = text.find('id="panel-assets"')
    inv_pos = text.find('id="panel-investments"')
    forex_pos = text.find('id="panel-forex"')
    other_pos = text.find('id="panel-other"')
    
    print(f'Positions: cc={cc_pos}, calc={calc_pos}, assets={assets_pos}, inv={inv_pos}, forex={forex_pos}, other={other_pos}')
    
    # Between cc_pos and calc_pos, count open vs close divs
    sub_cc = text[cc_pos:calc_pos]
    opens = len(re.findall(r'<div[\s>]', sub_cc))
    closes = len(re.findall(r'</div>', sub_cc))
    print(f'Between panel-cc and reward-calculator: opens={opens}, closes={closes}, diff={opens-closes}')
    
    # If closes > opens, panel-cc was closed premature!
    # Let's inspect the sub_cc snippet near calc_pos
    if closes > opens:
        print('Premature closing divs found before reward-calculator! Removing extra closes...')
        # The extra closes are right before id="reward-calculator"
        # We need opens == closes + 1 so panel-cc stays OPEN into reward-calculator
        # Let's fix sub_cc
        # Replace excess </div> tags before reward-calculator
        lines = sub_cc.split('\n')
        # Remove empty </div> lines at the end of sub_cc
        new_lines = []
        trailing_removed = 0
        target_diff = 1 # panel-cc itself is open
        current_diff = opens - closes
        needed_removal = target_diff - current_diff # e.g. 1 - (-2) = 3
        
        for line in reversed(lines):
            if trailing_removed < needed_removal and line.strip() == '</div>':
                trailing_removed += 1
                continue
            new_lines.append(line)
        new_lines.reverse()
        fixed_sub_cc = '\n'.join(new_lines)
        
        text = text[:cc_pos] + fixed_sub_cc + text[calc_pos:]
        print(f'Removed {trailing_removed} excess closing divs before reward-calculator.')

    # Also check between calc_pos and assets_pos
    calc_pos = text.find('id="reward-calculator"')
    assets_pos = text.find('id="panel-assets"')
    sub_calc = text[calc_pos:assets_pos]
    opens_c = len(re.findall(r'<div[\s>]', sub_calc))
    closes_c = len(re.findall(r'</div>', sub_calc))
    print(f'Between reward-calculator and panel-assets: opens={opens_c}, closes={closes_c}, diff={opens_c-closes_c}')
    
    # We need panel-cc to close right before panel-assets!
    # So between cc_pos and assets_pos, opens should equal closes (panel-cc completely closed).
    total_opens = len(re.findall(r'<div[\s>]', text[cc_pos:assets_pos]))
    total_closes = len(re.findall(r'</div>', text[cc_pos:assets_pos]))
    print(f'Total panel-cc section (cc -> assets): opens={total_opens}, closes={total_closes}, diff={total_opens-total_closes}')
    
    if total_opens != total_closes:
        diff_err = total_opens - total_closes
        print(f'Fixing total panel-cc closure diff of {diff_err}...')
        if diff_err > 0:
            # Need diff_err more closing divs before assets_pos
            ins_pos = text.find('id="panel-assets"')
            div_start = text.rfind('<div', 0, ins_pos)
            text = text[:div_start] + ('</div>\n' * diff_err) + text[div_start:]
        elif diff_err < 0:
            # Need to remove abs(diff_err) closing divs before assets_pos
            ins_pos = text.find('id="panel-assets"')
            div_start = text.rfind('<div', 0, ins_pos)
            chunk = text[:div_start]
            for _ in range(abs(diff_err)):
                last_c = chunk.rfind('</div>')
                if last_c != -1:
                    chunk = chunk[:last_c] + chunk[last_c+6:]
            text = chunk + text[div_start:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Panel isolation fix complete for {filepath}!\n')

fix_panel_isolation('experience_solitaire_dashboard_new.html')
fix_panel_isolation('experience_solitaire_dashboard.html')
