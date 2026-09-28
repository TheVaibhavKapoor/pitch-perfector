import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_tab_math():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Testing Tab Positioning Math on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Inject fixed calc positioning test style
        await page.goto(url, wait_until="domcontentloaded")
        
        tab_k = page.locator("#kompanion-tab")
        tab_s = page.locator("#spoc-tab")
        
        box_k = await tab_k.bounding_box()
        box_s = await tab_s.bounding_box()
        
        print("\nCurrent Bounding Boxes:")
        print("  - Kompanion Tab:", box_k)
        print("  - Spoc Tab:", box_s)
        
        if box_k and box_s:
            bottom_k = box_k['y'] + box_k['height']
            top_s = box_s['y']
            gap = top_s - bottom_k
            print(f"\n  => Physical Vertical Gap: {gap:.2f}px")
            if gap < 0:
                print("  ❌ OVERLAP DETECTED!")
            else:
                print(f"  ✅ NO OVERLAP! Clean gap of {gap:.2f}px")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_tab_math())
