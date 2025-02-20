from playwright.async_api import async_playwright

class WebScrapper:
    def __init__(self, url):
        self.url = url
    
    async def run(self):
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                extra_http_headers={
                    "Accept-Language": "en-US,en;q=0.9",
                    "Referer": self.url,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                }
            )
            page = await context.new_page()
            await page.goto(self.url, wait_until="domcontentloaded")  # Ensures content is loaded
            await page.wait_for_timeout(5000)
            all_text = await page.evaluate("document.body.innerText")
            await browser.close()
            return all_text
