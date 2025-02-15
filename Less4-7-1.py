import sys,time
import asyncio

runners = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,

}

async def run_lap(name, speed):
    time_needed = round(100/speed,2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")

async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    tasks = [asyncio.create_task(run_lap(name, speed)) for name, speed in runners.items()]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_time)
    except TimeoutError:
        print("Задача не была завершена в установленное время")

start_time = time.perf_counter()

asyncio.run(main())

stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
