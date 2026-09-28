import re

with open("program_type_selection.html", "r", encoding="utf-8") as f:
    html = f.read()

# I previously set dashboardNTB for privy to experience_privy_dashboard.html.
# Change it to experience_privy_dashboard_new.html
html = html.replace(
    "dashboardNTB: 'experience_privy_dashboard.html'",
    "dashboardNTB: 'experience_privy_dashboard_new.html'"
)

# And for privy+ it was experience_privy_plus_dashboard.html
html = html.replace(
    "dashboardNTB: 'experience_privy_plus_dashboard.html'",
    "dashboardNTB: 'experience_privy_plus_dashboard_new.html'"
)

with open("program_type_selection.html", "w", encoding="utf-8") as f:
    f.write(html)
