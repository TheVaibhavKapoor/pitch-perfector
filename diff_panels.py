import os, re, difflib


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def get_panels(content):
    matches = list(re.finditer(r'id=["\']panel-([^"\']+)["\']', content))
    panels = {}
    for i, m in enumerate(matches):
        name = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        panels[name] = content[start:end]
    return panels


sol_content = get_content("experience_solitaire_dashboard_new.html")
prv_content = get_content("experience_privy_dashboard_new.html")

sol_panels = get_panels(sol_content)
prv_panels = get_panels(prv_content)

print(
    f"Solitaire panels: {list(sol_panels.keys())}\nPrivy panels: {list(prv_panels.keys())}\n"
)

with open("panels_diff.txt", "w", encoding="utf-8") as out:
    for name in prv_panels:
        if name not in sol_panels:
            out.write(f"=== PANEL {name} NOT FOUND IN SOLITAIRE ===\n\n")
            continue
        p_sol = sol_panels[name].splitlines()
        p_prv = prv_panels[name].splitlines()
        diff = list(
            difflib.unified_diff(
                p_prv, p_sol, fromfile="privy", tofile="solitaire", lineterm=""
            )
        )
        if diff:
            out.write(f"=== DIFF FOR PANEL: {name} ===\n")
            for line in diff:
                out.write(line + "\n")
            out.write("\n" + "=" * 50 + "\n\n")
        else:
            out.write(f"=== PANEL {name} IS IDENTICAL ===\n\n")

print("Diff of panels written to panels_diff.txt")
