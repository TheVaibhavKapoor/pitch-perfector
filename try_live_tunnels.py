import subprocess, time, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def test_tunnels():
    # Try cloudflared via npx
    print("Testing cloudflared tunnel...")
    try:
        proc = subprocess.Popen("npx -y @cloudflare/cloudflared tunnel --url http://localhost:3000", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        start = time.time()
        while time.time() - start < 12:
            line = proc.stdout.readline()
            if line:
                print("cloudflared:", line.strip())
                m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
                if m:
                    url = m.group(0)
                    print(f"FOUND CLOUDFLARED URL: {url}")
                    with open("live_tunnel.txt", "w") as f:
                        f.write(url)
                    return url
    except Exception as e:
        print("Cloudflared error:", e)

    # Try pinggy via ssh
    print("Testing pinggy tunnel...")
    try:
        proc2 = subprocess.Popen("ssh -o StrictHostKeyChecking=no -p 443 -R0:localhost:3000 a.pinggy.io", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        start = time.time()
        while time.time() - start < 10:
            line = proc2.stdout.readline()
            if line:
                print("pinggy:", line.strip())
                m = re.search(r'https://[a-zA-Z0-9-]+\.pinggy\.link', line)
                if m:
                    url = m.group(0)
                    print(f"FOUND PINGGY URL: {url}")
                    with open("live_tunnel.txt", "w") as f:
                        f.write(url)
                    return url
    except Exception as e:
        print("Pinggy error:", e)

    # Try localtunnel
    print("Testing localtunnel...")
    try:
        proc3 = subprocess.Popen("npx -y localtunnel --port 3000", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        start = time.time()
        while time.time() - start < 10:
            line = proc3.stdout.readline()
            if line:
                print("lt:", line.strip())
                m = re.search(r'https://[a-zA-Z0-9-]+\.loca\.lt', line)
                if m:
                    url = m.group(0)
                    print(f"FOUND LOCALTUNNEL URL: {url}")
                    with open("live_tunnel.txt", "w") as f:
                        f.write(url)
                    return url
    except Exception as e:
        print("Localtunnel error:", e)

    return None

if __name__ == "__main__":
    res = test_tunnels()
    print("Final tunnel result:", res)
