import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

def clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find panel-cc
    cc_start = text.find('id="panel-cc"')
    if cc_start == -1:
        print(f'panel-cc not found in {filename}')
        return

    # Find panel-assets
    assets_start = text.find('id="panel-assets"')
    if assets_start == -1:
        print(f'panel-assets not found in {filename}')
        return

    # Extract panel-cc chunk
    cc_chunk = text[cc_start:assets_start]
    
    # Remove </main> and trailing broken divs
    # Clean end of panel-cc: it should end with </div> right before <div class="info-panel" id="panel-assets">
    
    # Let's clean cc_chunk: remove </main>
    cc_chunk_clean = cc_chunk.replace('</main>', '')
    
    # Let's check div balance in cc_chunk_clean
    # The chunk starts like: id="panel-cc" class="info-panel active"> ... or <div id="panel-cc" ...
    # We should ensure panel-cc is properly closed before panel-assets.
    
    # Find where <div id="panel-assets" or <div class="info-panel" id="panel-assets" starts
    # We want cc_chunk_clean to end with </div>\n\n
    
    # Replace in text
    new_text = text[:cc_start] + cc_chunk_clean + text[assets_start:]
    
    # Let's fix the transition between panel-cc and panel-assets
    # Ensure panel-cc closes properly
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f'Cleaned {filename}')

clean_file('experience_solitaire_dashboard_new.html')
clean_file('experience_solitaire_dashboard.html')
