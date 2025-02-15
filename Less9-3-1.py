import sys,time
import asyncio

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

#events = [asyncio.Event() for _ in ip]
alarm = asyncio.Event()

async def Sensor_operation(Sensor:tuple):
    print(f'Датчик {Sensor[0]} IP-адрес {Sensor[1]} настроен и ожидает срабатывания')
    await alarm.wait()
    print(f'Датчик {Sensor[0]} IP-адрес {Sensor[1]} активирован, "Wee-wee-wee-wee"')

async def Alarm_operation():
    print('Датчики зафиксировали движение')
    alarm.set()

async def main():
    tasks = [asyncio.create_task(Sensor_operation((i,sip))) for i,sip in enumerate(ip)]
    tasks.append(asyncio.create_task(Alarm_operation()))
    await asyncio.gather(*tasks)



start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
