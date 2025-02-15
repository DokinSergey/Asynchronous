import sys,time
import asyncio
import random

ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}

async def scan_port(address, port):
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        print(f'Port {port} on {address} is open')
        return port
    return

async def scan_range(address, ports):
    print(f'Scanning ports {ports[0]} - {ports[1]} on {address}')
    await asyncio.sleep(1)
    _tasks = [asyncio.create_task(scan_port(address, port)) for port in range(ports[0],ports[1] + 1)]
    await asyncio.gather(*_tasks)
    # if (open_ports := [task.result() for task in _tasks if task.result()]):
        # print(f'Открытые порты на адресе {address}: {open_ports}')
    # else:print(f'Открытых портов на адресе {address} не найдено')
    return (address,[task.result() for task in _tasks if task.result() or task.result() == 0],)

async def main(dct):
    tasks = [asyncio.create_task(scan_range(address, ports)) for address,ports in dct.items()]
    await asyncio.gather(*tasks)
    for task in tasks:
        res = task.result()
        if len(res) > 1 and res[1]:
            print(f'Всего найдено открытых портов {len(res[1])} {res[1]} для ip: {res[0]}')

start_time = time.perf_counter()
asyncio.run(main(ip_dct))
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
