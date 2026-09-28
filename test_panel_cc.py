with open('experience_solitaire_dashboard.html', 'r', encoding='utf-8') as f:
    t1 = f.read()
    
with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    t2 = f.read()

def check_panel(text, name):
    idx = text.find('id="panel-cc"')
    if idx == -1:
        print(f'{name}: not found')
        return
    end_idx = text.find('id="panel-assets"')
    if end_idx == -1:
        print(f'{name}: no panel-assets')
        return
    print(f'{name}: panel-cc is {end_idx - idx} characters long')
    # Let's print the first 200 chars
    print(text[idx:idx+200].encode('ascii', 'replace').decode('ascii'))

check_panel(t1, 'experience_solitaire_dashboard.html')
check_panel(t2, 'experience_solitaire_dashboard_new.html')
