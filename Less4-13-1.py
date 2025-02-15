import sys,time
import asyncio

articles = [
    {'title': 'Методы картирования генома', 'length': 3.2},
    {'title': 'Гормоны растений и их рост', 'length': 4.5},
    {'title': 'Применение CRISPR', 'length': 2.1},
    {'title': 'Микробное разнообразие', 'length': 1.5},
    {'title': 'Механика деления клеток', 'length': 4.1},
    {'title': 'Эпигенетическая регуляция', 'length': 3.8},
    {'title': 'Динамика сворачивания белков', 'length': 4.0},
    {'title': 'Экологические взаимодействия', 'length': 0.7},
    {'title': 'Модели нейронных сетей', 'length': 4.3},
    {'title': 'Пути биолюминесценции', 'length': 2.9}
]


async def upload_article(article):
    await asyncio.sleep(article['length'])
    article['loop'] = asyncio.get_running_loop()
    return article

async def main():
    tasks = [asyncio.create_task(upload_article(article)) for article in articles]
    await asyncio.gather(*tasks)
    # articleswe = await asyncio.gather(*tasks)
    # print(articles)
    # print()
    # print(articleswe)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
