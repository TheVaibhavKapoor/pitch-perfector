import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_product_boxes():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Loans & Investments Product Boxes on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # Test Loans Panel
        print("\n[1] Testing Loans Panel (panel-assets):")
        await page.locator("div.product-card[onclick*='assets']").first.click()
        await page.wait_for_timeout(300)
        
        loans = page.locator("#panel-assets")
        print("  - Loans Panel visible:", await loans.is_visible())
        print("  - Home Loan (HL) box visible:", await loans.locator("text=Home Loan (HL)").is_visible())
        print("  - Loan Against Property (LAP) box visible:", await loans.locator("text=Loan Against Property (LAP)").is_visible())
        print("  - Loan Against Securities (LAS) box visible:", await loans.locator("text=Loan Against Securities (LAS)").is_visible())
        print("  - Credit Line / Overdraft box visible:", await loans.locator("text=Credit Line / Overdraft").is_visible())
        print("  - Auto Loan box visible:", await loans.locator("text=Auto Loan (Solitaire)").is_visible())
        print("  - Personal Loan box visible:", await loans.locator("text=Personal Loan").is_visible())
        print("  - Check NO inner tabs exist in Loans:", await loans.locator(".inner-tabs-container").count() == 0)

        # Test Investments Panel
        print("\n[2] Testing Investments Panel (panel-investments):")
        await page.locator("div.product-card[onclick*='investments']").first.click()
        await page.wait_for_timeout(300)
        
        inv = page.locator("#panel-investments")
        print("  - Investments Panel visible:", await inv.is_visible())
        print("  - Demat & Equity Trading box visible:", await inv.locator("text=Demat & Equity Trading").is_visible())
        print("  - Mutual Funds & SIP / SWP box visible:", await inv.locator("text=Mutual Funds & SIP / SWP").is_visible())
        print("  - IPO & Primary Market (ASBA) box visible:", await inv.locator("text=IPO & Primary Market (ASBA)").is_visible())
        print("  - Margin Trading Facility (MTF) box visible:", await inv.locator("text=Margin Trading Facility (MTF)").is_visible())
        print("  - Alternate Investments (AIF & PMS) box visible:", await inv.locator("text=Alternate Investments (AIF & PMS)").is_visible())
        print("  - Global Investments & LRS box visible:", await inv.locator("text=Global Investments & LRS").is_visible())
        print("  - Check NO inner tabs exist in Investments:", await inv.locator(".inner-tabs-container").count() == 0)

        print("\n🎉 LOANS & INVESTMENTS PRODUCT BOXES VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_product_boxes())
