# -*- coding: utf-8 -*-
import re

dash_path = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
template_path = r'c:\Users\vaibh\Desktop\Pitch Perfector\credit_card_details.html'
out_path = r'c:\Users\vaibh\Desktop\Pitch Perfector\solitaire_cc.html'

with open(dash_path, 'r', encoding='utf-8') as f:
    dash_html = f.read()
with open(template_path, 'r', encoding='utf-8') as f:
    tmpl_html = f.read()

# Extract pitch & calculator from dash_html
# Start from <div style="grid-column: 1 / -1;"> which is where the merged content begins, up to </div> <!-- calc end -->
# Actually, let's just find the first <div class="product-features-grid"> in panel-cc
start_idx = dash_html.find('<div id="panel-cc"')
end_idx = dash_html.find('<div id="panel-assets"', start_idx)
panel_cc = dash_html[start_idx:end_idx]

# Remove the <div id="panel-cc" class="info-panel active"> wrapper so we can style it ourselves, or keep it.
# We just need the inner content
inner_start = panel_cc.find('>', panel_cc.find('<div style="grid-column: 1 / -1;">')) + 1
# find the calculator
calc_start = panel_cc.find('<div id="reward-calculator"')

pitch_html = panel_cc[panel_cc.find('<h2'):]

# In the template (credit_card_details.html), there is a main area. Let's find a good place to replace.
# The template has <main class="main-content"> ... <header> ... <section> ... 
# We'll replace everything after </header> up to </main>
main_start = tmpl_html.find('</header>') + len('</header>')
main_end = tmpl_html.rfind('</main>')

# We also need the javascript for the calculator
js_start = dash_html.find('// Flow-Matched Calculation Logic')
js_end = dash_html.find('</script>', js_start)
js_script = dash_html[js_start:js_end] if js_start != -1 else ""

new_content = tmpl_html[:main_start] + f'''
    <section style="padding: 32px; max-width: 1200px; margin: 0 auto;">
        {pitch_html}
    </section>
''' + tmpl_html[main_end:]

# append JS
new_content = new_content.replace('</body>', f'<script>\n{js_script}\n</script>\n</body>')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
