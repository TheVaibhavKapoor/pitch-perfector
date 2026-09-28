import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def debug_inv_panel():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Debugging Investments Panel ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,svg,woff,woff2,ttf}", lambda route: route.abort())
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector("#panel-intro", timeout=5000)
        
        print("Initial state of #panel-investments:")
        print("  display:", await page.evaluate("window.getComputedStyle(document.getElementById('panel-investments')).display"))
        print("  classList:", await page.evaluate("Array.from(document.getElementById('panel-investments').classList)"))

        print("\nCalling showPanel('investments', document.querySelectorAll('.product-card')[4])...")
        await page.evaluate("""() => {
            const cards = document.querySelectorAll('.product-card');
            const invCard = Array.from(cards).find(c => c.getAttribute('onclick').includes("'investments'"));
            showPanel('investments', invCard);
        }""")
        await page.wait_for_timeout(300)

        print("State of #panel-investments after showPanel:")
        print("  display:", await page.evaluate("window.getComputedStyle(document.getElementById('panel-investments')).display"))
        print("  classList:", await page.evaluate("Array.from(document.getElementById('panel-investments').classList)"))
        print("  is_visible:", await page.locator("#panel-investments").is_visible())

        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_inv_panel())
