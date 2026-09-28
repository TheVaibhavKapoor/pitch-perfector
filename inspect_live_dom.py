import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def inspect_dom(url):
    print(f"\n==================== Playwright DOM Inspection for {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        
        # Check if #send-deck-modal is inside #compare-modal in actual DOM
        is_child = await page.evaluate("""() => {
            const comp = document.getElementById('compare-modal');
            const send = document.getElementById('send-deck-modal');
            return comp.contains(send);
        }""")
        print(f"Is #send-deck-modal INSIDE #compare-modal in live DOM? -> {is_child}")
        
        is_create_child = await page.evaluate("""() => {
            const comp = document.getElementById('compare-modal');
            const create = document.getElementById('create-lead-modal');
            return comp.contains(create);
        }""")
        print(f"Is #create-lead-modal INSIDE #compare-modal in live DOM? -> {is_create_child}")

        # Check where #send-deck-modal is in document.body
        send_parent = await page.evaluate("""() => {
            const send = document.getElementById('send-deck-modal');
            return send ? send.parentElement.outerHTML.slice(0, 150) : 'NULL';
        }""")
        print(f"Parent of #send-deck-modal: {send_parent}")

        await browser.close()

async def main():
    await inspect_dom("http://localhost:3000/experience_solitaire_dashboard_new.html")
    await inspect_dom("http://localhost:3000/customer_overview_solitaire.html")

if __name__ == "__main__":
    asyncio.run(main())
