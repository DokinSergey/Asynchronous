import sys,time
import asyncio

async def auto_write_data(condition, name):
    # Блокировка условия
    async with condition:
        print(f'Ожидает получения данных: {name}')
        await condition.wait()
        print(f'{name} добавляются в БД')
        await asyncio.sleep(0.5)
        print(f'Скачанные {name} автоматически записаны в БД')

async def download_data(condition):
    for i in range(3):
        async with condition:
            await asyncio.sleep(0.5) # скачивание данных
            print(f'Данные {i} готовы для записи в БД')
            condition.notify()

async def manual_write_data(lock, data):
    async with lock:
        print(f'{data} добавляются в БД')
        await asyncio.sleep(0.5)
        print(f'{data} добавлены в БД')

async def main():
    lock = asyncio.Lock() # создаем замок
    condition = asyncio.Condition(lock) # используем данный замок при создании объекта Condition
    tasks = [asyncio.create_task(auto_write_data(condition, f'данные {i}')) for i in range(3)]
    manual_task = asyncio.create_task(manual_write_data(lock, 'данные из другого источника'))
    await asyncio.gather(download_data(condition), *tasks, manual_task)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
