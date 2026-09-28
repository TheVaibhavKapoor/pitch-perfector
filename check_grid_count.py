import sys

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
print("Occurrences of id=\"loan-product-selector-grid\":", c.count('id="loan-product-selector-grid"'))
print("Occurrences of id=\"inv-product-selector-grid\":", c.count('id="inv-product-selector-grid"'))
