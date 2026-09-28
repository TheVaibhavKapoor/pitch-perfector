import urllib.request, sys

sys.stdout.reconfigure(encoding='utf-8')

base = open("global_live_link.txt").read().strip()

urls = [
    f"{base}/experience_solitaire_dashboard_new.html",
    f"{base}/customer_overview_solitaire.html",
    f"{base}/"
]

for url in urls:
    try:
        req = urllib.request.urlopen(url, timeout=5)
        print(f"FETCH {url} -> STATUS {req.status}")
    except Exception as e:
        print(f"FETCH {url} -> ERROR {e}")
