import os

if os.path.exists("cf_live_link.txt"):
    print("CF LINK:", open("cf_live_link.txt").read().strip())
else:
    print("CF LINK NOT READY YET")
