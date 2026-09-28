import subprocess, time, re

def start_persistent_cf_tunnel():
    # Run cloudflared tunnel
    proc = subprocess.Popen("npx -y cloudflared tunnel --url http://localhost:3000", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    url = None
    for i in range(100):
        line = proc.stdout.readline()
        if not line:
            time.sleep(0.1)
            continue
        print("CF:", line.strip())
        m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
        if m:
            url = m.group(0)
            print(f"\n==========================================")
            print(f"SUCCESS! GLOBAL LIVE URL: {url}")
            print(f"==========================================")
            with open("global_live_link.txt", "w") as f:
                f.write(url)
            break
            
    # Keep reading in background so pipe doesn't block
    while True:
        l = proc.stdout.readline()
        if not l:
            time.sleep(1)

if __name__ == "__main__":
    start_persistent_cf_tunnel()
