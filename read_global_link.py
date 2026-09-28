import os

if os.path.exists("global_live_link.txt"):
    print("GLOBAL LINK:", open("global_live_link.txt").read().strip())
else:
    print("NOT READY YET")
