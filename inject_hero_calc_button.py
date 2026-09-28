import re

calc_button_html = '''                        <div style="margin-top: 18px; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 16px;">
                            <span style="font-size: 0.85rem; font-weight: 600; opacity: 0.9;">Want to calculate your exact EMI &amp; interest savings?</span>
                            <button onclick="openHomeLoanModal()" style="background: #ffffff; color: #1e3a8a; border: none; padding: 10px 22px; border-radius: 8px; font-weight: 800; font-size: 0.88rem; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.15); transition: transform 0.2s;">
                                ?? CALCULATE INTEREST SAVINGS &rarr;
                            </button>
                        </div>
                    </div>'''

def update_file(filepath):
    print(f"Injecting calculator button into {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Target the end of the pill list before </div>
    target = '''                            <span style="background: rgba(255,255,255,0.14); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 600;">&#9989; Dedicated RM</span>
                        </div>
                    </div>'''

    replacement = '''                            <span style="background: rgba(255,255,255,0.14); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 600;">&#9989; Dedicated RM</span>
                        </div>
''' + calc_button_html

    if target in text:
        text = text.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"SUCCESS: Injected button into {filepath}")
    else:
        print(f"Target not found in {filepath}")

update_file('experience_solitaire_dashboard_new.html')
update_file('experience_solitaire_dashboard.html')
