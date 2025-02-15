import sys,time
from random import random
import asyncio


async def producer(queue):
    print('Производитель: Запущен')
    for _ in range(10):
        value = random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print('Производитель: Done')


async def consumer(queue):
    print('Потребитель: Запущен')
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'>Потребитель получил: {item}')
    print('Потребитель: Done')


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
