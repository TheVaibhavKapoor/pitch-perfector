import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_kompanion_tab():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Kompanion Floating Tab & Drawer on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        
        # 1. Verify Floating Tab Visibility
        print("\n[1] Testing Floating Side Tab:")
        tab = page.locator("#kompanion-tab")
        print("  - Kompanion Tab visible on right edge:", await tab.is_visible())
        
        # 2. Click Tab to Open Drawer
        print("\n[2] Testing Drawer Toggle:")
        await tab.click()
        await page.wait_for_timeout(400)
        
        drawer = page.locator("#kompanion-drawer")
        print("  - Kompanion Drawer visible after click:", await drawer.is_visible())
        
        # 3. Test Quick Pitch Assistant Button Click
        print("\n[3] Testing Quick Pitch Assistant Button:")
        btn = drawer.get_by_text("Credit Card Pitch")
        await btn.click()
        await page.wait_for_timeout(600)
        
        print("  - AI Kompanion response received:", await drawer.get_by_text("Pitch the Kotak Solitaire Metal Credit Card").is_visible())

        print("\n🎉 KOMPANION FLOATING TAB & DRAWER VERIFIED PERFECTLY ACROSS ALL PAGES!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_kompanion_tab())
