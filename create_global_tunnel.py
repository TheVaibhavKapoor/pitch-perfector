import subprocess, time, re

def try_localtunnel():
    print("Trying localtunnel via npx...")
    cmd = "npx -y localtunnel --port 3000"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    start = time.time()
    url = None
    while time.time() - start < 15:
        line = proc.stdout.readline()
        if line:
            print("lt output:", line.strip())
            m = re.search(r'https://[a-zA-Z0-9-]+\.loca\.lt', line)
            if m:
                url = m.group(0)
                print(f"FOUND LOCALTUNNEL URL: {url}")
                break
        time.sleep(0.5)
    return url

if __name__ == "__main__":
    u = try_localtunnel()
    if u:
        print(f"\nSUCCESS! Global live URL: {u}")
    else:
        print("\nLocaltunnel did not produce URL in time.")
