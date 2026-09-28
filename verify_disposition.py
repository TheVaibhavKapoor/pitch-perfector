import os

def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()

for f in ["customer_overview_solitaire.html", "experience_solitaire_dashboard_new.html"]:
    c = get_content(f)
    print(f"\n=== {f} ===")
    print(f"'Disposition' button found: {'openDispositionModal()' in c}")
    print(f"'Create Lead' button remains: {'openDispositionModal' not in c and 'Create Lead</button>' in c}")
    print(f"create-lead-modal div found: {'id=\"create-lead-modal\"' in c}")
    print(f"Disposition Modal found: {'Customer Disposition' in c}")
    print(f"handleDisposition found: {'handleDisposition' in c}")
    print(f"addProductRow found: {'addProductRow' in c}")
