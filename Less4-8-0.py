import sys,time
import asyncio

processors_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
    'AMD Ryzen 9 5900X': 8.4,
    'AMD Ryzen 7 5800X': 3.55,
    'AMD Ryzen 5 5600X': 1.15,
    'Intel Core i9-10900K': 1.8,
    'Intel Core i7-10700K': 5.58,
    'Intel Core i5-10600K': 2.01,
    'AMD Ryzen 9 3950X': 6.19,
    'AMD Ryzen 9 3900X': 3.08,
    'AMD Ryzen 7 3800X': 4.1,
    'AMD Ryzen 5 3600X': 6.13,
    'Intel Core i9-9900K': 1.16,
    'Intel Core i7-9700K': 2.46,
    'Intel Core i5-9600K': 4.91,
    'AMD Ryzen 9 3850X': 1.33,
    'AMD Ryzen 9 3750X': 7.62,
    'AMD Ryzen 7 3700X': 6.67,
    'AMD Ryzen 5 3500X': 5.65,
    'Intel Core i9-10850K': 8.89,
    'Intel Core i7-10600K': 8.37,
    'Intel Core i5-10400F': 3.07,
    'AMD Ryzen 9 3950XT': 4.37,
    'AMD Ryzen 9 3900XT': 3.92,
    'AMD Ryzen 7 3800XT': 1.93,
    'AMD Ryzen 5 3600XT': 3.55,
    'Intel Core i9-10980XE': 1.67,
    'Intel Core i7-10700F': 6.79
}

async def simulate_processing(delay):
    await asyncio.sleep(delay)
    return delay

async def main():
    tasks = [asyncio.create_task(simulate_processing(delay),name = proc) for proc,delay in processors_delays.items()]
    done,_ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    d = {}
    for task in done:
        d[task.get_name()] = task.result()
    # print(d)
    print(min(list(d.values())))
    minpros = [key for key, val in d.items() if val == min(list(processors_delays.values()))][0]
    # # for task in done:
    # # print(list(mydict.keys())[list(mydict.values()).index(16)])
    print(f"Первый завершенный процесс: {minpros}")


start_time = time.perf_counter()
asyncio.run(main())

stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
