import sys,time

import asyncio


async def coroutine_1():
    await asyncio.sleep(1.5)  # Задержка для первого сообщения
    print("Сообщение 1 от корутины 1")
    await asyncio.sleep(1.0)  # Задержка для второго сообщения
    print("\tСообщение 2 от корутины 1")

async def coroutine_2():
    await asyncio.sleep(1.5)
    print("Сообщение 1 от корутины 2")
    await asyncio.sleep(1.7)
    print("\tСообщение 2 от корутины 2")

async def coroutine_3():
    await asyncio.sleep(1.5)
    print("Сообщение 1 от корутины 3")
    await asyncio.sleep(2.8)
    print("\tСообщение 2 от корутины 3")

async def coroutine_4():
    await asyncio.sleep(1.5)
    print("Сообщение 1 от корутины 4")
    await asyncio.sleep(1.1)
    print("\tСообщение 2 от корутины 4")

async def coroutine_5():
    await asyncio.sleep(1.5)
    print("Сообщение 1 от корутины 5")
    await asyncio.sleep(2.4)
    print("\tСообщение 2 от корутины 5")

async def coroutine_6():
    await asyncio.sleep(2.0)
    print("Сообщение 1 от корутины 6")
    await asyncio.sleep(1.9)
    print("\tСообщение 2 от корутины 6")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
        coroutine_4(),
        coroutine_5(),
        coroutine_6(),
    )


start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'Общее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
