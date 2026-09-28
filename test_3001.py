import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_modals_on_3001(url):
    print(f"\n==================== Testing Modals on {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # Test Send Deck button
        send_deck_btn = page.locator("button:has-text('Send Deck')").first
        if await send_deck_btn.count() > 0:
            print("Clicking Send Deck button...")
            await send_deck_btn.click()
            await page.wait_for_timeout(500)
            
            modal = page.locator("#send-deck-modal")
            is_vis = await modal.is_visible()
            comp_display = await modal.evaluate("el => window.getComputedStyle(el).display")
            print(f"  #send-deck-modal is_visible: {is_vis}, computed display: '{comp_display}'")
            
        # Close modal
        await page.evaluate("() => { const m = document.getElementById('send-deck-modal'); if(m) m.style.display='none'; }")

        # Test Disposition button
        disp_btn = page.locator("button:has-text('Disposition')").first
        if await disp_btn.count() > 0:
            print("Clicking Disposition button...")
            await disp_btn.click()
            await page.wait_for_timeout(500)
            
            modal = page.locator("#create-lead-modal")
            is_vis = await modal.is_visible()
            comp_display = await modal.evaluate("el => window.getComputedStyle(el).display")
            print(f"  #create-lead-modal is_visible: {is_vis}, computed display: '{comp_display}'")

        await browser.close()

async def main():
    await test_modals_on_3001("http://localhost:3001/experience_solitaire_dashboard_new.html")
    await test_modals_on_3001("http://localhost:3001/customer_overview_solitaire.html")

if __name__ == "__main__":
    asyncio.run(main())
