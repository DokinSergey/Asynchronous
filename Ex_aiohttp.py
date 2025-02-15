import sys,time
import asyncio
import aiohttp

async def fetch(url):
    asyncio.current_task().set_name(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return url, (await response.text())[:60]


async def main():
    urls = [
        'https://www.example.com/',
        'https://www.google.com/',
        'https://www.github.com/',
        'https://docs.python.org/3.12/',
        'https://docs.python.org/3.11/',
        'https://stepik.org/'
    ]

    # Создаем список задач, где часть защищена, часть - нет.
    shielded_and_usual_tasks = []
    for url in urls:
        if 'python' in url:
            task = asyncio.shield(fetch(url))
        else:
            task = asyncio.create_task(fetch(url))
        shielded_and_usual_tasks.append(task)

    # Получаем список всех задач в цикле событий кроме задачи, созданной из main()
    tasks = [task for task in asyncio.all_tasks() if task.get_name() != 'Task-1']

    # Получаем результат первого ответа, остальные попытаемся отменить
    done, pending = await asyncio.wait(shielded_and_usual_tasks, return_when=asyncio.FIRST_COMPLETED)
    print(*[f"Первая выполненная задача: {future.result()}" for future in done])
    [future.cancel() for future in pending]
    print(f'\nОтменяем: {len(pending)} задач')

    # Дожидаемся завершения всех задач.
    for task in tasks:
        try:
            result = await task
            print(f"Результат выполнения задачи {task.get_name()}: {result}")
        except asyncio.CancelledError as ex:
            print(f"Ошибка в задаче - задача {task.get_name()} отменена: {type(ex)}")


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
