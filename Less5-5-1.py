import sys,time
import asyncio
import random
# Не менять!
async def main():
    print("Основная корутина запущена")
    task = asyncio.current_task()
    result = asyncio.gather(task)
    await result


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
