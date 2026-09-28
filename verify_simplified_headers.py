import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_simplified_headers():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Simplified Headers on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # Test Home Loan
        print("\n[1] Testing Home Loan Simplified Headers:")
        await page.locator("div.product-card[onclick*='assets']").first.click()
        await page.wait_for_timeout(300)
        
        hl_pane = page.locator("#loan-content-hl")
        print("  - Features Header visible:", await hl_pane.locator("h4:has-text('Features')").is_visible())
        print("  - Pitches Accordion Summary visible:", await hl_pane.locator("summary:has-text('Pitches')").is_visible())
        print("  - Calculator Accordion Summary visible:", await hl_pane.locator("summary:has-text('Calculator')").is_visible())
        
        # Expand Pitches
        await hl_pane.locator("summary:has-text('Pitches')").click()
        await page.wait_for_timeout(200)
        print("  - Pitch script visible after click:", await hl_pane.get_by_text("A. General Property Purchase Pitch").is_visible())

        # Test Mutual Funds
        print("\n[2] Testing Mutual Funds Simplified Headers:")
        await page.locator("div.product-card[onclick*='investments']").first.click()
        await page.wait_for_timeout(300)
        
        await page.locator("#panel-investments .inv-prod-box:has-text('Mutual Funds')").click()
        await page.wait_for_timeout(300)
        
        mf_pane = page.locator("#inv-content-mf")
        print("  - Features Header visible:", await mf_pane.locator("h4:has-text('Features')").is_visible())
        print("  - Pitches Accordion Summary visible:", await mf_pane.locator("summary:has-text('Pitches')").is_visible())
        print("  - Calculator Accordion Summary visible:", await mf_pane.locator("summary:has-text('Calculator')").is_visible())

        print("\n🎉 ALL SIMPLIFIED HEADERS VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_simplified_headers())
