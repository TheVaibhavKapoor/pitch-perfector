import re
import os

files = [
    'experience_solitaire_dashboard.html',
    'experience_solitaire_dashboard_new.html',
    'experience_privy_dashboard.html',
    'experience_privy_dashboard_new.html',
    'experience_privy_plus_dashboard.html',
    'experience_privy_plus_dashboard_new.html'
]

script_to_add = """
<script>
function toggleCalculator() {
    var calc = document.getElementById('reward-calculator');
    var chevron = document.getElementById('calc-chevron');
    if (calc.style.display === 'none') {
        calc.style.display = 'block';
        chevron.style.transform = 'rotate(180deg)';
    } else {
        calc.style.display = 'none';
        chevron.style.transform = 'rotate(0deg)';
    }
}
</script>
</body>
"""

search_pattern = re.compile(
    r'<div id="reward-calculator"[^>]*>\s*<div class="card calc-card-photo">\s*<h2 class="calc-main-heading">Calculate rewards points for customer</h2>'
)

replacement = """<div id="reward-calculator-wrapper" style="margin-top: 32px; margin-bottom: 32px; border: 1px solid #e2e8f0; border-radius: 12px; background: white; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
  <div onclick="toggleCalculator()" style="padding: 20px 24px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: #f8fafc; border-bottom: 1px solid #e2e8f0; transition: background 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='#f8fafc'">
    <h2 style="margin: 0; font-size: 1.15rem; font-weight: 700; color: #1e293b; display: flex; align-items: center; gap: 8px;">
      <span>🧮</span> Calculate Rewards Points
    </h2>
    <svg id="calc-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.3s; transform: rotate(0deg);">
      <polyline points="6 9 12 15 18 9"></polyline>
    </svg>
  </div>
  <div id="reward-calculator" style="display: none; padding: 24px;">
  <div class="card calc-card-photo" style="box-shadow: none; border: none; margin: 0; padding: 0;">
"""

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already added
        if 'reward-calculator-wrapper' not in content:
            content = search_pattern.sub(replacement, content)
            
            # Add JS function before </body>
            if 'function toggleCalculator()' not in content:
                content = content.replace('</body>', script_to_add)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"Already updated {filename}")

