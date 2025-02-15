import sys,time
import asyncio

import random

# Не менять!
random.seed(1)

async def collect_gold():
    delay = random.randint(1,5)
    await asyncio.sleep(delay)
    return random.randint(10,50)

async def main():
    total = 0
    tasks = [asyncio.create_task(collect_gold()) for i in range(10)]
    for completed_task in asyncio.as_completed(tasks):
        amount = await completed_task
        print(f"Собрано {amount} единиц золота.")
        total += amount
        print(f"Общее количество золота: {total} единиц.")
        print()

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
