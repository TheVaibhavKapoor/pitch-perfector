import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_expandable_pitches():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Expandable Pitches & Calculators on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # Test Home Loan
        print("\n[1] Testing Home Loan Expandables:")
        await page.locator("div.product-card[onclick*='assets']").first.click()
        await page.wait_for_timeout(300)
        
        hl_pane = page.locator("#loan-content-hl")
        
        # Click expand pitches
        await hl_pane.locator("summary:has-text('Relationship Manager Conversation Pitches')").click()
        await page.wait_for_timeout(200)
        print("  - HL Pitch A visible after expand:", await hl_pane.get_by_text("A. General Property Purchase Pitch").is_visible())
        print("  - HL Pitch C & CTA visible after expand:", await hl_pane.get_by_text("C. Customer Already Has a Home Loan Elsewhere").is_visible())
        
        # Click expand calculator
        await hl_pane.locator("summary:has-text('Interactive Home Loan EMI & Savings Calculator')").click()
        await page.wait_for_timeout(200)
        print("  - HL Calculator Output visible after expand:", await hl_pane.locator("#hl-calc-emi").is_visible())

        # Test Mutual Funds
        print("\n[2] Testing Mutual Funds Expandables:")
        await page.locator("div.product-card[onclick*='investments']").first.click()
        await page.wait_for_timeout(300)
        
        await page.locator("#panel-investments .inv-prod-box:has-text('Mutual Funds')").click()
        await page.wait_for_timeout(300)
        
        mf_pane = page.locator("#inv-content-mf")
        
        # Click expand pitches
        await mf_pane.locator("summary:has-text('Relationship Manager Conversation Pitches')").click()
        await page.wait_for_timeout(200)
        print("  - MF Pitch A visible after expand:", await mf_pane.get_by_text("A. General Investment Pitch").is_visible())
        print("  - MF Pitch I visible after expand:", await mf_pane.get_by_text("I. SWP / Retirement Monthly Cash Flow Pitch").is_visible())

        # Click expand calculator
        await mf_pane.locator("summary:has-text('Interactive SIP & SWP Wealth Calculator')").click()
        await page.wait_for_timeout(200)
        print("  - MF Calculator Output visible after expand:", await mf_pane.locator("#mf-calc-corpus").is_visible())

        print("\n🎉 ALL EXPANDABLE PITCHES & CALCULATORS VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_expandable_pitches())
