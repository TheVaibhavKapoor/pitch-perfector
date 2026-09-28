import os, json
log_dir = r"C:\Users\vaibh\.gemini\antigravity-ide\brain\03948273-1692-4395-a2ef-cfc81d47e003\.system_generated\logs"
fpath = os.path.join(log_dir, "transcript_full.jsonl")
if os.path.exists(fpath):
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if "view_file" in line:
                try:
                    data = json.loads(line)
                    print(f"Line {i}: type={data.get('type')}")
                except Exception as e:
                    pass
