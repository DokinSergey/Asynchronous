import sys,time
import asyncio

def check_loop_status(loop):
    
    return f'Цикл событий активен: {loop.is_running()}, Цикл событий закрыт: {loop.is_closed()}.'



async def main():
    print(check_loop_status(loop))
    print("Корутина завершена")

loop = asyncio.new_event_loop()
print(check_loop_status(loop))
loop.run_until_complete(main())
# print(check_loop_status(loop))
loop.close()
print(check_loop_status(loop))

start_time = time.perf_counter()
# asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
