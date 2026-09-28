import re, codecs

def check_dc(filepath):
    print(f'=== Checking panel-dc in {filepath} ===')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    dc_start = text.find('id="panel-dc"')
    cc_start = text.find('id="panel-cc"')
    dc_chunk = text[dc_start:cc_start]
    
    print('Length of panel-dc chunk:', len(dc_chunk))
    if 'investment' in dc_chunk.lower():
        print('FOUND "investment" inside panel-dc chunk!')
        for line in dc_chunk.split('\n'):
            if 'investment' in line.lower() or 'id=' in line.lower():
                print('  MATCH LINE:', repr(line))
    else:
        print('NO "investment" text found inside panel-dc.')

check_dc('experience_solitaire_dashboard_new.html')
check_dc('experience_solitaire_dashboard.html')
