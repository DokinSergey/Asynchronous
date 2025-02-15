import sys,time
import asyncio

files = {
    "Начало": 4.2,
    "Матрица": 3.8,
    "Аватар": 5.1,
    "Интерстеллар": 2.6,
    "Паразиты": 6.0,
    "Джокер": 4.5,
    "Довод": 3.3,
    "Побег из Шоушенка": 5.4,
    "Криминальное чтиво": 2.9,
    "Форрест Гамп": 5.8,
}

async def upload_file(filename, delay):
    await asyncio.sleep(delay)
    return filename

async def main():
    tasks = [asyncio.create_task(upload_file(filename,delay)) for filename,delay in files.items()]
    for completed_task in asyncio.as_completed(tasks):
        filename = await completed_task
        print(f"{filename}: фильм загружен на сервер")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
