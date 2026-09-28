import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


c = get('experience_solitaire_dashboard_new.html')
# Check all IIFE locations
positions = [m.start() for m in re.finditer(r'\(function\(\)\{', c)]
html_end = c.find('</html>')
body_end = c.find('</body>')
print(f"</body>: {body_end}, </html>: {html_end}")
for p in positions:
    # Get 80 chars of context
    snippet = c[p:p+80].replace('\n', ' ')
    print(f"  IIFE at {p} (after body={p>body_end}): {snippet}")
