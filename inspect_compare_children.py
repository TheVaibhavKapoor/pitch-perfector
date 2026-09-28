import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def inspect_compare_children(url):
    print(f"\n==================== Compare Modal Children for {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        
        children = await page.evaluate("""() => {
            const comp = document.getElementById('compare-modal');
            return Array.from(comp.children).map(c => ({
                tag: c.tagName,
                id: c.id,
                className: c.className
            }));
        }""")
        print("Direct children of #compare-modal:")
        for idx, c in enumerate(children):
            print(f"  [{idx}] <{c['tag']} id='{c['id']}' class='{c['className']}'>")

        await browser.close()

async def main():
    await inspect_compare_children("http://localhost:3000/experience_solitaire_dashboard_new.html")
    await inspect_compare_children("http://localhost:3000/customer_overview_solitaire.html")

if __name__ == "__main__":
    asyncio.run(main())
