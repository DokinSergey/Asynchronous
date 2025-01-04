import sys

import asyncio
import random

async def waiter(future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")

async def setter(future):
    await asyncio.sleep(random.randint(1,3))
    future.set_result(True)

async def main():
    future = asyncio.Future()
    # task1 = asyncio.create_task(waiter(future))
    # task2 = asyncio.create_task(setter(future))
    # await asyncio.gather(task1,task2)
    
    await asyncio.gather(waiter(future), setter(future))

asyncio.run(main())

if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
