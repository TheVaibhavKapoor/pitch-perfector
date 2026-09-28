import subprocess, time, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def get_cf_url():
    cmd = "npx -y cloudflared tunnel --url http://localhost:3000"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    start = time.time()
    url = None
    while time.time() - start < 15:
        line = proc.stdout.readline()
        if line:
            print("CF:", line.strip())
            m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
            if m:
                url = m.group(0)
                print(f"\n==========================================")
                print(f"CLOUDFLARE LIVE URL: {url}")
                print(f"==========================================")
                with open("cf_live_link.txt", "w") as f:
                    f.write(url)
                # Keep process running in background
                break
        time.sleep(0.2)
    return url

if __name__ == "__main__":
    get_cf_url()
