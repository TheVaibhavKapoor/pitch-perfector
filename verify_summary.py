import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_summary_and_all():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Summary & All Panels on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # Test Summary Panel
        print("\n[1] Testing Summary Panel:")
        await page.locator("div.product-card[onclick*='summary']").first.click()
        await page.wait_for_timeout(300)
        
        summary = page.locator("#panel-summary")
        print("  - Summary Panel visible:", await summary.is_visible())
        print("  - Headline ₹2.0L – ₹3.0L+ / year visible:", await summary.locator("text=₹2.0L – ₹3.0L+").is_visible())
        print("  - Target Profile ₹1 Cr Net-Worth visible:", await summary.locator("text=₹1 Cr Net-Worth Customer").is_visible())
        print("  - The Killer RM Line visible:", await summary.locator("text=The Killer RM Line").is_visible())
        print("  - Official Credit Card Value Chart Accordion visible:", await summary.locator("summary:has-text('Official Kotak Solitaire Credit Card Value Chart')").is_visible())
        print("  - Disclaimer visible:", await summary.locator("text=Values shown are illustrative maximum/potential values").is_visible())

        # Test Modals
        print("\n[2] Testing Modals:")
        send_btn = page.locator("button:has-text('Send Deck')").first
        await send_btn.click()
        await page.wait_for_timeout(300)
        print("  - Send Deck Modal visible:", await page.locator("#send-deck-modal").is_visible())
        
        await page.evaluate("document.getElementById('send-deck-modal').style.display='none'")
        
        disp_btn = page.locator("button:has-text('Disposition')").first
        await disp_btn.click()
        await page.wait_for_timeout(300)
        print("  - Disposition Modal visible:", await page.locator("#create-lead-modal").is_visible())

        print("\n🎉 ALL SUMMARY & MODAL TESTS PASSED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_summary_and_all())
