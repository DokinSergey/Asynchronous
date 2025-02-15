import sys,time
import asyncio

import random

random.seed(5)

def on_data_parsed(task):
    result = task.result()
    print(f"Найдено {len(result)} файлов для скачивания: {result}")



async def parse_data(url):
    await asyncio.sleep(1)
    if random.choice([True, False]):
        file_urls = [f"{url}/example_file.zip"]
        current_task = asyncio.current_task()
        current_task.add_done_callback(on_data_parsed)
    else:
        file_urls = []
    return file_urls


async def main():
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3"
    ]
    tasks = [asyncio.create_task(parse_data(url)) for url in urls]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
