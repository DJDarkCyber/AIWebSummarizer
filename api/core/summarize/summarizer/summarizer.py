import asyncio

from core.summarize.summarizer.scrapper import WebScrapper
from core.summarize.summarizer.ai_summarizer import Claude35Haiku

async def summarizer(url):
    scrapper = WebScrapper(url)
    text = await scrapper.run()
    ai_summarizer = Claude35Haiku(text)
    ai_summarized = ai_summarizer.summarize()
    # print("Extracted Text:\n", text)
    # print(ai_summarized)
    return ai_summarized
    
