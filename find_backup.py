import os
pp_best_path = r"c:\Users\vaibh\Desktop\PP BEST\customer_overview_solitaire.html"
if os.path.exists(pp_best_path):
    print(f"Found in PP BEST, size: {os.path.getsize(pp_best_path)} bytes")
else:
    print("Not found in PP BEST")
