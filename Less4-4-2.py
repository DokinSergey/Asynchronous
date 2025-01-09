import sys,time
import asyncio

async def countdown(name, seconds):
    for i in range(seconds,0,-1):
        if name == 'Квест на поиск сокровищ':
            print(f"{name}: Осталось {i} сек. Найди скрытые сокровища!")
        if name == 'Побег от дракона':
            print(f"{name}: Осталось {i} сек. Беги быстрее, дракон на хвосте!")
        await asyncio.sleep(1)
    print(f"{name}: Задание выполнено! Что дальше?")

async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ",10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона",5))
    await asyncio.gather(treasure_hunt,dragon_escape)

start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'Общее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
