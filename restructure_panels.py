import os
from bs4 import BeautifulSoup, Comment

files = [
    'experience_solitaire_dashboard_new.html'
]

inner_tabs_html = """
<div class="inner-tabs-container" style="display: flex; gap: 8px; margin-bottom: 24px; background: #f1f5f9; padding: 6px; border-radius: 12px;">
    <button class="inner-tab-btn active" onclick="switchInnerTab(this, 'features')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #0f172a; background: white; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;">Features</button>
    <button class="inner-tab-btn" onclick="switchInnerTab(this, 'calculator')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;">Calculator</button>
    <button class="inner-tab-btn" onclick="switchInnerTab(this, 'pitches')" style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;">Pitches</button>
</div>
"""

pitch_template = """
<div class="inner-tab-content inner-tab-content-pitches" style="display: none;">
    <div style="background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 12px; padding: 32px; text-align: center; color: #64748b;">
        <h3 style="color: #0f172a; margin-bottom: 8px; font-size: 1.1rem;">{title} Pitch</h3>
        <p>This is a placeholder for the {title} pitch. Highlight the premium benefits, exclusive features, and value proposition for the customer here.</p>
    </div>
</div>
"""

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # 1. Panel Assets
    panel_assets = soup.find(id='panel-assets')
    # Check if already processed
    if panel_assets and not panel_assets.find(class_='inner-tabs-container'):
        h2 = panel_assets.find('h2')
        p = panel_assets.find('p')
        
        calc_btn = panel_assets.find(lambda tag: tag.name == 'button' and 'home_loan_calculator.html' in tag.get('onclick', ''))
        calc_area = None
        if calc_btn:
            calc_area = calc_btn.parent
            
        features_content = []
        for child in list(panel_assets.children):
            if child not in [h2, p, calc_area]:
                features_content.append(child.extract())
                
        new_panel_assets = soup.new_tag('div', id='panel-assets', **{'class': 'info-panel'})
        if h2: new_panel_assets.append(h2.extract())
        if p: new_panel_assets.append(p.extract())
        
        tabs_soup = BeautifulSoup(inner_tabs_html, 'html.parser')
        new_panel_assets.append(tabs_soup)
        
        features_div = soup.new_tag('div', **{'class': 'inner-tab-content inner-tab-content-features', 'style': 'display: block;'})
        for fc in features_content:
            features_div.append(fc)
        new_panel_assets.append(features_div)
        
        calc_div = soup.new_tag('div', **{'class': 'inner-tab-content inner-tab-content-calculator', 'style': 'display: none;'})
        if calc_area:
            calc_div.append(calc_area.extract())
        new_panel_assets.append(calc_div)
        
        pitch_soup = BeautifulSoup(pitch_template.format(title="Loans"), 'html.parser')
        new_panel_assets.append(pitch_soup)
        
        panel_assets.replace_with(new_panel_assets)

    # 2. Panel Investments
    panel_investments = soup.find(id='panel-investments')
    if panel_investments and not panel_investments.find(class_='inner-tabs-container'):
        h2 = panel_investments.find('h2')
        p = panel_investments.find('p')
        
        calc_section = panel_investments.find(lambda tag: tag.name == 'div' and 'Investment Return Calculator' in tag.text)
        
        features_content = []
        for child in list(panel_investments.children):
            if child not in [h2, p, calc_section]:
                features_content.append(child.extract())
                
        new_panel_inv = soup.new_tag('div', id='panel-investments', **{'class': 'info-panel'})
        if h2: new_panel_inv.append(h2.extract())
        if p: new_panel_inv.append(p.extract())
        
        tabs_soup = BeautifulSoup(inner_tabs_html, 'html.parser')
        new_panel_inv.append(tabs_soup)
        
        features_div = soup.new_tag('div', **{'class': 'inner-tab-content inner-tab-content-features', 'style': 'display: block;'})
        for fc in features_content:
            features_div.append(fc)
        new_panel_inv.append(features_div)
        
        calc_div = soup.new_tag('div', **{'class': 'inner-tab-content inner-tab-content-calculator', 'style': 'display: none;'})
        if calc_section:
            calc_div.append(calc_section.extract())
        new_panel_inv.append(calc_div)
        
        pitch_soup = BeautifulSoup(pitch_template.format(title="Investment"), 'html.parser')
        new_panel_inv.append(pitch_soup)
        
        panel_investments.replace_with(new_panel_inv)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Updated {filename}")
