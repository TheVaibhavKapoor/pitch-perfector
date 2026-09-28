import os

for fname in ["cf_tunnel_url.txt", "live_tunnel.txt"]:
    if os.path.exists(fname):
        print(f"File {fname}: {open(fname).read().strip()}")
    else:
        print(f"File {fname}: NOT CREATED YET")
