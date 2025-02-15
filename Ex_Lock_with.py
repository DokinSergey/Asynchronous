import sys,time
import asyncio

counter = 0

# Создаем объект lock для управления доступом к counter
lock = asyncio.Lock()

async def worker_1():
    global counter
    # Захватываем lock, чтобы исключить конкурентный доступ к counter
    async with lock:
        for i in range(10):
            counter += 1
            print(f"Переменная увеличена на 1 из корутины worker_1, counter = {counter}")
            await asyncio.sleep(1)

async def worker_2():
    global counter
    # Захватываем lock, чтобы исключить конкурентный доступ к counter
    async with lock:
        for i in range(10):
            counter += 1
            print(f"Переменная увеличена на 1 из корутины worker_2, counter = {counter}")
            await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    await task1
    await task2

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
