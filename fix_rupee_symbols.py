import re

# Fix broken rupee symbols (? -> ₹) across HTML files
# Only replace ? in contexts where it's clearly a rupee symbol

def fix_rupee(fname, replacements):
    """Apply string replacements to fix ? -> ₹"""
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    original_count = content.count('₹')
    for old, new in replacements:
        content = content.replace(old, new)
    new_count = content.count('₹')
    print(f'{fname}: added {new_count - original_count} rupee symbols')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

# ── experience_solitaire_dashboard.html ──────────────────────────────────────
# Line 749: >? FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>
# (that ? is a rupee icon before "FEATURED")
fix_rupee('experience_solitaire_dashboard.html', [
    ('">? FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>', '">₹ FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>'),
])

# ── experience_solitaire_dashboard_new.html ──────────────────────────────────
# Line 691 : >? FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>
# Line 1339: >7.50% p.a. ?</div>
# Line 1371: <span>? <strong>Zero Processing Fee Savings:</strong> Waived (Save up to ?50,000)</span>
# Line 1372: <span style="font-weight: 800; color: #15803d;">+ ? 50,000</span>
# Lines 1412-1418: JS strings '? ' + ...
fix_rupee('experience_solitaire_dashboard_new.html', [
    ('">? FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>', '">₹ FEATURED &mdash; SOLITAIRE PREFERENTIAL RATE</div>'),
    ('p.a. ?</div>', 'p.a. ₹</div>'),
    ('<span>? <strong>Zero Processing Fee Savings:</strong> Waived (Save up to ?50,000)</span>',
     '<span>₹ <strong>Zero Processing Fee Savings:</strong> Waived (Save up to ₹50,000)</span>'),
    ('+ ? 50,000', '+ ₹ 50,000'),
    ("'? ' + (p >= 10000000", "'₹ ' + (p >= 10000000"),
    ("'? ' + Math.round(emiNormal)", "'₹ ' + Math.round(emiNormal)"),
    ("'? ' + Math.round(emiSolitaire)", "'₹ ' + Math.round(emiSolitaire)"),
    ("'? ' + Math.round(monthlySave)", "'₹ ' + Math.round(monthlySave)"),
    ("'? ' + Math.round(totalInterestSaved)", "'₹ ' + Math.round(totalInterestSaved)"),
])

print('All fixes applied!')
