# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire_dashboard.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace everything from <script> to the end
new_script = '''<script>
        function showPanel(panelName, element) {
            // Update active state on product cards
            const grid = element.closest('.product-grid');
            if (grid) {
                const cards = grid.querySelectorAll('.product-card');
                cards.forEach(card => card.classList.remove('active'));
                element.classList.add('active');
            }

            // Hide all panels in this segment
            const segmentContainer = element.closest('.segment-wrapper');
            if (segmentContainer) {
                const panels = segmentContainer.querySelectorAll('.info-panel');
                panels.forEach(p => p.classList.remove('active'));
                
                // Get segment prefix (e.g., 'individual' or 'business')
                const segmentId = segmentContainer.id.split('-')[1];
                
                // Show selected panel
                const panelId = 'panel-' + segmentId + '-' + panelName;
                const panel = document.getElementById(panelId);
                if(panel) {
                    panel.classList.add('active');
                }
            }
        }

        function setSegment(segmentName, element) {
            // Update active tab styling
            document.querySelectorAll('.segment-tab').forEach(tab => {
                tab.style.color = '#6b7280';
                tab.style.borderBottom = '2px solid transparent';
            });
            if (element) {
                element.style.color = '#d61f26';
                element.style.borderBottom = '2px solid #d61f26';
            }
            
            // Format segment ID (e.g. "Corporate Salary" -> "corporate-salary", "Individual" -> "individual")
            let segmentId = segmentName.toLowerCase().replace(' ', '-');
            
            // Note: Currently we only have 'individual' and 'business' contents. 
            // Corporate salary can share individual for now if it doesn't have its own.
            if (segmentId === 'corporate-salary') {
                segmentId = 'individual'; 
            }
            
            // Hide all segment content
            const allSegments = document.querySelectorAll('.segment-wrapper');
            allSegments.forEach(seg => seg.style.display = 'none');
            
            // Show selected segment content
            const selContent = document.getElementById('segment-' + segmentId + '-content');
            if(selContent) {
                selContent.style.display = 'block';
                
                // Default select the Credit Card tab in the newly shown segment
                const ccCard = selContent.querySelector('[onclick="showPanel(\\'cc\\', this)"]');
                if (ccCard) {
                    showPanel('cc', ccCard);
                }
            }
        }
        
        window.onload = function() {
            // Load user details from localStorage
            const name = localStorage.getItem('solitaire_customer_name');
            const type = localStorage.getItem('solitaire_type');
            
            if (name) {
                const nameEl = document.getElementById('disp-name');
                if (nameEl) nameEl.innerText = name;
            }
            if (type) {
                const typeEl = document.getElementById('disp-type');
                if (typeEl) typeEl.innerText = type + ' Customer';
            }
            
            // Initialize first tab
            const firstTab = document.querySelector('.segment-tab');
            if (firstTab) {
                setSegment('Individual', firstTab);
            }
        }
    </script>
</body>
</html>'''

html = re.sub(r'<script>.*', new_script, html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed script and interactivity")
