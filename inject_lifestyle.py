import os
from bs4 import BeautifulSoup

def update_lifestyle_panel_styled(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    panel_lifestyle = soup.find(id='panel-lifestyle')
    if not panel_lifestyle:
        print(f"Could not find panel-lifestyle in {filename}")
        return
        
    # Clear existing content
    panel_lifestyle.clear()
    
    # Header
    header = soup.new_tag('h2', style="font-size: 1.35rem; font-weight: 800; color: #0f172a; margin-bottom: 8px;")
    header.string = "Lifestyle Benefits"
    panel_lifestyle.append(header)
    
    desc = soup.new_tag('p', style="color: #64748b; line-height: 1.6; margin-bottom: 24px;")
    desc.string = "Elevate your everyday experiences with unmatched lifestyle privileges and curated offers."
    panel_lifestyle.append(desc)
    
    # Sub-tabs container (using the exact pill-style container the user requested)
    tabs_div = soup.new_tag('div', class_="inner-tabs-container", style="display: flex; gap: 8px; margin-bottom: 24px; background: #f1f5f9; padding: 6px; border-radius: 12px;")
    
    tab_benefits = soup.new_tag('button', class_="inner-tab-btn active", style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #0f172a; background: white; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;", onclick="switchLifestyleTab('benefits', this)")
    tab_benefits.string = "Benefits"
    
    tab_offers = soup.new_tag('button', class_="inner-tab-btn", style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;", onclick="switchLifestyleTab('offers', this)")
    tab_offers.string = "Ongoing Offers"
    
    tab_pitches = soup.new_tag('button', class_="inner-tab-btn", style="flex: 1; padding: 10px 16px; font-size: 0.95rem; font-weight: 600; color: #475569; background: transparent; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s;", onclick="switchLifestyleTab('pitches', this)")
    tab_pitches.string = "Pitches"
    
    tabs_div.append(tab_benefits)
    tabs_div.append(tab_offers)
    tabs_div.append(tab_pitches)
    panel_lifestyle.append(tabs_div)
    
    # Script for switching tabs inside lifestyle panel (with correct styling updates for the pill UI)
    script = soup.new_tag('script')
    script.string = """
    function switchLifestyleTab(tabId, btn) {
        // Hide all lifestyle contents
        document.querySelectorAll('.lifestyle-content').forEach(el => el.style.display = 'none');
        
        // Reset all buttons
        const btns = btn.parentElement.querySelectorAll('button');
        btns.forEach(b => {
            b.classList.remove('active');
            b.style.background = 'transparent';
            b.style.color = '#475569';
            b.style.boxShadow = 'none';
        });
        
        // Show active content
        document.getElementById('lifestyle-' + tabId).style.display = 'block';
        
        // Highlight active button
        btn.classList.add('active');
        btn.style.background = 'white';
        btn.style.color = '#0f172a';
        btn.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
    }
    """
    panel_lifestyle.append(script)
    
    # --- BENEFITS CONTENT ---
    benefits_content = soup.new_tag('div', id="lifestyle-benefits", attrs={"class": "lifestyle-content"}, style="display: block;")
    benefits_html = """
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
        <h3 style="color: #0f172a; font-size: 1.15rem; font-weight: 700; margin-bottom: 16px;">Core Lifestyle Privileges</h3>
        <ul style="padding-left: 20px; line-height: 1.8; color: #475569; font-size: 0.95rem; list-style-type: disc;">
            <li style="margin-bottom: 8px;"><strong>District by Zomato – Solitaire Table:</strong> Exclusive dining and lifestyle privileges.</li>
            <li style="margin-bottom: 8px;"><strong>20% off on District:</strong> Up to ₹5,000 per transaction, 2 transactions/month, across eligible dining, nightlife, movies, shopping and experiences.</li>
            <li style="margin-bottom: 8px;"><strong>Exclusive District Experiences:</strong> Early access to select chef's tables, tasting menus, fine-dining and curated experiences.</li>
            <li style="margin-bottom: 8px;"><strong>Solitaire Concierge:</strong> Assistance with travel, hotels, restaurants, visa support, airport services, gifting, celebrations, shopping and relocation.</li>
            <li style="margin-bottom: 8px;"><strong>Luxury Hotel Benefits:</strong> Access to selected hotel/stay offers such as complimentary nights or discounted additional nights.</li>
            <li style="margin-bottom: 8px;"><strong>Zomato Gold:</strong> Eligible Solitaire customers can access promotional Zomato Gold membership offers.</li>
            <li style="margin-bottom: 8px;"><strong>Premium Travel:</strong> Unlimited domestic & international airport lounge access for eligible Solitaire cardholders.</li>
            <li style="margin-bottom: 8px;"><strong>Travel Rewards:</strong> 10 Air Miles/₹100 on eligible flight/hotel bookings through Kotak Unbox.</li>
            <li style="margin-bottom: 8px;"><strong>Zero Forex Markup:</strong> 0% forex markup on eligible Solitaire Credit Card international transactions.</li>
            <li style="margin-bottom: 8px;"><strong>Lifestyle & Entertainment:</strong> Access to dining, movie, shopping and entertainment privileges through Kotak's curated offers.</li>
            <li style="margin-bottom: 8px;"><strong>Family Benefits:</strong> Add-on cardholders can also access applicable premium card/lifestyle privileges.</li>
            <li style="margin-bottom: 8px;"><strong>Tactical Offers:</strong> Regularly refreshed offers across travel, dining, entertainment, shopping and lifestyle categories.</li>
        </ul>
    </div>
    """
    benefits_content.append(BeautifulSoup(benefits_html, 'html.parser'))
    panel_lifestyle.append(benefits_content)
    
    # --- ONGOING OFFERS CONTENT ---
    offers_content = soup.new_tag('div', id="lifestyle-offers", attrs={"class": "lifestyle-content"}, style="display: none;")
    offers_html = """
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px;">
            <h4 style="font-weight: 700; color: #1e3a8a; margin-bottom: 12px; font-size: 1.05rem;">🍽️ District by Zomato – Solitaire Table</h4>
            <ul style="padding-left: 20px; line-height: 1.6; color: #1e40af; font-size: 0.9rem;">
                <li>20% discount (Up to ₹5,000 per transaction)</li>
                <li>2 transactions/month</li>
                <li>Maximum potential benefit: ₹10,000/month</li>
                <li>Validity: 1 Apr 2026 – 31 Mar 2027</li>
                <li>Applicable on eligible dining, nightlife, movies, shopping, play and family experiences.</li>
            </ul>
        </div>
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px;">
            <h4 style="font-weight: 700; color: #166534; margin-bottom: 12px; font-size: 1.05rem;">✈️ 10X Air Miles – Eligible Vouchers</h4>
            <ul style="padding-left: 20px; line-height: 1.6; color: #15803d; font-size: 0.9rem;">
                <li>10 Air Miles/₹100 on eligible voucher purchases through Kotak Unbox.</li>
                <li>Current campaign: 1 Jul – 30 Sep 2026</li>
                <li>Accelerated Air Miles subject to applicable monthly cap.</li>
            </ul>
        </div>
        <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 16px;">
            <h4 style="font-weight: 700; color: #92400e; margin-bottom: 12px; font-size: 1.05rem;">🎬 PVR Buy 2 Get 1</h4>
            <ul style="padding-left: 20px; line-height: 1.6; color: #b45309; font-size: 0.9rem;">
                <li>Buy 2 or more eligible movie tickets and get 1 ticket free.</li>
                <li>Benefit up to ₹1,500. Up to 2 transactions/month.</li>
                <li>Current campaign: 1 Jul – 30 Sep 2026</li>
                <li>Applicable at participating PVR formats.</li>
            </ul>
        </div>
        <div style="background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 8px; padding: 16px;">
            <h4 style="font-weight: 700; color: #6b21a8; margin-bottom: 12px; font-size: 1.05rem;">🔄 30% Bonus Air Miles Transfer</h4>
            <ul style="padding-left: 20px; line-height: 1.6; color: #7e22ce; font-size: 0.9rem;">
                <li>30% bonus Air Miles when transferring eligible miles to participating airline/hotel partners.</li>
                <li>Partners: Air France-KLM, Air Canada, British Airways, Cathay Pacific, Etihad, Qatar Airways, United MileagePlus and Marriott Bonvoy.</li>
                <li>Current campaign: 1 Jul – 30 Sep 2026 (Subject to applicable caps and terms)</li>
            </ul>
        </div>
        <div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 8px; padding: 16px; grid-column: span 2;">
            <h4 style="font-weight: 700; color: #9d174d; margin-bottom: 12px; font-size: 1.05rem;">🏨 Hotel Offers</h4>
            <p style="color: #be185d; font-size: 0.9rem; margin-bottom: 8px;">Selected luxury hotel/stay offers such as 3rd night complimentary or 50% off the 2nd night, depending on the participating property and offer.</p>
            <p style="color: #64748b; font-size: 0.8rem; font-style: italic; margin-top: 12px;">Note: Offers are campaign-based and may change; eligibility, participating merchants, caps and T&Cs apply.</p>
        </div>
    </div>
    """
    offers_content.append(BeautifulSoup(offers_html, 'html.parser'))
    panel_lifestyle.append(offers_content)
    
    # --- PITCHES CONTENT ---
    pitches_content = soup.new_tag('div', id="lifestyle-pitches", attrs={"class": "lifestyle-content"}, style="display: none;")
    pitches_html = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
        <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 16px; border-radius: 0 8px 8px 0;">
            <h4 style="font-weight: 700; color: #0f172a; margin-bottom: 8px;">🗣️ General Lifestyle Pitch</h4>
            <p style="color: #334155; line-height: 1.6; font-style: italic;">“Sir/Ma'am, Solitaire is not just about premium banking. There are several lifestyle privileges attached to the relationship, and my role as your RM is to make sure you actually utilise them. Whether you're travelling, dining, shopping, watching a movie or planning an experience, I'll proactively keep you informed about relevant Solitaire benefits and offers.”</p>
        </div>
        <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 16px; border-radius: 0 8px 8px 0;">
            <h4 style="font-weight: 700; color: #0f172a; margin-bottom: 8px;">🍽️ District Pitch</h4>
            <p style="color: #334155; line-height: 1.6; font-style: italic;">“If you regularly dine out or use District, Solitaire currently gives you 20% off up to ₹5,000 per transaction, twice a month. You also get access to curated dining and lifestyle experiences. So before making a booking, I'd recommend checking the Solitaire benefit first.”</p>
        </div>
        <div style="background: #f8fafc; border-left: 4px solid #14b8a6; padding: 16px; border-radius: 0 8px 8px 0;">
            <h4 style="font-weight: 700; color: #0f172a; margin-bottom: 8px;">✈️ Travel Pitch</h4>
            <p style="color: #334155; line-height: 1.6; font-style: italic;">“If you travel frequently, Solitaire becomes particularly valuable. You get unlimited lounge access, zero forex markup and enhanced Air Miles on eligible flight and hotel bookings through Kotak Unbox. Before your next international trip, I'd suggest connecting with me so I can check the applicable travel benefits for you.”</p>
        </div>
        <div style="background: #f8fafc; border-left: 4px solid #8b5cf6; padding: 16px; border-radius: 0 8px 8px 0;">
            <h4 style="font-weight: 700; color: #0f172a; margin-bottom: 8px;">🛎️ Concierge Pitch</h4>
            <p style="color: #334155; line-height: 1.6; font-style: italic;">“One benefit I particularly want you to know about is Solitaire Concierge. If you need help with a hotel, restaurant reservation, travel planning, airport assistance, gifting or a special occasion, you can reach out to the Concierge. Think of it as an extension of your Solitaire relationship beyond banking.”</p>
        </div>
        <div style="background: #f8fafc; border-left: 4px solid #f59e0b; padding: 16px; border-radius: 0 8px 8px 0;">
            <h4 style="font-weight: 700; color: #0f172a; margin-bottom: 8px;">🎁 Tactical Offer Pitch</h4>
            <p style="color: #334155; line-height: 1.6; font-style: italic;">“Sir/Ma'am, there is currently a Solitaire offer that may be relevant to you. These tactical offers change periodically across travel, dining, entertainment and shopping. I'll keep an eye on the offers and proactively let you know whenever something matches your spending or upcoming plans.”</p>
        </div>
        <div style="background: #e0f2fe; border-left: 4px solid #0284c7; padding: 16px; border-radius: 0 8px 8px 0;">
            <h4 style="font-weight: 700; color: #0369a1; margin-bottom: 8px;">🎯 RM Positioning</h4>
            <p style="color: #075985; line-height: 1.6; font-weight: 600;">“You don't need to remember all your Solitaire benefits. Just remember me. Before any major travel, dining, shopping or lifestyle booking, reach out to me and I'll check what benefit is available for you.”</p>
        </div>
    </div>
    """
    pitches_content.append(BeautifulSoup(pitches_html, 'html.parser'))
    panel_lifestyle.append(pitches_content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filename}")


update_lifestyle_panel_styled('experience_solitaire_dashboard_new.html')
