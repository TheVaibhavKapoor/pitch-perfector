import re, codecs

def clean_file(filepath):
    print(f'=== Cleaning Panel Start & End Tags in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean double <div <div
    text = re.sub(r'<div\s+<div id="panel-investments" class="info-panel">', r'<div id="panel-investments" class="info-panel">', text)
    text = re.sub(r'<div\s+<div id="panel-forex" class="info-panel">', r'<div id="panel-forex" class="info-panel">', text)
    text = re.sub(r'<div\s+<div id="panel-business-assets" class="info-panel">', r'<div id="panel-business-assets" class="info-panel">', text)

    # Let's verify panel-investments, panel-forex, panel-other boundaries
    # Each panel should start with <div id="panel-NAME" class="info-panel"> and end with </div> before the next panel!
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

clean_file('experience_solitaire_dashboard_new.html')
clean_file('experience_solitaire_dashboard.html')
