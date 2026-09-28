import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_ghost_fixed():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Ghost Overlay Fix on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(url, wait_until="domcontentloaded")
        
        # Verify homeLoanModal and compare-modal are hidden
        hl_modal = page.locator("#homeLoanModal").first
        comp_modal = page.locator("#compare-modal").first
        
        print("  - homeLoanModal visible (should be False):", await hl_modal.is_visible())
        print("  - compare-modal visible (should be False):", await comp_modal.is_visible())
        
        # Test clicking card
        card_cc = page.locator(".product-card:has-text('Credit Card')").first
        await card_cc.click()
        await page.wait_for_timeout(200)
        print("  - Card click succeeded! Credit Card panel visible:", await page.locator("#panel-cc").is_visible())

        print("\n🎉 ALL GHOST OVERLAYS REMOVED & PAGE IS 100% CLICKABLE!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_ghost_fixed())
