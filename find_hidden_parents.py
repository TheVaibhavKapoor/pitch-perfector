import asyncio, sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def find_hidden_parents(url):
    print(f"\n==================== Checking Parent Chain for {url} ====================")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        
        script = """
        (id) => {
            const el = document.getElementById(id);
            if (!el) return `Element #${id} not found`;
            
            const chain = [];
            let curr = el;
            while (curr) {
                const style = window.getComputedStyle(curr);
                chain.push({
                    tag: curr.tagName,
                    id: curr.id,
                    className: curr.className,
                    display: style.display,
                    visibility: style.visibility,
                    opacity: style.opacity
                });
                curr = curr.parentElement;
            }
            return chain;
        }
        """
        
        for mid in ["send-deck-modal", "create-lead-modal", "compare-modal"]:
            chain = await page.evaluate(script, mid)
            print(f"\n--- Parent Chain for #{mid} ---")
            if isinstance(chain, str):
                print(chain)
            else:
                for idx, node in enumerate(chain):
                    print(f"  Level {idx}: <{node['tag']} id='{node['id']}' class='{node['className']}'> -> display: '{node['display']}', visibility: '{node['visibility']}'")

        await browser.close()

async def main():
    await find_hidden_parents("http://localhost:3000/experience_solitaire_dashboard_new.html")
    await find_hidden_parents("http://localhost:3000/customer_overview_solitaire.html")

if __name__ == "__main__":
    asyncio.run(main())
