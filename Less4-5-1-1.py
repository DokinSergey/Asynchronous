import sys,time
import asyncio

async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2

async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2

async def portal_operator():
    task1 = asyncio.ensure_future(activate_portal(2))
    await asyncio.wait([task1])
    res = 1 if task1.result() > 4 else task1.result()
    task2 = asyncio.ensure_future(perform_teleportation(res))
    await asyncio.gather(task2)
    print(f'Результат активации портала: {res} единиц энергии')
    print(f'Результат телепортации: {task2.result()} единиц времени')

start_time = time.perf_counter()
# asyncio.run(main())
asyncio.run(portal_operator())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
