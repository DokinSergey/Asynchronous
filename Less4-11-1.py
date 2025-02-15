import sys,time
import asyncio

async def switch_loop():
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    current_loop = asyncio.get_running_loop()
    return current_loop is new_loop

loop = asyncio.new_event_loop()
result = loop.run_until_complete(switch_loop())

print(result)
loop.close()


start_time = time.perf_counter()
# asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
