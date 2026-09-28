import re, codecs

def clean_file_headers(filepath):
    print(f'=== Cleaning headers in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split </div><div class="info-panel" into separate lines
    text = re.sub(r'</div>\s*<div\s+class="info-panel"\s+id="([^"]+)">', r'</div>\n<div class="info-panel" id="\1">', text)
    text = re.sub(r'</div>\s*<div\s+id="([^"]+)"\s+class="info-panel">', r'</div>\n<div class="info-panel" id="\1">', text)

    # Standardize all panel start tags
    # Replace <div class="info-panel" id="xyz"> or <div id="xyz" class="info-panel"> with <div class="info-panel" id="xyz">
    # (except keep active if present)
    def replacer(m):
        full = m.group(0)
        is_active = 'active' in full
        pid = m.group(1) if m.group(1) else m.group(2)
        active_str = ' active' if is_active else ''
        return f'<div class="info-panel{active_str}" id="{pid}">'

    text = re.sub(r'<div\s+(?:class="info-panel(?:\s+active)?"\s+id="([^"]+)"|id="([^"]+)"\s+class="info-panel(?:\s+active)?")\s*>', replacer, text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done cleaning {filepath}')

clean_file_headers('experience_solitaire_dashboard_new.html')
clean_file_headers('experience_solitaire_dashboard.html')
