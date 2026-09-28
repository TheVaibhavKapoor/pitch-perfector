import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def test_page(url):
    print(f"\n==================== Testing {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Listen for console messages and errors
        page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        
        try:
            await page.goto(url, wait_until="networkidle", timeout=10000)
        except Exception as e:
            print(f"Failed to load {url}: {e}")
            await browser.close()
            return
            
        print("Page loaded successfully.")
        
        # Test Send Deck button
        print("\n--- Testing Send Deck Button ---")
        send_deck_btn = page.locator("button:has-text('Send Deck')").first
        if await send_deck_btn.count() > 0:
            print("Send Deck button found. Clicking...")
            await send_deck_btn.click()
            await page.wait_for_timeout(1000)
            
            modal = page.locator("#send-deck-modal")
            is_vis = await modal.is_visible()
            comp_display = await modal.evaluate("el => window.getComputedStyle(el).display")
            comp_z = await modal.evaluate("el => window.getComputedStyle(el).zIndex")
            print(f"send-deck-modal is_visible: {is_vis}, computed display: '{comp_display}', z-index: '{comp_z}'")
            if not is_vis:
                # check bounding box or parent visibility
                bbox = await modal.bounding_box()
                print(f"Bounding box: {bbox}")
                parent_vis = await modal.evaluate("el => window.getComputedStyle(el.parentElement).display")
                print(f"Parent display: '{parent_vis}'")
        else:
            print("Send Deck button NOT FOUND!")

        # Close send deck if open
        await page.evaluate("() => { const m = document.getElementById('send-deck-modal'); if(m) m.style.display='none'; }")

        # Test Disposition button
        print("\n--- Testing Disposition Button ---")
        disp_btn = page.locator("button:has-text('Disposition')").first
        if await disp_btn.count() > 0:
            print("Disposition button found. Clicking...")
            await disp_btn.click()
            await page.wait_for_timeout(1000)
            
            modal = page.locator("#create-lead-modal")
            is_vis = await modal.is_visible()
            comp_display = await modal.evaluate("el => window.getComputedStyle(el).display")
            comp_z = await modal.evaluate("el => window.getComputedStyle(el).zIndex")
            print(f"create-lead-modal is_visible: {is_vis}, computed display: '{comp_display}', z-index: '{comp_z}'")
            if not is_vis:
                bbox = await modal.bounding_box()
                print(f"Bounding box: {bbox}")
        else:
            print("Disposition button NOT FOUND!")

        await browser.close()

async def main():
    await test_page("http://localhost:3000/experience_solitaire_dashboard_new.html")
    await test_page("http://localhost:3000/customer_overview_solitaire.html")

if __name__ == "__main__":
    asyncio.run(main())
