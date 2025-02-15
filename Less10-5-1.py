import os,sys,time
# from glob import glob
from rich import print as rpn
import asyncio
from aiohttp import ClientSession
# import aiofiles
start_time = time.perf_counter()
#pylint: disable-msg=W0603


async def fetch(url, session):
    # Отправка GET-запроса к URL
    async with session.get(url) as response:
        # Извлечение текста ответа
        data = await response.text()
        # Вывод информации текст и урл
        print(data[:5], response.url)

async def main():
    url = "http://asyncio.ru/example/index.html"
    tasks = []
    # Создание клиентской сессии для управления соединениями
    async with ClientSession() as session:
        for i in range(30000):
            # Добавление задачи в список задач
            task = asyncio.create_task(fetch(url, session))
            tasks.append(task)

        # Ожидание завершения всех задач
        responses = asyncio.gather(*tasks)
        await responses

asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
