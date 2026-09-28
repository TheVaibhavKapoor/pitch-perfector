import urllib.request

urls = [
    "http://localhost:3000/experience_solitaire_dashboard_new.html",
    "http://localhost:3001/experience_solitaire_dashboard_new.html",
    "http://localhost:3000/customer_overview_solitaire.html",
    "http://localhost:3001/customer_overview_solitaire.html",
    "http://localhost:3000/",
    "http://localhost:3001/"
]

for url in urls:
    try:
        req = urllib.request.urlopen(url, timeout=2)
        print(f"{url} -> STATUS {req.status}")
    except Exception as e:
        print(f"{url} -> ERROR {e}")
