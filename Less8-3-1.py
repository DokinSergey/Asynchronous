import sys,time
import asyncio

async def autosave(queue,_time):
    queue.put_nowait(f'Автосохранение {_time}')
    await asyncio.sleep(0)
    print(f"Автосохранение игры через {_time} часов")


async def simulate_gameplay(queue):
    _autosave = queue.get_nowait()
    print(f"Загружена последняя версия игры: {_autosave}")
    await asyncio.sleep(0)

async def main():
    queue = asyncio.LifoQueue()
    for i in range(1,21):
        await(autosave(queue,i))
        await asyncio.sleep(0.1)
        if not i%5:await(simulate_gameplay(queue))
    print('Игра пройдена!')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
