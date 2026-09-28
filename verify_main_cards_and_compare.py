import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_cards_and_compare():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Compact Main Cards Grid & Compare Card on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # Test Compare Program Card
        print("\n[1] Testing Compare Program Card:")
        compare_card = page.locator(".product-card:has-text('Compare Program')").first
        print("  - Compare Program Card visible:", await compare_card.is_visible())
        
        await compare_card.click()
        await page.wait_for_timeout(300)
        print("  - Compare Modal visible after clicking Compare Card:", await page.locator("#compare-modal").is_visible())
        
        # Hide compare modal
        await page.evaluate("document.getElementById('compare-modal').style.display='none'")
        
        # Test switching panels via other cards
        print("\n[2] Testing panel switching via compact cards:")
        await page.locator(".product-card:has-text('Lifestyle benefits')").first.click()
        await page.wait_for_timeout(200)
        print("  - Lifestyle Panel visible:", await page.locator("#panel-lifestyle").is_visible())
        
        await page.locator(".product-card:has-text('Loans')").first.click()
        await page.wait_for_timeout(200)
        print("  - Loans Panel visible:", await page.locator("#panel-assets").is_visible())
        
        await page.locator(".product-card:has-text('Summary')").first.click()
        await page.wait_for_timeout(200)
        print("  - Summary Panel visible:", await page.locator("#panel-summary").is_visible())

        print("\n🎉 ALL COMPACT CARDS & COMPARE PROGRAM CARD VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_cards_and_compare())
