import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def find_inv_parent_chain():
    url = "http://localhost:3000/experience_solitaire_dashboard_new.html"
    print(f"\n==================== Parent Chain for #panel-investments ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        
        chain = await page.evaluate("""() => {
            let curr = document.getElementById('panel-investments');
            const res = [];
            while (curr) {
                res.push({
                    tag: curr.tagName,
                    id: curr.id,
                    className: curr.className,
                    display: window.getComputedStyle(curr).display
                });
                curr = curr.parentElement;
            }
            return res;
        }""")
        
        for idx, item in enumerate(chain):
            print(f"Level {idx}: <{item['tag']} id='{item['id']}' class='{item['className']}'> -> display: '{item['display']}'")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(find_inv_parent_chain())
