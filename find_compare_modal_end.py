import os


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


c = get_content("experience_solitaire_dashboard_new.html")
# Compare modal starts at 151103
# Find where compare modal truly closes
pos = 151103
segment = c[pos:]
depth = 0
end_pos = 0
i = 0
while i < len(segment):
    if segment[i:i+4] == '<div':
        depth += 1
        i += 4
    elif segment[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            end_pos = pos + i + 6
            break
        i += 6
    else:
        i += 1

print(f"Compare modal closes at approx pos: {end_pos}")
print(f"Total file length: {len(c)}")
# Print what's right after compare modal
print("\nContent right after compare modal:")
print(c[end_pos:end_pos+500])
