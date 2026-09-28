import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

def save(f, c):
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

fname = "experience_solitaire_dashboard_new.html"
c = get(fname)

print(f"\n==================== Simplifying Headers in {fname} ====================")

# 1. Simplify Features headers
c = re.sub(r'<h4 style="([^"]*)">📌 (.*?)</h4>', r'<h4 style="\1">📌 Features</h4>', c)

# 2. Simplify Pitches summary headers
c = re.sub(
    r'<summary style="([^"]*)">\s*<span style="[^"]*">\s*<span>🗣️</span> (.*?)\s*</span>\s*<span style="[^"]*">▼ (.*?)</span>\s*</summary>',
    r'''<summary style="\1">
        <span style="display: flex; align-items: center; gap: 8px;">
            <span>🗣️</span> Pitches
        </span>
        <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼</span>
    </summary>''',
    c
)

# Also handle simple span Pitches summary
c = re.sub(
    r'<summary style="([^"]*)">\s*<span>🗣️ (.*?)</span>\s*<span style="[^"]*">▼ (.*?)</span>\s*</summary>',
    r'''<summary style="\1">
        <span style="display: flex; align-items: center; gap: 8px;">
            <span>🗣️</span> Pitches
        </span>
        <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼</span>
    </summary>''',
    c
)

# 3. Simplify Calculator summary headers
c = re.sub(
    r'<summary style="([^"]*)">\s*<span style="[^"]*">\s*<span>🧮</span> (.*?)\s*</span>\s*<span style="[^"]*">▼ (.*?)</span>\s*</summary>',
    r'''<summary style="\1">
        <span style="display: flex; align-items: center; gap: 8px;">
            <span>🧮</span> Calculator
        </span>
        <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼</span>
    </summary>''',
    c
)

c = re.sub(
    r'<summary style="([^"]*)">\s*<span>🧮 (.*?)</span>\s*<span style="[^"]*">▼ (.*?)</span>\s*</summary>',
    r'''<summary style="\1">
        <span style="display: flex; align-items: center; gap: 8px;">
            <span>🧮</span> Calculator
        </span>
        <span style="font-size: 0.8rem; color: #3b82f6; font-weight: 700;">▼</span>
    </summary>''',
    c
)

save(fname, c)
print("Successfully simplified headers to Features, Pitches, and Calculator!")
