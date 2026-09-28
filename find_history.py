import os, json

vscode_history = r"C:\Users\vaibh\AppData\Roaming\Code\User\History"
if os.path.exists(vscode_history):
    print("Found VS Code History folder!")
    for root, dirs, files in os.walk(vscode_history):
        for f in files:
            if f == "entries.json":
                fpath = os.path.join(root, f)
                try:
                    with open(fpath, "r", encoding="utf-8") as file:
                        data = json.load(file)
                    for entry in data.get("entries", []):
                        # print the resource to check what we have
                        resource = entry.get("resource", "")
                        if "customer_overview_solitaire" in resource:
                            print(f"Found entry: {entry} in {root}")
                            # The backup file itself is in the same directory, named entry['id']
                            backup_file = os.path.join(root, entry["id"])
                            if os.path.exists(backup_file):
                                print(f"Backup file exists: {backup_file}, size: {os.path.getsize(backup_file)}")
                except Exception as e:
                    print(f"Error reading {fpath}: {e}")
else:
    print("VS Code History folder not found")
