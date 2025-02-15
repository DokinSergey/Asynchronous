import sys,time
import asyncio

robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']

lock = asyncio.Lock()

spot_counter = 0

async def motion_robot(robot):
    global spot_counter
    async with lock:
        print(f"Робот {robot} передвигается к месту A")
        await asyncio.sleep(0.1)
        spot_counter += 1
        print(f"Робот {robot} достиг места A. Место A посещено {spot_counter} раз")

async def main():
    tasks = [asyncio.create_task(motion_robot(f'{name}({i})')) for i,name in enumerate(robot_names) ]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
