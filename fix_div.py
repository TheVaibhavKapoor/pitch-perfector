import os

files = [
    'experience_solitaire_dashboard.html',
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard.html',
    'experience_privy_plus_dashboard_new.html'
]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replaced `<div id="reward-calculator" ...> <div class="card calc-card-photo">` 
    # with `<div id="reward-calculator-wrapper"...> <div ...> <h2...><svg...></div> <div id="reward-calculator"...> <div class="card calc-card-photo"...>`
    # The original had 2 open divs. The new has 3 open divs!
    # So we need one extra closing `</div>` wherever the original `reward-calculator` closed.
    # Where does `reward-calculator` close?
    # It closes exactly before `<script>` tag for Flow-Matched Calculation Logic!
    
    # Let's find the exact end of calc-card-photo and reward-calculator
    # In original, it was:
    # </div> <!-- calc-card-photo -->
    # </div> <!-- reward-calculator -->
    # <script>
    # // Flow-Matched Calculation Logic
    
    # Let's just find `// Flow-Matched Calculation Logic` and add `</div>` before the `<script>` tag that contains it.
    
    idx = content.find('// Flow-Matched Calculation Logic')
    if idx != -1:
        script_start = content.rfind('<script>', 0, idx)
        if script_start != -1:
            # We want to add a `</div>` right before `script_start` if we haven't already
            if "<!-- Wrapper Close --></div>" not in content[script_start-50:script_start]:
                new_content = content[:script_start] + '\n<!-- Wrapper Close --></div>\n' + content[script_start:]
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {filename}")
            else:
                print(f"Already fixed {filename}")
