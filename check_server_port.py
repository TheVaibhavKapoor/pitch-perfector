import urllib.request

for port in [3000, 3001]:
    url = f"http://localhost:{port}/experience_solitaire_dashboard_new.html"
    try:
        req = urllib.request.urlopen(url, timeout=2)
        print(f"Port {port} STATUS: {req.status}")
    except Exception as e:
        print(f"Port {port} ERROR: {e}")
