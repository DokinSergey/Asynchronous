import sys,time
import asyncio

lock = asyncio.Lock()

async def coro(num):
    await asyncio.sleep(num * 0.1)
    print(f'Задача {num} выполнена')

async def main():
    
    for i in range(5):
        tasks = asyncio.create_task(coro(i))
    tasks = asyncio.all_tasks() - {asyncio.current_task()}
    # print(type())#
    await asyncio.gather(*tasks)
    print('Работа программы завершена')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
