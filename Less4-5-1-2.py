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

async def recharge_portal(x): 
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 3

async def check_portal_stability(x):
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 4

async def restore_portal(x): 
    print(f'Восстановление портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 5

async def close_portal(x):
    print(f'Закрытие портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x - 1

async def portal_operator():
    
    active = asyncio.ensure_future(activate_portal(2))
    await active
    n = 1 if active.result() > 4 else active.result()
    jump = asyncio.ensure_future(perform_teleportation(n))
    await jump
    print(f'Результат активации портала: {n} единиц энергии')
    print(f'Результат телепортации: {jump.result()} единиц времени')

start_time = time.perf_counter()
# asyncio.run(main())
asyncio.run(portal_operator())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
