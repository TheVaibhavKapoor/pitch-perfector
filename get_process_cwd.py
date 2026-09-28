import psutil
try:
    p = psutil.Process(57240)
    print("Process CWD:", p.cwd())
    print("Process command line:", p.cmdline())
except Exception as e:
    print("Error:", e)
