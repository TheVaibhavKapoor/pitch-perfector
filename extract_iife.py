import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


c = get('experience_solitaire_dashboard_new.html')

# Extract the IIFE block fully
iife_start = c.find('(function(){')
iife_end = c.find('})();', iife_start)
if iife_end != -1:
    iife_end += 5
    print(f"IIFE from {iife_start} to {iife_end}")
    print(c[iife_start:iife_end])
else:
    print("IIFE end not found, printing 3000 chars")
    print(c[iife_start:iife_start+3000])
