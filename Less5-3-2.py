import sys,time
import asyncio

async def coroutine_with_return():
    await asyncio.sleep(2) 
    return 42


async def another_coroutine_with_return():
    await asyncio.sleep(1) 
    return 420


async def main():
    task1 = asyncio.create_task(coroutine_with_return())
    task2 = asyncio.create_task(another_coroutine_with_return())

    await task1

    result1 = task1.result()
    result2 = task2.result()

    print(result1)
    print(result2)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
