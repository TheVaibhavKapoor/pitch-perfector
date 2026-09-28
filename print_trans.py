import os, json
log_dir = r"C:\Users\vaibh\.gemini\antigravity-ide\brain\03948273-1692-4395-a2ef-cfc81d47e003\.system_generated\logs"
fpath = os.path.join(log_dir, "transcript_full.jsonl")
with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
    for i, line in enumerate(f):
        if i == 102:
            data = json.loads(line)
            content = data.get("content")
            if content:
                with open("original_modals_section.txt", "w", encoding="utf-8") as out:
                    out.write(content)
                print("Wrote content to original_modals_section.txt")
