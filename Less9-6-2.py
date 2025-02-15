import sys,time
import asyncio
#pylint: disable-msg=W0603

async def convert_file(file_name,semaphore):
    async with semaphore:
        await asyncio.sleep(1)
        return f"Файл {file_name} обработан"

async def main():
    while (akkaunt := input(':->')):
        files = input(':->').split()
        # akkaunt = input(':->')
        if akkaunt == 'premium': semaphore = asyncio.BoundedSemaphore(10)
        elif akkaunt == 'free': semaphore = asyncio.BoundedSemaphore(2)
        else: break
        start_time = time.perf_counter()
        tasks = [asyncio.create_task(convert_file(file_name,semaphore)) for file_name in files]
        await asyncio.gather(*tasks)
        for task in tasks:
            print(task)
        stop_time =  time.perf_counter()
        Inetrval = stop_time - start_time
        print(f'\nОбщее время выполнения {Inetrval:.7f}')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
