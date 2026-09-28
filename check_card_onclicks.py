import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()

c = get("experience_solitaire_dashboard_new.html")
# search for product-card onclick
cards = re.findall(r'<div class="product-card[^"]*"[^>]*>', c)
for card in cards:
    print("CARD:", card)

# search for function definitions for panel switching
funcs = re.findall(r'function [a-zA-Z0-9_]+\(', c)
print("\nJS Functions in file:")
for fn in set(funcs):
    print(" ", fn)
