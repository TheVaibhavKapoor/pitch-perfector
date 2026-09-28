import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


content = get_content("experience_privy_dashboard_new.html")
lines = content.split("\n")
with open("panel_cc_output.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "panel-cc" in line:
            out.write(f"Line {i+1}:\n")
            for idx in range(max(0, i - 2), min(len(lines), i + 100)):
                out.write(f"  {idx+1}: {lines[idx]}\n")
            out.write("-" * 50 + "\n")
print("Wrote panel_cc_output.txt")
