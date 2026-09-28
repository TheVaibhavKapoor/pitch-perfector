import subprocess, sys

def check_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        print(f"[{cmd}] Exit code: {res.returncode}")
        if res.stdout: print("  stdout:", res.stdout[:150].strip())
        if res.stderr: print("  stderr:", res.stderr[:150].strip())
        return res.returncode == 0
    except Exception as e:
        print(f"[{cmd}] Exception: {e}")
        return False

print("=== Checking Available Tunnel Tools ===")
check_cmd("npx --version")
check_cmd("ngrok --version")
check_cmd("ssh -V")
