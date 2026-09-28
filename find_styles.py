import os
print("styles.css exists:", os.path.exists("styles.css"))
if os.path.exists("styles.css"):
    print("styles.css size:", os.path.getsize("styles.css"))
