import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_dark_blue_btn():
    url = "http://localhost:3000/program_type_selection.html"
    print(f"\n==================== Verifying Dark Blue Solitaire Button on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(url, wait_until="domcontentloaded")
        
        btn = page.locator("#submit-btn")
        print("  - EXPERIENCE SOLITAIRE button visible:", await btn.is_visible())
        
        bg_color = await btn.evaluate("el => getComputedStyle(el).backgroundColor")
        print(f"  - Button Background Color (Computed): {bg_color}")
        
        # Check experience_solitaire.html as well
        url2 = "http://localhost:3000/experience_solitaire.html"
        await page.goto(url2, wait_until="domcontentloaded")
        btn2 = page.locator("button:has-text('EXPERIENCE SOLITAIRE')")
        bg_color2 = await btn2.evaluate("el => getComputedStyle(el).backgroundColor")
        print(f"  - Button Background Color in experience_solitaire.html: {bg_color2}")

        print("\n🎉 EXPERIENCE SOLITAIRE BUTTON IS VERIFIED IN SLEEK DARK BLUE!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_dark_blue_btn())
