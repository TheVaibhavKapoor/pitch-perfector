import os, json
log_dir = r"C:\Users\vaibh\.gemini\antigravity-ide\brain\03948273-1692-4395-a2ef-cfc81d47e003\.system_generated\logs"
fpath = os.path.join(log_dir, "transcript_full.jsonl")
if os.path.exists(fpath):
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        for idx, line in enumerate(f):
            if 100 <= idx <= 110:
                try:
                    data = json.loads(line)
                    print(f"Index {idx}: source={data.get('source')} type={data.get('type')}")
                    # If type is SYSTEM_MESSAGE or similar, print the content
                    content = data.get('content')
                    if content:
                        print(f"Content length: {len(content)}")
                        if len(content) > 500:
                            print(content[:500] + "...")
                        else:
                            print(content)
                except Exception as e:
                    print(f"Error reading index {idx}: {e}")
