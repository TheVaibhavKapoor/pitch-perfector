import subprocess, time, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def launch_cloudflare_tunnel():
    print("Launching Cloudflare Tunnel (cloudflared) for http://localhost:3001...")
    cmd = "npx -y cloudflared tunnel --url http://localhost:3001"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    start = time.time()
    url = None
    while time.time() - start < 30:
        line = proc.stdout.readline()
        if line:
            print("cloudflared log:", line.strip())
            m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
            if m:
                url = m.group(0)
                print(f"\n==========================================")
                print(f"SUCCESS! GLOBAL LIVE CLOUDFLARE URL: {url}")
                print(f"==========================================")
                with open("cf_tunnel_url.txt", "w") as f:
                    f.write(url)
                break
        time.sleep(0.2)
    
    if url:
        print("Tunnel is actively serving traffic. Streaming logs (press Ctrl+C to stop)...")
        try:
            for line in proc.stdout:
                if line:
                    print("cloudflared:", line.strip())
        except KeyboardInterrupt:
            proc.terminate()
    return url

if __name__ == "__main__":
    launch_cloudflare_tunnel()
