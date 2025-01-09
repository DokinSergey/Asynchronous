import sys,time
import asyncio

async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    res = x * 2
    # print(f'Результат активации портала: {res} единиц энергии')
    return res

async def perform_teleportation(x):
    res = x + 2
    print(f'Телепортация в процессе, требуется времени: {res} единиц')
    await asyncio.sleep(x)
    
    # print(f'Результат телепортации: {res} единиц времени')
    return res

async def portal_operator():
    task_act = await asyncio.ensure_future(activate_portal(2))
    res_act = 1 if task_act > 4 else task_act
    task_tele = await asyncio.ensure_future(perform_teleportation(res_act))
    # await asyncio.gather(task_act,task_act)
    
    print(f'Результат активации портала: {task_act} единиц энергии')
    print(f'Результат телепортации: {task_tele} единиц времени')

start_time = time.perf_counter()
# asyncio.run(main())
asyncio.run(portal_operator())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
