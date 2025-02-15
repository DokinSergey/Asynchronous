import sys,time
import asyncio

async def print_event_loop(loop):
    current_loop = asyncio.get_running_loop()
    if current_loop == loop:
        print("Переданный цикл событий активен")
    else:
        print("Переданный цикл событий не активен")

loop = asyncio.new_event_loop()
asyncio.run(print_event_loop(loop))

start_time = time.perf_counter()
# asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
