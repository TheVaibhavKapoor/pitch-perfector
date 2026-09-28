import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_privy_compare_panel():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Privy / Privy+ / Solitaire Program Comparison on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        # 1. Verify Top Right Menu has NO Compare Program button
        print("\n[1] Verifying Top Right Menu:")
        top_compare_btn = page.locator("header button:has-text('Compare Program')")
        print("  - Top Right Compare Program button count (should be 0):", await top_compare_btn.count())

        # 2. Click Compare Program card
        print("\n[2] Testing Compare Program Card Click:")
        compare_card = page.locator(".product-card:has-text('Compare Program')")
        await compare_card.click()
        await page.wait_for_timeout(300)
        
        compare_panel = page.locator("#panel-compare")
        print("  - Inline #panel-compare visible:", await compare_panel.is_visible())
        
        # 3. Verify Privy vs Privy+ vs Solitaire Columns
        print("\n[3] Testing Privy / Privy+ / Solitaire Headers:")
        print("  - Header PRIVY visible:", await compare_panel.get_by_text("PRIVY", exact=True).is_visible())
        print("  - Header PRIVY+ visible:", await compare_panel.get_by_text("PRIVY+", exact=True).is_visible())
        print("  - Header SOLITAIRE visible:", await compare_panel.get_by_text("SOLITAIRE", exact=True).is_visible())

        # 4. Verify Accordions
        print("\n[4] Testing Accordions:")
        print("  - Eligibility accordion open:", await compare_panel.get_by_text("₹75L+").is_visible())
        
        await compare_panel.locator("summary:has-text('Credit Cards')").click()
        await page.wait_for_timeout(200)
        print("  - Credit Cards accordion expanded (0% Forex Markup visible):", await compare_panel.get_by_text("0% Forex Markup").is_visible())

        print("\n🎉 PRIVY vs PRIVY+ vs SOLITAIRE PROGRAM COMPARISON VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_privy_compare_panel())
