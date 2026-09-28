import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("customer_overview_solitaire.html")
print("=== customer_overview_solitaire.html ===")
for term in ["lifestyle", "investment", "district", "concierge", "demat", "pitch"]:
    cnt = c.lower().count(term)
    print(f"Term '{term}': {cnt} occurrences")

