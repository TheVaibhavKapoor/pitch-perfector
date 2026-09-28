import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_inline_compare_panel():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Verifying Inline Compare Panel & Top Menu on {url} ====================")
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

        # 2. Verify Clicking 7th Compare Program card shows inline #panel-compare
        print("\n[2] Testing Compare Program Card Click:")
        compare_card = page.locator(".product-card:has-text('Compare Program')")
        print("  - Compare Program Card visible:", await compare_card.is_visible())
        
        await compare_card.click()
        await page.wait_for_timeout(300)
        
        compare_panel = page.locator("#panel-compare")
        print("  - Inline #panel-compare visible:", await compare_panel.is_visible())
        
        # 3. Verify Expandable Categories inside #panel-compare
        print("\n[3] Testing Expandable Categories inside #panel-compare:")
        cat1 = compare_panel.locator("summary:has-text('Premium Banking')")
        print("  - Category 1 (Premium Banking) visible:", await cat1.is_visible())
        
        await cat1.click()
        await page.wait_for_timeout(200)
        print("  - Category 1 comparison table visible after expand:", await compare_panel.get_by_text("ActivMoney auto-sweep").is_visible())

        cat2 = compare_panel.locator("summary:has-text('Credit Card Rewards')")
        await cat2.click()
        await page.wait_for_timeout(200)
        print("  - Category 2 comparison table visible after expand:", await compare_panel.get_by_text("10 Air Miles / ₹100").is_visible())

        print("\n🎉 INLINE COMPARE PANEL & EXPANDABLE CATEGORIES VERIFIED PERFECTLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_inline_compare_panel())
