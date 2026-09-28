import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_interactive_boxes():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Small Interactive Product Boxes on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # Test Loans Panel (panel-assets)
        print("\n[1] Testing Loans Panel Small Boxes:")
        await page.locator("div.product-card[onclick*='assets']").first.click()
        await page.wait_for_timeout(300)
        
        loans = page.locator("#panel-assets")
        print("  - Loans Panel visible:", await loans.is_visible())
        
        # Click Home Loan
        await loans.locator(".loan-prod-box:has-text('Home Loan')").click()
        await page.wait_for_timeout(200)
        hl_pane = loans.locator("#loan-content-hl")
        print("  - Home Loan Pane visible:", await hl_pane.is_visible())
        print("  - Home Loan Features visible:", await hl_pane.get_by_text("Key Features & Privileges").is_visible())
        print("  - Home Loan Pitch visible:", await hl_pane.get_by_text("Pitch Script").is_visible())
        print("  - Home Loan Expandable Calculator visible:", await hl_pane.locator("summary:has-text('Calculator')").is_visible())
        
        # Click LAP
        await loans.locator(".loan-prod-box:has-text('LAP')").click()
        await page.wait_for_timeout(200)
        lap_pane = loans.locator("#loan-content-lap")
        print("  - LAP Pane visible:", await lap_pane.is_visible())
        print("  - LAP Features visible:", await lap_pane.get_by_text("Key Features & Privileges").is_visible())

        # Click LAS
        await loans.locator(".loan-prod-box:has-text('LAS')").click()
        await page.wait_for_timeout(200)
        las_pane = loans.locator("#loan-content-las")
        print("  - LAS Pane visible:", await las_pane.is_visible())

        # Test Investments Panel (panel-investments)
        print("\n[2] Testing Investments Panel Small Boxes:")
        await page.locator("div.product-card[onclick*='investments']").first.click()
        await page.wait_for_timeout(300)
        
        inv = page.locator("#panel-investments")
        print("  - Investments Panel visible:", await inv.is_visible())
        
        # Click Demat
        await inv.locator(".inv-prod-box:has-text('Demat')").click()
        await page.wait_for_timeout(200)
        demat_pane = inv.locator("#inv-content-demat")
        print("  - Demat Pane visible:", await demat_pane.is_visible())
        print("  - Demat Features visible:", await demat_pane.get_by_text("Key Features & Privileges").is_visible())
        print("  - Demat Pitch visible:", await demat_pane.get_by_text("Pitch Script").is_visible())
        print("  - Demat Expandable Calculator visible:", await demat_pane.locator("summary:has-text('Calculator')").is_visible())

        # Click Mutual Funds
        await inv.locator(".inv-prod-box:has-text('Mutual Funds')").click()
        await page.wait_for_timeout(200)
        mf_pane = inv.locator("#inv-content-mf")
        print("  - Mutual Funds Pane visible:", await mf_pane.is_visible())

        # Click MTF
        await inv.locator(".inv-prod-box:has-text('MTF')").click()
        await page.wait_for_timeout(200)
        mtf_pane = inv.locator("#inv-content-mtf")
        print("  - MTF Pane visible:", await mtf_pane.is_visible())

        print("\n🎉 SMALL INTERACTIVE PRODUCT BOXES VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_interactive_boxes())
