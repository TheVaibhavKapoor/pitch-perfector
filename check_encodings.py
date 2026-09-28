import glob


def check_encoding(fpath):
    # Try reading as UTF-16
    try:
        with open(fpath, "r", encoding="utf-16") as f:
            f.read()
        return "UTF-16"
    except Exception:
        pass
    # Try reading as UTF-8
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            f.read()
        return "UTF-8"
    except Exception:
        return "Unknown"


for f in glob.glob("*.html"):
    print(f"{f}: {check_encoding(f)}")
