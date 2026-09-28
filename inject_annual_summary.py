import os
from bs4 import BeautifulSoup

def update_summary_panel():
    dash_file = 'experience_solitaire_dashboard_new.html'
    benefit_file = 'calculate_benefit.html'
    
    if not os.path.exists(dash_file) or not os.path.exists(benefit_file):
        print("Files not found")
        return
        
    with open(dash_file, 'r', encoding='utf-8') as f:
        soup_dash = BeautifulSoup(f, 'html.parser')
        
    with open(benefit_file, 'r', encoding='utf-8') as f:
        soup_ben = BeautifulSoup(f, 'html.parser')
        
    panel_summary = soup_dash.find(id='panel-summary')
    if not panel_summary:
        print("Panel summary not found in dash")
        return
        
    # Clear current dummy content
    panel_summary.clear()
    
    # We want to bring the hero summary banner, and the bento grid section
    hero = soup_ben.find('section', class_='hero-summary-card')
    bento_grid = soup_ben.find('div', class_='bento-grid')
    section_header = soup_ben.find('div', class_='section-header')
    
    if hero:
        panel_summary.append(hero)
    if section_header:
        panel_summary.append(section_header)
    if bento_grid:
        panel_summary.append(bento_grid)
        
    # We also need the CSS styles from calculate_benefit.html
    # We will grab the entire <style> block and add it to the <head> of dash_file
    style_block = soup_ben.find('style')
    if style_block:
        # Avoid duplicate styles if already present (e.g., if we run script twice)
        existing_styles = soup_dash.head.find_all('style')
        is_already_injected = False
        for s in existing_styles:
            if 'hero-summary-card' in s.string:
                is_already_injected = True
                break
        
        if not is_already_injected:
            soup_dash.head.append(style_block)
            
    # Also add the "Send Summary Over Email Section" ?
    # It's an interactive part. I'll add it too, since it is part of the summary.
    email_section = soup_ben.find('section', class_='email-section-card')
    if email_section:
        panel_summary.append(email_section)
        
    # And the script for the email form
    # We will find the script containing 'handleSendEmail'
    scripts = soup_ben.find_all('script')
    for script in scripts:
        if script.string and 'handleSendEmail' in script.string:
            panel_summary.append(script)
            break
            
    # And the Toast notification HTML
    toast = soup_ben.find(id='toastSuccess')
    if toast:
        soup_dash.body.append(toast)
        
    # And the spin animation style at the bottom of the file
    spin_style = soup_ben.find_all('style')[-1]
    if spin_style and 'spin' in spin_style.string:
        soup_dash.head.append(spin_style)
        
    with open(dash_file, 'w', encoding='utf-8') as f:
        f.write(str(soup_dash))
    print(f"Updated {dash_file} with Annual Benefit Summary")

update_summary_panel()
