import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")
lines = c.split('\n')

# Find tab-related lines for CC, Loans, Investments
keywords = ['Features', 'Calculator', 'Pitches', 'tab', 'credit', 'loan', 'invest', 'tab-btn', 'tab-content']
for i, line in enumerate(lines):
    for kw in keywords:
        if kw.lower() in line.lower() and ('tab' in line.lower() or 'calculator' in line.lower() or 'pitch' in line.lower() or 'feature' in line.lower()):
            print(f"Line {i+1}: {line.strip()[:140]}")
            break
