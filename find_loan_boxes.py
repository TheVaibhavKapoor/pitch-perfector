import sys, re

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
matches = [m.start() for m in re.finditer(r'selectLoanProduct', c)]
print(f"Total selectLoanProduct occurrences: {len(matches)}")
for m in matches:
    print(c[m-50:m+100])
    print("-" * 40)
