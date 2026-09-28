import re

# 1. Update CSS
css_to_add = """
/* Home Loan Modal */
.modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    z-index: 2000;
    justify-content: center;
    align-items: center;
}

.modal-overlay.show {
    display: flex;
}

.modal-content {
    background: #ffffff;
    border-radius: 12px;
    width: 90%;
    max-width: 500px;
    padding: 24px;
    position: relative;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.modal-close {
    position: absolute;
    top: 16px;
    right: 16px;
    background: transparent;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #6b7280;
}

.modal-header h2 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.modal-details-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.modal-details-list li {
    font-size: 0.95rem;
    color: #374151;
    background: #f9fafb;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid var(--accent-red);
}

.modal-details-list li strong {
    color: #111827;
    font-weight: 600;
}

.featured-badge {
    background: #fef2f2;
    color: #d61f26;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    margin-left: auto;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    border: 1px solid #fecaca;
    transition: all 0.2s ease;
}

.featured-badge:hover {
    background: #fee2e2;
    transform: scale(1.05);
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if ".modal-overlay" not in css_content:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + css_to_add)


# 2. Update HTML files
html_to_add = """
<!-- Home Loan Modal -->
<div id="homeLoanModal" class="modal-overlay">
    <div class="modal-content">
        <button class="modal-close" onclick="closeHomeLoanModal()">&times;</button>
        <div class="modal-header">
            <h2>?? Pre-Approved Home Loan</h2>
        </div>
        <div class="modal-body">
            <ul class="modal-details-list">
                <li><strong>Relationship Value (RV):</strong> ? 2.5 Crore</li>
                <li><strong>Eligibility:</strong> Pre-approved up to 3X of RV (? 7.5 Crore)</li>
                <li><strong>Processing Charge:</strong> Nil (0 with Solitaire)</li>
                <li><strong>Tenure:</strong> Up to 20 Years</li>
                <li><strong>Interest Rate:</strong> 7.8% p.a.</li>
            </ul>
        </div>
    </div>
</div>

<script>
function openHomeLoanModal() {
    document.getElementById('homeLoanModal').classList.add('show');
}
function closeHomeLoanModal() {
    document.getElementById('homeLoanModal').classList.remove('show');
}
// Close if clicked outside the content
window.addEventListener('click', function(e) {
    if (e.target == document.getElementById('homeLoanModal')) {
        closeHomeLoanModal();
    }
});
</script>
"""

files = ['experience_solitaire_dashboard.html', 'experience_solitaire_dashboard_new.html']
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2a. Replace Home Loan header
    old_header = r'<div class="feat-card-header"><span class="feat-icon">??</span><h3>Home Loan</h3></div>'
    new_header = '<div class="feat-card-header"><span class="feat-icon">\U0001F3E0</span><h3>Home Loan</h3><span class="featured-badge" onclick="openHomeLoanModal()">? Featured</span></div>'
    
    # Using regex just in case there are spacing differences, though direct string replace is safer if exact.
    # We'll use re.sub with a flexible pattern if literal replace fails.
    if '<div class="feat-card-header"><span class="feat-icon">??</span><h3>Home Loan</h3></div>' in content:
        content = content.replace('<div class="feat-card-header"><span class="feat-icon">??</span><h3>Home Loan</h3></div>', new_header)
    else:
        # Fallback to regex
        content = re.sub(r'<div class="feat-card-header">\s*<span class="feat-icon">??</span>\s*<h3>Home Loan</h3>\s*</div>', new_header, content)

    # 2b. Add Modal HTML before </body> if not exists
    if "id=\"homeLoanModal\"" not in content:
        content = content.replace('</body>', html_to_add + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating HTML and CSS.")
