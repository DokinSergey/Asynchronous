import sys,time

import asyncio

# 0.3
# 0.2
# 0.1

# 0.2
# 0.1
# 0.4(0.5)

# 0.1
# 0.3
# 0.2(0.3)


async def coroutine_1(delay=0.1):
    print("-Первое сообщение от корутины 1")
    await asyncio.sleep(0.3)  # Первая задержка
    print("--Второе сообщение от корутины 1")
    await asyncio.sleep(0.2)  # Вторая задержка
    print("---Третье сообщение от корутины 1")
    await asyncio.sleep(0.1)  # Третья задержка
    print("----Четвертое сообщение от корутины 1")

async def coroutine_2(delay=0.1):
    print("-Первое сообщение от корутины 2")
    await asyncio.sleep(0.2)  # Первая задержка
    print("--Второе сообщение от корутины 2")
    await asyncio.sleep(0.1)  # Вторая задержка
    print("---Третье сообщение от корутины 2")
    await asyncio.sleep(0.4)  # Третья задержка
    print("----Четвертое сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    print("-Первое сообщение от корутины 3")
    await asyncio.sleep(delay)  # Первая задержка
    print("--Второе сообщение от корутины 3")
    await asyncio.sleep(0.3)  # Вторая задержка
    print("---Третье сообщение от корутины 3")
    await asyncio.sleep(0.2)  # Третья задержка
    print("----Четвертое сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )
start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'Общее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
