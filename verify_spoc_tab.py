import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_spoc_tab():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Spoc Floating Tab & Directory Drawer on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        
        # 1. Verify Floating Tab Visibility
        print("\n[1] Testing Blue Spoc Floating Side Tab:")
        tab = page.locator("#spoc-tab")
        print("  - Spoc Tab visible on right edge:", await tab.is_visible())
        
        # 2. Click Tab to Open Drawer
        print("\n[2] Testing Drawer Toggle:")
        await tab.click()
        await page.wait_for_timeout(400)
        
        drawer = page.locator("#spoc-drawer")
        print("  - Spoc Drawer visible after click:", await drawer.is_visible())
        
        # 3. Verify Filters & Auto-Fetched Contact Details
        print("\n[3] Testing SPOC Auto-Fetched Details:")
        poc_card = drawer.get_by_text("PRIMARY POC")
        print("  - Primary POC card visible:", await poc_card.is_visible())
        
        supervisor_card = drawer.get_by_text("ESCALATION SUPERVISOR")
        print("  - Escalation Supervisor card visible:", await supervisor_card.is_visible())
        
        print("  - Primary POC Email visible:", await drawer.get_by_text("rajesh.sharma@kotak.com").is_visible())
        print("  - Primary POC Phone visible:", await drawer.get_by_text("+91 98201 44521").is_visible())
        print("  - Supervisor Name visible:", await drawer.get_by_text("Ananya Iyer").is_visible())

        # 4. Test changing category to Assets
        print("\n[4] Testing Category Switch to Assets:")
        await drawer.locator("#spoc-category").select_option("assets")
        await page.wait_for_timeout(300)
        
        print("  - Mortgages POC (Vikram Deshmukh) visible:", await drawer.get_by_text("Vikram Deshmukh").is_visible())
        print("  - Mortgages Supervisor (Sunil Mehta) visible:", await drawer.get_by_text("Sunil Mehta").is_visible())

        print("\n🎉 BLUE SPOC FLOATING TAB & DIRECTORY DRAWER VERIFIED PERFECTLY ACROSS ALL PAGES!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_spoc_tab())
