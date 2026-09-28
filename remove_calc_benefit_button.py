import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def save_content(fpath, content):
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


content = get_content("experience_solitaire_dashboard_new.html")

# Find all CALCULATE OVERALL BENEFIT button blocks and remove them
# Pattern: the whole <div style="margin-top: 48px; ..."> ... </button>\n</div>
pat = re.compile(
    r'\s*<\!-- Calculate Benefit Button -->\s*'
    r'<div[^>]*>\s*'
    r'<button[^>]*>\s*CALCULATE OVERALL BENEFIT\s*</button>\s*'
    r'</div>',
    re.DOTALL
)
count = len(pat.findall(content))
print(f"Found {count} CALCULATE OVERALL BENEFIT button block(s)")
content = pat.sub('', content)

# Also remove any leftover bare button without comment header
pat2 = re.compile(
    r'\s*<div[^>]*>\s*'
    r'<button[^>]*onclick=["\']window\.open\([\'"]calculate_benefit[^>]*>\s*'
    r'CALCULATE OVERALL BENEFIT\s*</button>\s*'
    r'</div>',
    re.DOTALL
)
count2 = len(pat2.findall(content))
print(f"Found {count2} additional bare button block(s)")
content = pat2.sub('', content)

save_content("experience_solitaire_dashboard_new.html", content)
print("Done!")
