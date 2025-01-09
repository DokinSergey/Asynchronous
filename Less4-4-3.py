import sys,time
import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
    "Конференция разработчиков игр пройдет онлайн",
    "Открыт новый вид подводных животных",]

headers = {"COVID-19":0.3,"игр":0.4, "новый вид":0.5}

async def analyze_news(keyword, delay):
    for news in news_list:
        if keyword.lower() in news.lower():
            print(f"Найдено соответствие для '{keyword}': {news}")
        await asyncio.sleep(delay)

async def main():
    tasks = [asyncio.create_task(analyze_news(header,header_delay)) for header,header_delay in headers.items()]


    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
