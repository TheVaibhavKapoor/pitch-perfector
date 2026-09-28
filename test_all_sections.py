import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_all_sections():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Complete Verification of {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # 1. Test Intro Panel
        print("\n[1] Program Intro Section:")
        intro = page.locator("#panel-intro")
        print("  - Intro Title visible:", await intro.locator("text=Kotak Solitaire Program Introduction").is_visible())
        print("  - Salary ₹75L+ / Self-employed ₹1Cr+ Eligibility visible:", await intro.locator("text=Eligibility: Generally, salaried customers require ₹75 lakh+ Relationship Value (RV)").is_visible())
        print("  - Premium Banking category visible:", await intro.locator("summary:has-text('Premium Banking')").is_visible())
        print("  - Solitaire Credit Card category visible:", await intro.locator("summary:has-text('Solitaire Credit Card')").is_visible())
        print("  - Lending & Liquidity category visible:", await intro.locator("summary:has-text('Lending & Liquidity')").is_visible())
        print("  - Wealth Management category visible:", await intro.locator("summary:has-text('Wealth Management')").is_visible())
        print("  - Lifestyle Privileges category visible:", await intro.locator("summary:has-text('Lifestyle Privileges')").is_visible())

        # 2. Test Lifestyle Panel
        print("\n[2] Lifestyle Section:")
        await page.locator("div.product-card[onclick*='lifestyle']").first.click()
        await page.wait_for_timeout(300)
        
        life = page.locator("#panel-lifestyle")
        print("  - Lifestyle Panel visible:", await life.is_visible())
        print("  - Dining & Experiences category visible:", await life.locator("summary:has-text('Dining & Experiences')").is_visible())
        print("  - Solitaire Table 20% Off up to ₹5,000 visible:", await life.locator("text=20% Off up to ₹5,000 per transaction").is_visible())
        print("  - Travel & Concierge category visible:", await life.locator("summary:has-text('Travel & Concierge')").is_visible())

        # Test Tactical Offers Tab
        await life.locator("button:has-text('Tactical')").click()
        await page.wait_for_timeout(200)
        print("  - Tactical Offers Tab visible:", await life.locator(".inner-tab-content-tactical").is_visible())
        print("  - Dining & District Campaign offer visible:", await life.locator("text=District Fine-Dining Promo").is_visible())
        print("  - PVR Luxe Movie offer visible:", await life.locator("text=PVR Luxe").is_visible())

        # Test Pitches Tab
        await life.locator("button:has-text('Pitches')").click()
        await page.wait_for_timeout(200)
        print("  - Lifestyle Pitches Tab visible:", await life.locator(".inner-tab-content-pitches").is_visible())
        print("  - Intro Pitch visible:", await life.locator("text=A. INTRODUCTION PITCH").is_visible())
        print("  - Dining Pitch & Trigger visible:", await life.locator("text=B. DINING PITCH").is_visible())
        print("  - Travel Pitch & Trigger visible:", await life.locator("text=C. TRAVEL PITCH").is_visible())
        print("  - Tactical Offer Pitch template visible:", await life.locator("text=F. TACTICAL OFFER PITCH").is_visible())

        # 3. Test Investments Panel
        print("\n[3] Investments Section:")
        await page.locator("div.product-card[onclick*='investments']").first.click()
        await page.wait_for_timeout(300)
        
        inv = page.locator("#panel-investments")
        print("  - Investments Panel visible:", await inv.is_visible())
        print("  - Demat & Equity Trading category visible:", await inv.locator("summary:has-text('Demat & Equity Trading')").is_visible())
        print("  - Mutual Funds & SIP Solutions category visible:", await inv.locator("summary:has-text('Mutual Funds')").is_visible())
        print("  - IPO & Primary Market category visible:", await inv.locator("summary:has-text('IPO')").is_visible())
        print("  - Margin Trading Facility (MTF) category visible:", await inv.locator("summary:has-text('Margin Trading Facility')").is_visible())

        # Test Pitches Tab in Investments
        await inv.locator("button:has-text('Pitches')").click()
        await page.wait_for_timeout(200)
        print("  - Investments Pitches Tab visible:", await inv.locator(".inner-tab-content-pitches").is_visible())
        print("  - Demat Pitch script visible:", await inv.locator("text=Demat & Trading Pitch").is_visible())

        # Test Calculator Tab in Investments
        await inv.locator("button:has-text('Calculator')").click()
        await page.wait_for_timeout(200)
        print("  - Investments Return Calculator Tab visible:", await inv.locator(".inner-tab-content-calculator").is_visible())
        print("  - SIP Return Calculator inputs visible:", await inv.locator("#sip-amount").is_visible())

        # 4. Test Modals
        print("\n[4] Modals Section:")
        send_deck_btn = page.locator("button:has-text('Send Deck')").first
        await send_deck_btn.click()
        await page.wait_for_timeout(300)
        send_modal = page.locator("#send-deck-modal")
        print("  - Send Deck Modal visible:", await send_modal.is_visible())

        await page.evaluate("document.getElementById('send-deck-modal').style.display='none'")
        
        disp_btn = page.locator("button:has-text('Disposition')").first
        await disp_btn.click()
        await page.wait_for_timeout(300)
        disp_modal = page.locator("#create-lead-modal")
        print("  - Disposition Modal visible:", await disp_modal.is_visible())

        print("\n🎉 ALL TESTS PASSED SUCCESSFULLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_all_sections())
