import sys,time
import asyncio
#pylint: disable-msg=W0603

sem = asyncio.Semaphore(3) # Создаем сефамор с начальным значением счетчика 3.

async def task(id):
    async with sem:  # Семафор захватывается и освобождается с помощью менеджера контекста
        print(f'Задача {id} начала выполнение')
        await asyncio.sleep(1)
        print(f'Задача {id} завершила выполнение')


async def main():
    tasks = [task(i) for i in range(10)]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
