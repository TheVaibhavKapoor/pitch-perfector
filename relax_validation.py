# -*- coding: utf-8 -*-
import os

filepath = r'c:\Users\vaibh\Desktop\Pitch Perfector\experience_solitaire.html'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove strict validations
    # Replace the body of submitWalkthrough
    import re
    new_func = '''function submitWalkthrough() {
            const selectedType = document.querySelector('input[name="customerType"]:checked');
            const type = selectedType ? selectedType.value : 'Existing';
            
            localStorage.setItem('solitaire_type', type);
            
            if (type === 'Existing') {
                const searchVal = document.getElementById('input-search').value;
                const dummyName = document.getElementById('dummy-name') ? document.getElementById('dummy-name').innerText : 'Vaibhav K';
                const dummyCrn = document.getElementById('dummy-crn') ? document.getElementById('dummy-crn').innerText : '987654321';
                
                localStorage.setItem('solitaire_customer_name', dummyName);
                localStorage.setItem('solitaire_customer_crn', dummyCrn);
            } else {
                const name = document.getElementById('input-name').value || 'New Customer';
                const phone = document.getElementById('input-phone').value || '9999999999';
                
                localStorage.setItem('solitaire_customer_name', name);
                localStorage.setItem('solitaire_customer_crn', 'NEW-' + Math.floor(1000 + Math.random() * 9000));
            }
            
            window.location.href = 'experience_solitaire_dashboard.html';
        }'''
        
    content = re.sub(r'function submitWalkthrough\(\)\s*\{.*?(?=</script>)', new_func + '\n\n    ', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated experience_solitaire.html")
