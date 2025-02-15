import sys,time
import asyncio
import random

server_names = {
        "1": "Server_Alpha", "2": "Server_Beta", "3": "Server_Gamma",
        "4": "Server_Delta", "5": "Server_Epsilon"}

async def load_data(server):
    print(f'Загрузка данных с сервера {server} началась')
    await asyncio.sleep(random.randint(0, 5))
    print(f'Загрузка данных с сервера {server} завершена')

async def main():
    tasks = [asyncio.create_task(load_data(server)) for _,server in server_names.items()]
    await asyncio.gather(*tasks)


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
