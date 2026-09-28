import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def print_cc_section(fpath):
    content = get_content(fpath)
    # find indices
    p_cc = content.find("panel-cc")
    p_life = content.find("panel-lifestyle")
    print(f"File: {fpath}, panel-cc index: {p_cc}, panel-lifestyle index: {p_life}")
    if p_cc != -1 and p_life != -1:
        snippet = content[p_cc - 100 : p_life + 100]
        out_f = fpath.replace(".html", "_cc_sec.txt")
        with open(out_f, "w", encoding="utf-8") as f:
            f.write(snippet)
        print(f"Wrote to {out_f}")


print_cc_section("experience_privy_dashboard_new.html")
print_cc_section("experience_solitaire_dashboard_new.html")
