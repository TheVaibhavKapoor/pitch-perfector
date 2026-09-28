import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def verify_updated_dashboard():
    url = "http://localhost:3001/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # 1. Verify Program Intro
        print("Checking Program Intro...")
        intro_text = await page.locator("#panel-intro").inner_text()
        print(f"  Program Intro contains 'Kotak Solitaire is Kotak Mahindra Bank': {'Kotak Solitaire is Kotak Mahindra Bank' in intro_text}")
        print(f"  Program Intro contains 'Eligibility: Generally, salaried customers': {'Eligibility: Generally, salaried customers' in intro_text}")
        print(f"  Program Intro contains 'Premium Banking': {'Premium Banking' in intro_text}")
        
        # 2. Verify Lifestyle Panel
        print("\nChecking Lifestyle Panel...")
        await page.evaluate("showPanel('lifestyle', document.querySelector('.product-card:nth-child(2)'))")
        await page.wait_for_timeout(500)
        
        life_panel = page.locator("#panel-lifestyle")
        print(f"  Lifestyle panel visible: {await life_panel.is_visible()}")
        
        # Test Tactical Offers tab in Lifestyle
        tactical_btn = page.locator("#panel-lifestyle button:has-text('Tactical')").first
        if await tactical_btn.count() > 0:
            await tactical_btn.click()
            await page.wait_for_timeout(300)
            tactical_content = page.locator("#panel-lifestyle .inner-tab-content-tactical")
            print(f"  Tactical Offers content visible: {await tactical_content.is_visible()}")
            
        # Test Pitches tab in Lifestyle
        pitches_btn = page.locator("#panel-lifestyle button:has-text('Pitches')").first
        if await pitches_btn.count() > 0:
            await pitches_btn.click()
            await page.wait_for_timeout(300)
            pitches_content = page.locator("#panel-lifestyle .inner-tab-content-pitches")
            print(f"  Pitches content visible: {await pitches_content.is_visible()}")

        # 3. Verify Investments Panel
        print("\nChecking Investments Panel...")
        await page.evaluate("showPanel('investments', document.querySelector('.product-card:nth-child(5)'))")
        await page.wait_for_timeout(500)
        
        inv_panel = page.locator("#panel-investments")
        print(f"  Investments panel visible: {await inv_panel.is_visible()}")

        # Test Pitches tab in Investments
        inv_pitches_btn = page.locator("#panel-investments button:has-text('Pitches')").first
        if await inv_pitches_btn.count() > 0:
            await inv_pitches_btn.click()
            await page.wait_for_timeout(300)
            inv_pitches_content = page.locator("#panel-investments .inner-tab-content-pitches")
            print(f"  Investments Pitches content visible: {await inv_pitches_content.is_visible()}")

        # Test Calculator tab in Investments
        inv_calc_btn = page.locator("#panel-investments button:has-text('Calculator')").first
        if await inv_calc_btn.count() > 0:
            await inv_calc_btn.click()
            await page.wait_for_timeout(300)
            inv_calc_content = page.locator("#panel-investments .inner-tab-content-calculator")
            print(f"  Investments Calculator content visible: {await inv_calc_content.is_visible()}")

        # 4. Verify Modals
        print("\nChecking Modals...")
        send_deck_btn = page.locator("button:has-text('Send Deck')").first
        await send_deck_btn.click()
        await page.wait_for_timeout(400)
        send_modal = page.locator("#send-deck-modal")
        print(f"  Send Deck Modal visible: {await send_modal.is_visible()}")

        await page.evaluate("document.getElementById('send-deck-modal').style.display='none'")
        
        disp_btn = page.locator("button:has-text('Disposition')").first
        await disp_btn.click()
        await page.wait_for_timeout(400)
        disp_modal = page.locator("#create-lead-modal")
        print(f"  Disposition Modal visible: {await disp_modal.is_visible()}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_updated_dashboard())
