import sys,time
import asyncio

equipment_list = ['#001 ps5f6537c5-506f-43c2-b095-1890ef579c52: 265 units',
                  '#002 ps5ec3020b-022f-466b-845a-a8f11161a6d1: 39 units',
                  '#003 psb5c6c090-4f1a-4741-936e-5fe2b3e8d181: 242 units',
                  '#004 ps10c90127-a4a5-4f85-b23f-66421ab04b09: 108 units',
                  '#005 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units']

# Корутина для отправки запроса.
async def equipment_request(request):
    await asyncio.sleep(1)
    res = request.split()[0]
    return f'{res} is Ok'

async def send_requests():
    results = await asyncio.gather(*[equipment_request(request) for request in equipment_list])
    print(f'На отправку {len(results)} запросов потребовалось  секунд!')
    print(*results,sep = '\n')

start_time = time.perf_counter()
asyncio.run(send_requests())
# asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
